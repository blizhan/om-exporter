# Cloud Agent Development Guide

本文档专为云端 AI Agent（如 Codex）设计，指导在每次全新环境中进行开发、测试。

## Environment Setup (每次必须执行)

### 1. 安装依赖

```bash
# 安装 uv（如果尚未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 同步项目依赖
uv sync
```

### 2. 验证环境

```bash
# 检查 Python 版本 (需要 3.13+)
uv run python --version

# 验证核心模块可导入
uv run python -c "
from om_exporter.grid import RegularGrid, GaussianGrid, GaussianGridType
from om_exporter.build import build_grid_from_domain
from om_exporter.converter.gasssian import GaussianToRegularConverter, TargetGrid
print('✅ All imports successful')
"

# 验证 CLI
uv run om-export --help
```

### 3. 网络依赖检查（可选）

如果需要访问 AWS S3 数据：

```bash
uv run python -c "
from s3fs import S3FileSystem
fs = S3FileSystem(anon=True)
files = fs.ls('openmeteo/data_run/ecmwf_ifs/', detail=False)[:3]
print('✅ S3 access OK, sample files:', files)
"
```

## Development Workflow

### 代码修改后的验证流程

```bash
# 1. 格式化代码
make fmt

# 2. 检查 lint
make lint

# 3. 运行测试
uv run pytest -v

# 4. 手动验证（如需要）
uv run python -c "
# 测试你修改的代码
"
```

### 新增模块的检查清单

- [ ] 添加到 `__all__` 导出列表
- [ ] 使用相对导入 (`from .module import ...`)
- [ ] 添加类型注解
- [ ] 编写 docstring
- [ ] 添加测试用例到 `test/`

## Testing Guide

### 单元测试

```bash
# 运行所有测试
uv run pytest

# 运行特定测试文件
uv run pytest test/test_grid.py -v

# 运行匹配的测试
uv run pytest -k "gaussian" -v
```

### 功能测试模板

创建测试时使用以下模板：

```python
# test/test_example.py
import numpy as np
import pytest
from om_exporter.grid import RegularGrid, GaussianGrid, GaussianGridType
from om_exporter.converter.gasssian import GaussianToRegularConverter


class TestRegularGrid:
    def test_count(self):
        grid = RegularGrid(nx=10, ny=20, lat_min=0, lon_min=0, dx=1, dy=1)
        assert grid.count == 200

    def test_find_point(self):
        grid = RegularGrid(nx=360, ny=180, lat_min=-90, lon_min=-180, dx=1, dy=1)
        idx = grid.find_point(lat=0, lon=0)
        assert idx == 90 * 360 + 180


class TestGaussianConverter:
    @pytest.fixture
    def converter(self):
        return GaussianToRegularConverter(GaussianGridType.O320)

    def test_build_target_grid(self, converter):
        target = converter.build_target_grid(
            target_resolution=(1.0, 1.0),
            lat_range=(-10, 10),
            lon_range=(-10, 10),
        )
        assert target.shape == (21, 21)

    def test_interpolate_1d(self, converter):
        target = converter.build_target_grid(
            target_resolution=(5.0, 5.0),
            lat_range=(-10, 10),
            lon_range=(-10, 10),
        )
        # 模拟数据
        data = np.random.rand(converter.grid_type.count)
        result = converter.interpolate(data, target, method="nearest")
        assert result.shape == target.shape

    def test_interpolate_2d(self, converter):
        target = converter.build_target_grid(
            target_resolution=(5.0, 5.0),
            lat_range=(-10, 10),
            lon_range=(-10, 10),
        )
        # 模拟多时间步数据
        n_times = 5
        data = np.random.rand(converter.grid_type.count, n_times)
        result = converter.interpolate(data, target, method="nearest")
        assert result.shape == (*target.shape, n_times)
```

### 集成测试（需要网络）

```python
# test/test_integration.py
import pytest
from s3fs import S3FileSystem
from omfiles.omfiles import OmFileReader
from om_exporter.build import build_grid_from_domain
from om_exporter.converter.gasssian import GaussianToRegularConverter


@pytest.mark.network
class TestS3Integration:
    def test_read_and_convert(self):
        fs = S3FileSystem(anon=True)
        # 使用一个已知存在的文件
        reader = OmFileReader.from_fsspec(
            fs, 
            "openmeteo/data/ecmwf_ifs/precipitation/chunk_1640.om"
        )
        data = reader[:]
        
        grid = build_grid_from_domain('EcmwfEcpdsDomain', 'ifs')
        converter = GaussianToRegularConverter(grid.grid_type)
        target = converter.build_target_grid(
            target_resolution=(1.0, 1.0),
            lat_range=(30, 40),
            lon_range=(110, 120),
        )
        result = converter.interpolate(data, target, method="nearest")
        
        assert result.shape[0] == 11  # lat points
        assert result.shape[1] == 11  # lon points
```

运行网络测试：

```bash
uv run pytest -m network -v
```

## Architecture Guidelines

### 新增网格类型

1. 在 `grid/__init__.py` 添加 dataclass
2. 更新 `Grid` Union 类型
3. 在 `build.py` 的 `build_grid()` 添加构建逻辑
4. 在 `conf/domain.py` 添加配置（如需要）

### 新增转换器

1. 在 `converter/` 创建新文件
2. 遵循 `GaussianToRegularConverter` 的模式：
   - 缓存源坐标和 KDTree
   - 提供 `build_target_grid()` 构建目标网格
   - 提供 `interpolate()` 执行转换
3. 支持 1D `(n_points,)` 和 2D `(n_points, n_times)` 输入

### 数据布局约定

```
输入数据: (n_points, n_times)  # 第一维是空间，第二维是时间
输出数据: (ny, nx, n_times)    # 规则网格 + 时间
```

## Quick Reference

### 常用导入

```python
# Grid 类型
from om_exporter.grid import (
    RegularGrid, 
    ProjectionGrid, 
    GaussianGrid, 
    GaussianGridType,
)

# 构建函数
from om_exporter.build import build_grid_from_domain

# 转换器
from om_exporter.converter.gasssian import GaussianToRegularConverter, TargetGrid

# 配置
from om_exporter.conf.domain import DOMAIN_GRIDS
```

### 可用的 Domain 配置

```python
# 查看所有 domain
print(list(DOMAIN_GRIDS.keys()))
# ['CdsDomain', 'EcmwfDomain', 'EcmwfEcpdsDomain', 'EcmwfSeasDomain', ...]

# 查看 domain 下的网格
print(list(DOMAIN_GRIDS['EcmwfEcpdsDomain'].keys()))
# ['ifs', 'wam']
```

## Troubleshooting

| 问题 | 解决方案 |
|------|----------|
| `ModuleNotFoundError` | 运行 `uv sync` 安装依赖 |
| `scipy` 导入错误 | 确认 `uv sync` 成功完成 |
| S3 访问失败 | 检查网络连接，确认 `anon=True` |
| pytest 找不到测试 | 确认测试文件名以 `test_` 开头 |
