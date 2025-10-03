# 天气预报系统

这是一个使用 Python 编写的简易天气预报系统，基于几座城市的历史气象数据生成未来天气预测。

## 功能

- 提供北京、上海、广州的示例历史气象数据。
- 根据历史温度、湿度变化趋势生成未来若干天的预报。
- 通过命令行查询指定城市的未来天气。

## 安装与运行

1. 创建虚拟环境并安装依赖：

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows 请使用 .venv\\Scripts\\activate
   pip install -r requirements.txt  # 若已经安装 pytest 可跳过
   ```

2. 运行命令行工具：

   ```bash
   python -m weather_app.cli 北京 --days 3
   ```

   示例输出：

   ```
   日期             温度(°C)      湿度(%)        天气
   -----------------------------------------------
   2024-04-08          24.2         31.5        多云
   2024-04-09          24.6         31.5        多云
   2024-04-10          25.1         31.6        多云
   ```

## 测试

项目使用 `pytest` 进行单元测试：

```bash
pytest
```
