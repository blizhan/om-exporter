"""网格类型定义。

包含三类网格：
- RegularGrid: 规则经纬度网格
- ProjectionGrid: 投影网格（兰伯特等角圆锥、旋转经纬度等）
- GaussianGrid: 高斯网格（O/N 系列）

TypedDict 类型用于 JSON 配置解析，dataclass 用于运行时操作。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Literal, Optional, Tuple, TypedDict, Union

import numpy as np

from .gaussian_grid import GaussianGridType

Range = Tuple[float, float]
LatLonValue = Union[float, Range]

GridTypeName = Literal["RegularGrid", "ProjectionGrid", "GaussianGrid"]
ProjectionTypeName = Literal[
    "LambertConformalConicProjection",
    "RotatedLatLonProjection",
    "StereographicProjection",
    "LambertAzimuthalEqualAreaProjection",
]

__all__ = [
    # 类型别名
    "GridTypeName",
    "ProjectionTypeName",
    # TypedDict (配置解析)
    "GridSpec",
    "ProjectionDef",
    "RegularGridParams",
    "ProjectionGridParams",
    "GaussianGridParams",
    # Projection dataclass
    "LambertConformalConicProjection",
    "RotatedLatLonProjection",
    "StereographicProjection",
    "LambertAzimuthalEqualAreaProjection",
    "Projection",
    # Grid dataclass
    "RegularGrid",
    "ProjectionGrid",
    "GaussianGrid",
    "Grid",
    # 高斯网格
    "GaussianGridType",
]


# ============================================================================
# TypedDict 定义 (用于 JSON 配置解析)
# ============================================================================

class LambertConformalConicParams(TypedDict):
    lambda0: float
    phi0: float
    phi1: float
    phi2: float
    radius: float


class RotatedLatLonParams(TypedDict):
    latitude: float
    longitude: float


class StereographicParams(TypedDict):
    latitude: float
    longitude: float
    radius: float


class LambertAzimuthalEqualAreaParams(TypedDict):
    lambda0: float
    phi1: float
    radius: float


ProjectionParams = Union[
    LambertConformalConicParams,
    RotatedLatLonParams,
    StereographicParams,
    LambertAzimuthalEqualAreaParams,
]


class ProjectionDef(TypedDict):
    type: ProjectionTypeName
    params: ProjectionParams


class RegularGridParamsRequired(TypedDict):
    nx: int
    ny: int
    latMin: float
    lonMin: float
    dx: float
    dy: float


class RegularGridParams(RegularGridParamsRequired, total=False):
    searchRadius: int


class ProjectionGridParamsRequired(TypedDict):
    nx: int
    ny: int
    projection: ProjectionDef


class ProjectionGridParams(ProjectionGridParamsRequired, total=False):
    latitude: LatLonValue
    longitude: LatLonValue
    latitudeProjectionOrigin: float
    longitudeProjectionOrigin: float
    dx: float
    dy: float


class GaussianGridParams(TypedDict):
    grid_type: str  # GaussianGridType.value


GridParams = Union[RegularGridParams, ProjectionGridParams, GaussianGridParams]


class GridSpec(TypedDict):
    type: GridTypeName
    params: GridParams


DomainGridMap = Dict[str, Dict[str, GridSpec]]


# ============================================================================
# Projection dataclass
# ============================================================================

@dataclass(frozen=True)
class LambertConformalConicProjection:
    """兰伯特等角圆锥投影。"""
    lambda0: float
    phi0: float
    phi1: float
    phi2: float
    radius: float


@dataclass(frozen=True)
class RotatedLatLonProjection:
    """旋转经纬度投影。"""
    latitude: float
    longitude: float


@dataclass(frozen=True)
class StereographicProjection:
    """球极平面投影。"""
    latitude: float
    longitude: float
    radius: float


@dataclass(frozen=True)
class LambertAzimuthalEqualAreaProjection:
    """兰伯特等面积方位投影。"""
    lambda0: float
    phi1: float
    radius: float


Projection = Union[
    LambertConformalConicProjection,
    RotatedLatLonProjection,
    StereographicProjection,
    LambertAzimuthalEqualAreaProjection,
]


# ============================================================================
# Grid dataclass
# ============================================================================

@dataclass(frozen=True)
class RegularGrid:
    """规则经纬度网格。"""
    nx: int
    ny: int
    lat_min: float
    lon_min: float
    dx: float
    dy: float
    search_radius: int = 1

    @property
    def count(self) -> int:
        """总点数。"""
        return self.nx * self.ny

    @property
    def is_global_lon(self) -> bool:
        """经度方向是否覆盖全球。"""
        return self.nx * self.dx >= 359

    @property
    def is_global_lat(self) -> bool:
        """纬度方向是否覆盖全球。"""
        return self.ny * self.dy >= 179

    def find_point_xy(self, lat: float, lon: float) -> Tuple[int, int]:
        """找到最接近给定经纬度的网格点 (x, y) 坐标。

        Args:
            lat: 纬度
            lon: 经度

        Returns:
            (x, y) 网格坐标

        Raises:
            ValueError: 如果坐标超出网格范围
        """
        x = int(round((lon - self.lon_min) / self.dx))
        y = int(round((lat - self.lat_min) / self.dy))

        # 全球网格边界处理
        if self.is_global_lon:
            if x == -1:
                x = 0
            elif x in (self.nx, self.nx + 1):
                x = self.nx - 1

        if self.is_global_lat:
            if y == -1:
                y = 0
            elif y == self.ny:
                y = self.ny - 1

        if y < 0 or x < 0 or y >= self.ny or x >= self.nx:
            raise ValueError(
                f"坐标超出网格范围: lat={lat}, lon={lon}, "
                f"x={x}, y={y}, nx={self.nx}, ny={self.ny}"
            )

        return x, y

    def find_point(self, lat: float, lon: float) -> int:
        """找到最接近给定经纬度的网格点索引（一维）。

        Args:
            lat: 纬度
            lon: 经度

        Returns:
            网格点在一维数组中的索引 (y * nx + x)
        """
        x, y = self.find_point_xy(lat, lon)
        return y * self.nx + x

    def get_lat_lon_arrays(self) -> Tuple[np.ndarray, np.ndarray]:
        """获取所有网格点的经纬度坐标（一维数组）。

        Returns:
            (lats, lons): 两个一维数组，长度为 count，按 (y * nx + x) 顺序排列
        """
        lat_1d = np.arange(self.ny, dtype=np.float64) * self.dy + self.lat_min
        lon_1d = np.arange(self.nx, dtype=np.float64) * self.dx + self.lon_min
        lons_2d, lats_2d = np.meshgrid(lon_1d, lat_1d)
        return lats_2d.ravel(), lons_2d.ravel()

    def get_lat_lon_2d(self) -> Tuple[np.ndarray, np.ndarray]:
        """获取所有网格点的经纬度坐标（二维数组）。

        Returns:
            (lats_2d, lons_2d): 两个二维数组，形状为 (ny, nx)
        """
        lat_1d = np.arange(self.ny, dtype=np.float64) * self.dy + self.lat_min
        lon_1d = np.arange(self.nx, dtype=np.float64) * self.dx + self.lon_min
        return np.meshgrid(lon_1d, lat_1d)[::-1]  # 返回 (lats_2d, lons_2d)

    def reshape_to_2d(self, data: np.ndarray) -> np.ndarray:
        """将一维数据重塑为二维网格。

        Args:
            data: 一维数据数组，长度必须等于 count

        Returns:
            二维数组，形状为 (ny, nx)
        """
        if data.size != self.count:
            raise ValueError(f"数据长度不匹配: 期望 {self.count}, 实际 {data.size}")
        return data.reshape(self.ny, self.nx)


@dataclass(frozen=True)
class ProjectionGrid:
    """投影网格。"""
    nx: int
    ny: int
    projection: Projection
    latitude: Optional[LatLonValue] = None
    longitude: Optional[LatLonValue] = None
    latitude_projection_origin: Optional[float] = None
    longitude_projection_origin: Optional[float] = None
    dx: Optional[float] = None
    dy: Optional[float] = None


@dataclass(frozen=True)
class GaussianGrid:
    """高斯网格。
    
    直接使用 GaussianGridType 枚举，可访问所有网格操作方法。
    """
    grid_type: GaussianGridType

    @property
    def count(self) -> int:
        """总点数。"""
        return self.grid_type.count

    def get_lat_lon_arrays(self):
        """获取所有网格点的经纬度坐标。"""
        return self.grid_type.get_lat_lon_arrays()

    def find_point(self, lat: float, lon: float) -> int:
        """找到最接近给定经纬度的网格点索引。"""
        return self.grid_type.find_point(lat, lon)


Grid = Union[RegularGrid, ProjectionGrid, GaussianGrid]
