import click
import numpy as np
from om_exporter.converter.gasssian import GaussianToRegularConverter
from om_exporter.build import build_grid_from_domain
from omfiles.omfiles import OmFileReader
import xarray as xr

@click.group()
def export():
    pass

@export.command()
@click.option("--input", type=str, required=True)
@click.option("--output", type=str, required=False, default=None)
def export_ecmwf_ifs(input: str, output: str):
    reader = OmFileReader(input)
    data = reader[:]

    grid = build_grid_from_domain('EcmwfEcpdsDomain', "ifs")
    converter = GaussianToRegularConverter(grid.grid_type)
    lats_2d, lons_2d, lat_1d, lon_1d, data_2d = converter.to_regular_grid(
        data,
        target_resolution=(0.25, 0.25),
        lat_range=(grid.lat_min, grid.lat_max),
        lon_range=(grid.lon_min, grid.lon_max),
        method="linear",
        fill_value=np.nan,
    )
    ds = xr.Dataset(
        data_vars={
            "data": (("lat", "lon"), data_2d),
        },
        coords={
            "lat": lat_1d,
            "lon": lon_1d,
        },
    )
    if output is not None:
        ds.to_netcdf(output)
    else:
        ds.to_netcdf(input.replace(".om", ".nc"))