"""网格构建函数。"""

from typing import Dict

from .grid import (
    Grid,
    GridSpec,
    GaussianGrid,
    GaussianGridType,
    LambertAzimuthalEqualAreaProjection,
    LambertConformalConicProjection,
    Projection,
    ProjectionDef,
    ProjectionGrid,
    RegularGrid,
    RotatedLatLonProjection,
    StereographicProjection,
)
from .conf.domain import DOMAIN_GRIDS

__all__ = [
    "build_grid",
    "build_grid_from_domain",
]


def build_projection(defn: ProjectionDef) -> Projection:
    """从配置构建投影对象。"""
    projection_type = defn["type"]
    params = defn["params"]
    
    if projection_type == "LambertConformalConicProjection":
        return LambertConformalConicProjection(
            lambda0=params["lambda0"],
            phi0=params["phi0"],
            phi1=params["phi1"],
            phi2=params["phi2"],
            radius=params["radius"],
        )
    if projection_type == "RotatedLatLonProjection":
        return RotatedLatLonProjection(
            latitude=params["latitude"],
            longitude=params["longitude"],
        )
    if projection_type == "StereographicProjection":
        return StereographicProjection(
            latitude=params["latitude"],
            longitude=params["longitude"],
            radius=params["radius"],
        )
    if projection_type == "LambertAzimuthalEqualAreaProjection":
        return LambertAzimuthalEqualAreaProjection(
            lambda0=params["lambda0"],
            phi1=params["phi1"],
            radius=params["radius"],
        )
    raise ValueError(f"Unsupported projection type: {projection_type}")


def build_grid(spec: GridSpec) -> Grid:
    """从配置构建网格对象。"""
    grid_type_name = spec["type"]
    params = spec["params"]
    
    if grid_type_name == "RegularGrid":
        return RegularGrid(
            nx=params["nx"],
            ny=params["ny"],
            lat_min=params["latMin"],
            lon_min=params["lonMin"],
            dx=params["dx"],
            dy=params["dy"],
            search_radius=params.get("searchRadius", 1),
        )
    if grid_type_name == "GaussianGrid":
        return GaussianGrid(grid_type=GaussianGridType(params["grid_type"]))
    if grid_type_name == "ProjectionGrid":
        projection = build_projection(params["projection"])
        return ProjectionGrid(
            nx=params["nx"],
            ny=params["ny"],
            projection=projection,
            latitude=params.get("latitude"),
            longitude=params.get("longitude"),
            latitude_projection_origin=params.get("latitudeProjectionOrigin"),
            longitude_projection_origin=params.get("longitudeProjectionOrigin"),
            dx=params.get("dx"),
            dy=params.get("dy"),
        )
    raise ValueError(f"Unsupported grid type: {grid_type_name}")


def get_grid_spec(
    domain: str,
    name: str,
    registry: Dict[str, Dict[str, GridSpec]] = DOMAIN_GRIDS,
) -> GridSpec:
    return registry[domain][name]


def build_grid_from_domain(
    domain: str,
    name: str,
    registry: Dict[str, Dict[str, GridSpec]] = DOMAIN_GRIDS,
) -> Grid:
    return build_grid(get_grid_spec(domain=domain, name=name, registry=registry))