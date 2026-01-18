#!/usr/bin/env python3
"""ECMWF 高斯网格类型定义与操作。

该模块定义高斯网格的核心类型：
- GaussianGridType：网格类型枚举，包含各类型的数学属性

依赖：
- 必需：numpy
"""

from __future__ import annotations

from enum import Enum
from functools import cached_property
from typing import Tuple

import numpy as np


class GaussianGridType(str, Enum):
    """高斯网格类型（ECMWF Gaussian Grid）。

    支持两种格式：
    - O (Octahedral Reduced): O320, O1280
    - N (Classic Reduced): N160, N320
    """

    O320 = "o320"
    O1280 = "o1280"
    N160 = "n160"
    N320 = "n320"

    @property
    def is_octahedral(self) -> bool:
        """是否为八面体缩减高斯网格（O 系列）。"""
        return self in (GaussianGridType.O320, GaussianGridType.O1280)

    @property
    def latitude_lines(self) -> int:
        """半球纬度线数量 L。总纬线数为 2L。"""
        mapping = {
            GaussianGridType.O320: 320,
            GaussianGridType.O1280: 1280,
            GaussianGridType.N160: 160,
            GaussianGridType.N320: 320,
        }
        return mapping[self]

    @property
    def count(self) -> int:
        """总点数。"""
        l = self.latitude_lines
        if self.is_octahedral:
            # O 系列：4L(L+9)
            return 4 * l * (l + 9)
        # TODO N 系列：近似公式（实际需查表）
        return 4 * l * (l + 9)  # 简化处理，实际 N 系列略有不同

    def nx_of(self, y: int) -> int:
        """纬度线 y 上的经度点数（y 范围：0..2L-1）。"""
        l = self.latitude_lines
        if y < 0 or y >= 2 * l:
            raise ValueError(f"y 超出范围: y={y}, 期望 0..{2 * l - 1}")

        if self.is_octahedral:
            if y < l:
                return 20 + y * 4
            return (2 * l - y - 1) * 4 + 20
        # TODO N 系列使用不同公式
        if y < l:
            return 20 + y * 4
        return (2 * l - y - 1) * 4 + 20

    def integral(self, y: int) -> int:
        """纬度线 y 之前所有点的累计数量（前缀和）。"""
        l = self.latitude_lines
        if y < 0 or y > 2 * l:
            raise ValueError(f"y 超出范围: y={y}, 期望 0..{2 * l}")

        if y <= l:
            return 2 * y * y + 18 * y
        # 镜像对称
        remaining = 2 * l - y
        return self.count - (2 * remaining * remaining + 18 * remaining)

    @cached_property
    def dy(self) -> float:
        """纬度线间距（度）。"""
        return 180.0 / (2.0 * self.latitude_lines + 0.5)

    def lat_of(self, y: int) -> float:
        """纬度线 y 的纬度值。"""
        return (self.latitude_lines - y - 1) * self.dy + self.dy / 2.0

    def get_lat_lon_arrays(self) -> Tuple[np.ndarray, np.ndarray]:
        """获取所有网格点的经纬度坐标。

        Returns:
            (lats, lons): 两个一维数组，长度为 count
        """
        l = self.latitude_lines
        total = self.count
        lats = np.empty(total, dtype=np.float64)
        lons = np.empty(total, dtype=np.float64)

        for y in range(2 * l):
            start = self.integral(y)
            nx = self.nx_of(y)
            end = start + nx

            lat = self.lat_of(y)
            dx = 360.0 / nx

            lats[start:end] = lat
            lon_line = np.arange(nx, dtype=np.float64) * dx
            # 标准化到 [-180, 180)
            lon_line = ((lon_line + 180.0) % 360.0) - 180.0
            lons[start:end] = lon_line

        return lats, lons

    def find_point(self, lat: float, lon: float) -> int:
        """找到最接近给定经纬度的网格点索引。"""
        x, y = self.find_point_xy(lat, lon)
        return self.integral(y) + x

    def find_point_xy(self, lat: float, lon: float) -> Tuple[int, int]:
        """找到最接近给定经纬度的网格点 (x, y) 坐标。"""
        l = self.latitude_lines

        # 计算纬线索引
        y_raw = l - 1.0 - ((lat - self.dy / 2.0) / self.dy)
        y = max(0, min(2 * l - 2, int(y_raw)))
        y_upper = y + 1

        nx = self.nx_of(y)
        nx_upper = self.nx_of(y_upper)
        dx = 360.0 / nx
        dx_upper = 360.0 / nx_upper

        lon_wrapped = _wrap_longitude(lon)
        x0 = _round_away_from_zero(lon_wrapped / dx)
        x1 = _round_away_from_zero(lon_wrapped / dx_upper)

        point_lat = self.lat_of(y)
        point_lon = x0 * dx
        point_lat_upper = self.lat_of(y_upper)
        point_lon_upper = x1 * dx_upper

        dist0 = (point_lat - lat) ** 2 + (point_lon - lon_wrapped) ** 2
        dist1 = (point_lat_upper - lat) ** 2 + (point_lon_upper - lon_wrapped) ** 2

        if dist0 < dist1:
            return ((x0 + nx) % nx, y)
        return ((x1 + nx_upper) % nx_upper, y_upper)

    @property
    def info(self) -> dict[str, float | int | str]:
        """网格信息（便于调试/日志）。"""
        l = self.latitude_lines
        return {
            "grid_type": self.value,
            "latitude_lines": 2 * l,
            "total_points": self.count,
            "dy": self.dy,
            "lat_min": -(l * self.dy - self.dy / 2.0),
            "lat_max": l * self.dy - self.dy / 2.0,
        }


def _wrap_longitude(lon: float) -> float:
    """将经度标准化到 [-180, 180)。"""
    return ((lon + 180.0) % 360.0) - 180.0


def _round_away_from_zero(x: float) -> int:
    """远离零的舍入（匹配 Swift 的 round() 行为）。"""
    if x >= 0.0:
        return int(np.floor(x + 0.5))
    return int(np.ceil(x - 0.5))
