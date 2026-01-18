# Project: om-exporter

## Quick Summary

Export Open-Meteo's `.om` file format to common meteorology formats. Provides tools for reading weather data from AWS S3, handling various grid types (Regular, Projection, Gaussian), and converting ECMWF Gaussian grids to regular lat-lon grids.

## Tech Stack

- **Language**: Python 3.13+
- **Package Manager**: uv
- **Key Dependencies**:
  - `omfiles` - Read .om file format
  - `s3fs` - AWS S3 filesystem access
  - `numpy`, `scipy` - Numerical computation & interpolation
  - `xarray` - N-dimensional arrays
  - `click` - CLI framework

## Project Structure

```
src/om_exporter/
├── __init__.py
├── build.py           # Grid factory functions (build_grid_from_domain)
├── cli.py             # Command-line interface
├── conf/
│   └── domain.py      # Pre-defined grid configurations (DOMAIN_GRIDS)
├── converter/
│   └── gasssian.py    # Gaussian to Regular grid converter
└── grid/
    ├── __init__.py    # Grid types: RegularGrid, ProjectionGrid, GaussianGrid
    └── gaussian_grid.py  # GaussianGridType enum with grid math
```

## Development Commands

```bash
# Install dependencies
uv sync

# Format code
make fmt

# Lint code
make lint

# Run tests
uv run pytest

# CLI usage
uv run om-export --help
```

## Code Conventions

- **Naming**: snake_case for files/functions, PascalCase for classes
- **Types**: Use type hints everywhere, prefer `dataclass` for data containers
- **Grid data layout**: `(n_points, n_times)` for 1D grids, `(ny, nx, n_times)` for 2D outputs
- **Imports**: Use relative imports within package (`from .grid import ...`)
- **Linting**: ruff with rules E4, E7, E9, F, I, RUF022

## Key Files

| File | Purpose |
|------|---------|
| `grid/__init__.py` | Grid type definitions (RegularGrid, ProjectionGrid, GaussianGrid) |
| `grid/gaussian_grid.py` | GaussianGridType enum with coordinate calculations |
| `converter/gasssian.py` | GaussianToRegularConverter for grid interpolation |
| `conf/domain.py` | DOMAIN_GRIDS dict with pre-configured grid specs |
| `build.py` | `build_grid_from_domain()` factory function |

## Common Workflows

### Read & Convert Gaussian Grid Data

```python
from s3fs import S3FileSystem
from omfiles.omfiles import OmFileReader
from om_exporter.build import build_grid_from_domain
from om_exporter.converter.gasssian import GaussianToRegularConverter

# Read from S3
fs = S3FileSystem(anon=True)
reader = OmFileReader.from_fsspec(fs, "openmeteo/data_run/ecmwf_ifs/.../precipitation.om")
data = reader[:]  # (n_points, n_times)

# Convert to regular grid
grid = build_grid_from_domain('EcmwfEcpdsDomain', 'ifs')
converter = GaussianToRegularConverter(grid.grid_type)
target = converter.build_target_grid(target_resolution=(0.25, 0.25))
data_regular = converter.interpolate(data, target)  # (ny, nx, n_times)
```

## Notes

- Gaussian grid types: O320, O1280 (octahedral), N160, N320 (classic)
- File `gasssian.py` has typo in name (3 s's) - intentional, don't rename
