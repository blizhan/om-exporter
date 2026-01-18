"""高斯网格转换器。"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np

from ..grid import GaussianGridType


@dataclass
class TargetGrid:
    """目标规则网格（缓存计算结果）。"""

    lat_1d: np.ndarray
    lon_1d: np.ndarray
    lats_2d: np.ndarray
    lons_2d: np.ndarray
    points_tgt: np.ndarray  # 用于插值的目标点坐标

    @property
    def shape(self) -> Tuple[int, int]:
        """目标网格形状 (ny, nx)。"""
        return self.lats_2d.shape


class GaussianToRegularConverter:
    """将高斯网格数据转换为规则经纬度网格。

    支持一维和二维数据：
    - 1D: shape (n_points,) -> 输出 (ny, nx)
    - 2D: shape (n_points, n_times) -> 输出 (ny, nx, n_times)

    Example:
        converter = GaussianToRegularConverter(GaussianGridType.O1280)

        # 预先构建目标网格（可复用）
        target = converter.build_target_grid(
            target_resolution=(0.25, 0.25),
            lat_range=(15.0, 55.0),
            lon_range=(70.0, 140.0),
        )

        # 批量转换多个时间步
        # data shape: (n_points, n_times)
        data_out = converter.interpolate(data, target, method="nearest")
        # data_out shape: (ny, nx, n_times)
    """

    def __init__(self, grid_type: GaussianGridType):
        self.grid_type = grid_type
        self._coords_cache: Optional[Tuple[np.ndarray, np.ndarray]] = None
        self._points_src_cache: Optional[np.ndarray] = None
        self._kdtree_cache = None

    @property
    def source_coords(self) -> Tuple[np.ndarray, np.ndarray]:
        """源网格坐标（缓存）。"""
        if self._coords_cache is None:
            self._coords_cache = self.grid_type.get_lat_lon_arrays()
        return self._coords_cache

    @property
    def points_src(self) -> np.ndarray:
        """源网格点坐标数组 (n_points, 2)，用于插值。"""
        if self._points_src_cache is None:
            lats_src, lons_src = self.source_coords
            self._points_src_cache = np.column_stack([lons_src, lats_src])
        return self._points_src_cache

    @property
    def kdtree(self):
        """KDTree（用于最近邻插值，缓存）。"""
        if self._kdtree_cache is None:
            from scipy.spatial import cKDTree

            self._kdtree_cache = cKDTree(self.points_src)
        return self._kdtree_cache

    def build_target_grid(
        self,
        target_resolution: Tuple[float, float] = (0.25, 0.25),
        lat_range: Optional[Tuple[float, float]] = None,
        lon_range: Optional[Tuple[float, float]] = None,
    ) -> TargetGrid:
        """构建目标规则网格（可复用）。

        Args:
            target_resolution: 目标网格分辨率 (dlat, dlon)，单位：度
            lat_range: 纬度范围 (lat_min, lat_max)
            lon_range: 经度范围 (lon_min, lon_max)

        Returns:
            TargetGrid 对象，可用于多次插值
        """
        dlat, dlon = target_resolution
        if dlat <= 0.0 or dlon <= 0.0:
            raise ValueError(f"target_resolution 必须为正数: {target_resolution}")

        info = self.grid_type.info
        lat_min = lat_range[0] if lat_range else float(info["lat_min"])
        lat_max = lat_range[1] if lat_range else float(info["lat_max"])
        lon_min = lon_range[0] if lon_range else -180.0
        lon_max = lon_range[1] if lon_range else 180.0

        lat_1d = np.arange(lat_min, lat_max + dlat / 2.0, dlat, dtype=np.float64)
        lon_1d = np.arange(lon_min, lon_max + dlon / 2.0, dlon, dtype=np.float64)
        lons_2d, lats_2d = np.meshgrid(lon_1d, lat_1d)
        points_tgt = np.column_stack([lons_2d.ravel(), lats_2d.ravel()])

        return TargetGrid(
            lat_1d=lat_1d,
            lon_1d=lon_1d,
            lats_2d=lats_2d,
            lons_2d=lons_2d,
            points_tgt=points_tgt,
        )

    def interpolate(
        self,
        data: np.ndarray,
        target: TargetGrid,
        method: str = "nearest",
        fill_value: float = np.nan,
    ) -> np.ndarray:
        """将高斯网格数据插值到目标规则网格。

        Args:
            data: 数据数组
                - 1D: shape (n_points,)
                - 2D: shape (n_points, n_times)
            target: 目标网格（由 build_target_grid 创建）
            method: 插值方法 ('nearest', 'linear', 'cubic')
            fill_value: 插值区域外的填充值

        Returns:
            插值后的数据
            - 1D 输入 -> shape (ny, nx)
            - 2D 输入 -> shape (ny, nx, n_times)
        """
        data = np.asarray(data)
        is_2d = data.ndim == 2

        # 验证数据形状
        n_points = data.shape[0]
        if n_points != self.grid_type.count:
            raise ValueError(
                f"数据长度不匹配: 期望 {self.grid_type.count}, 实际 {n_points}"
            )

        if method == "nearest":
            return self._interpolate_nearest(data, target, is_2d)
        return self._interpolate_scipy(data, target, method, fill_value, is_2d)

    def _interpolate_nearest(
        self,
        data: np.ndarray,
        target: TargetGrid,
        is_2d: bool,
    ) -> np.ndarray:
        """最近邻插值（使用 KDTree，高效）。"""
        # 查询最近邻索引（只需要计算一次）
        _, indices = self.kdtree.query(target.points_tgt)
        ny, nx = target.shape

        if is_2d:
            # (n_points, n_times) -> (ny, nx, n_times)
            n_times = data.shape[1]
            # 使用高级索引一次性完成，避免循环
            result = data[indices].reshape(ny, nx, n_times)
            return result

        # 单帧: (n_points,) -> (ny, nx)
        return data[indices].reshape(ny, nx)

    def _interpolate_scipy(
        self,
        data: np.ndarray,
        target: TargetGrid,
        method: str,
        fill_value: float,
        is_2d: bool,
    ) -> np.ndarray:
        """使用 scipy.interpolate.griddata 插值。"""
        from scipy.interpolate import griddata

        ny, nx = target.shape

        if is_2d:
            # (n_points, n_times) -> (ny, nx, n_times)
            n_times = data.shape[1]
            result = np.empty((ny, nx, n_times), dtype=np.float64)
            for t in range(n_times):
                interp = griddata(
                    self.points_src,
                    data[:, t],
                    target.points_tgt,
                    method=method,
                    fill_value=fill_value,
                )
                result[:, :, t] = interp.reshape(ny, nx)
            return result

        interp = griddata(
            self.points_src,
            data,
            target.points_tgt,
            method=method,
            fill_value=fill_value,
        )
        return interp.reshape(ny, nx)
