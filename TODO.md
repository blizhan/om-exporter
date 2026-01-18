# TODO

## 1. 计算指定经纬度范围/点的 range_list

为 OmFileReader 提供索引范围计算功能：

```python
# 期望 API
range_list = grid.get_range_list(
    lat_range=(30, 40),   # 纬度范围
    lon_range=(110, 120), # 经度范围
)
# 或单点
index = grid.find_point(lat=39.9, lon=116.4)

# 用于 OmFileReader 的切片读取
data = reader[range_list]  # 只读取指定区域的数据
```

## 2. to_xarray / to_png 导出功能

添加数据导出模块：

```python
# 期望 API
# 转换为 xarray.DataArray
da = converter.to_xarray(
    data, 
    target,
    dims=["lat", "lon", "time"],
    attrs={"units": "mm", "long_name": "Precipitation"},
)

# 导出为 PNG 图片
converter.to_png(
    data[:, :, 0],  # 单时间步
    target,
    output_path="output.png",
    cmap="viridis",
    vmin=0, vmax=10,
)
```
