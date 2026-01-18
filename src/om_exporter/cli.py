import click
import numpy as np
import xarray as xr
from omfiles.omfiles import OmFileReader

from om_exporter.build import build_grid_from_domain
from om_exporter.converter.gasssian import GaussianToRegularConverter


@click.group()
def export():
    pass


@export.command()
@click.option("--input", "input_path", type=str, required=True)
@click.option("--output", "output_path", type=str, required=False, default=None)
def export_ecmwf_ifs(input_path: str, output_path: str | None) -> None:
    """将 ECMWF IFS 高斯网格数据导出为 NetCDF 格式。"""
    reader = OmFileReader(input_path)
    data = reader[:]

    grid = build_grid_from_domain("EcmwfEcpdsDomain", "ifs")
    converter = GaussianToRegularConverter(grid.grid_type)

    # 从 grid_type.info 获取纬度范围，经度使用全球范围
    info = grid.grid_type.info
    lat_min = float(info["lat_min"])
    lat_max = float(info["lat_max"])

    target = converter.build_target_grid(
        target_resolution=(0.25, 0.25),
        lat_range=(lat_min, lat_max),
        lon_range=(-180.0, 180.0),
    )

    data_regular = converter.interpolate(
        data, target, method="linear", fill_value=np.nan
    )

    # 根据数据维度构建 Dataset
    if data_regular.ndim == 2:
        # 单时间步: (ny, nx)
        ds = xr.Dataset(
            data_vars={"data": (("lat", "lon"), data_regular)},
            coords={"lat": target.lat_1d, "lon": target.lon_1d},
        )
    else:
        # 多时间步: (ny, nx, n_times)
        n_times = data_regular.shape[2]
        ds = xr.Dataset(
            data_vars={"data": (("lat", "lon", "time"), data_regular)},
            coords={
                "lat": target.lat_1d,
                "lon": target.lon_1d,
                "time": np.arange(n_times),
            },
        )

    output_file = (
        output_path if output_path is not None else input_path.replace(".om", ".nc")
    )
    ds.to_netcdf(output_file)
