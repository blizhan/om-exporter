# om-exporter

Export om format from open-meteo [[link](https://github.com/open-meteo/om-file-format)] to common meteology format.  



## Quick Start

从 AWS S3 读取 Open-Meteo 数据并转换为规则网格：

```python
from s3fs import S3FileSystem
from omfiles.omfiles import OmFileReader
from om_exporter.build import build_grid_from_domain
from om_exporter.converter.gasssian import GaussianToRegularConverter

# 1. 从 AWS Open Data 读取 OM 文件
fs = S3FileSystem(anon=True)
reader = OmFileReader.from_fsspec(
    fs, 
    "openmeteo/data_run/ecmwf_ifs/2026/01/17/1200Z/precipitation.om"
)
data = reader[:]  # shape: (n_points, n_times)

# 2. 构建网格（从预定义配置）
grid = build_grid_from_domain('EcmwfEcpdsDomain', 'ifs')

# 3. 创建转换器并构建目标网格
converter = GaussianToRegularConverter(grid.grid_type)
target = converter.build_target_grid(
    target_resolution=(0.1, 0.1),      # 0.1° 分辨率
    lat_range=(-90.0, 90.0),           # 全球
    lon_range=(-180.0, 180.0),
)

# 4. 插值转换
data_regular = converter.interpolate(data, target, method="nearest")
# shape: (ny, nx, n_times) = (1801, 3601, n_times)

# 5. 可视化
import matplotlib.pyplot as plt
plt.imshow(data_regular[:, :, 0], vmin=0.01, vmax=1.0)
plt.show()
```



## Data Sources & Attribution

- This project uses data from the following sources:
  - **Open-Meteo on AWS Open Data**  
  © Open-Meteo Licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**  
  https://github.com/open-meteo/open-data



## Grid Types

本项目支持三种气象网格类型：

### RegularGrid（规则经纬度网格）

标准的等间距经纬度网格：

```python
from om_exporter.grid import RegularGrid

grid = RegularGrid(
    nx=1440,        # 经度方向格点数
    ny=721,         # 纬度方向格点数
    lat_min=-90.0,  # 最小纬度
    lon_min=-180.0, # 最小经度
    dx=0.25,        # 经度间距（度）
    dy=0.25,        # 纬度间距（度）
)

# 获取网格信息
grid.count                              # 总点数
lats, lons = grid.get_lat_lon_arrays()  # 一维坐标
lats_2d, lons_2d = grid.get_lat_lon_2d() # 二维坐标
index = grid.find_point(lat=39.9, lon=116.4)  # 查找最近点
data_2d = grid.reshape_to_2d(data_1d)   # 重塑为 (ny, nx)
```

### ProjectionGrid（投影网格）

支持多种地图投影：
- **LambertConformalConicProjection**：兰伯特等角圆锥投影
- **RotatedLatLonProjection**：旋转经纬度投影
- **StereographicProjection**：球极平面投影
- **LambertAzimuthalEqualAreaProjection**：兰伯特等面积方位投影

```python
from om_exporter.grid import ProjectionGrid, LambertConformalConicProjection

grid = ProjectionGrid(
    nx=1799,
    ny=1059,
    projection=LambertConformalConicProjection(
        lambda0=-97.5, phi0=0.0, phi1=38.5, phi2=38.5, radius=6371229,
    ),
    latitude=(21.138, 47.8424),
    longitude=(-122.72, -60.918),
)
```

### GaussianGrid（高斯网格）

ECMWF 缩减高斯网格，支持 O（八面体）和 N（经典）系列：

| 类型 | 描述 | 总点数 |
|------|------|--------|
| O320 | 八面体缩减高斯网格 | ~421,120 |
| O1280 | 高分辨率八面体网格 | ~6,599,680 |
| N160 | 经典缩减高斯网格 | ~108,160 |
| N320 | 经典缩减高斯网格 | ~421,120 |

```python
from om_exporter.grid import GaussianGrid, GaussianGridType
from om_exporter.converter.gasssian import GaussianToRegularConverter

# 创建高斯网格
grid = GaussianGrid(grid_type=GaussianGridType.O1280)

# 获取网格点坐标
lats, lons = grid.get_lat_lon_arrays()

# 查找最近点
index = grid.find_point(lat=39.9, lon=116.4)  # 北京
```

### 高斯网格转换

将高斯网格数据转换为规则经纬度网格：

```python
from om_exporter.grid import GaussianGridType
from om_exporter.converter.gasssian import GaussianToRegularConverter, TargetGrid

converter = GaussianToRegularConverter(GaussianGridType.O1280)

# 构建目标网格（可复用）
target = converter.build_target_grid(
    target_resolution=(0.25, 0.25),
    lat_range=(15.0, 55.0),   # 中国区域
    lon_range=(70.0, 140.0),
)

# 插值转换
# 输入: (n_points,) 或 (n_points, n_times)
# 输出: (ny, nx) 或 (ny, nx, n_times)
data_regular = converter.interpolate(data, target, method="nearest")

# 访问目标网格信息
target.lat_1d, target.lon_1d   # 一维坐标
target.lats_2d, target.lons_2d # 二维坐标
target.shape                   # (ny, nx)
```

### 从配置构建网格

```python
from om_exporter.build import build_grid_from_domain
from om_exporter.conf.domain import DOMAIN_GRIDS

# 从预定义配置构建
grid = build_grid_from_domain(domain="CdsDomain", name="era5")
grid = build_grid_from_domain(domain="EcmwfEcpdsDomain", name="ifs")
grid = build_grid_from_domain(domain="EcmwfSeasDomain", name="seas5")

# 查看所有可用配置
print(DOMAIN_GRIDS.keys())
```



## Installation

```bash
uv add om-exporter
```

### Dependencies

```bash
# 读取 OM 文件
uv add omfiles

# 访问 AWS S3
uv add s3fs

# 高斯网格插值（可选）
uv add scipy

# 可视化（可选）
uv add matplotlib
```
