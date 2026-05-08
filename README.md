# 监测后台 AI 特征库
Feature library for AI-powered monitoring backend
## 📊 特征统计
- **版本**: 1.0.0
- **总特征数**: **15**
- **System Features**: 6 个
- **Application Features**: 4 个
- **Business Features**: 2 个
- **Anomaly Detection Features**: 3 个

## 特征分类
- **系统指标**: CPU、内存、磁盘、网络、负载等基础系统资源监控
- **应用指标**: 请求数、响应时间、错误率等应用层监控
- **业务指标**: 活跃用户、交易数等业务指标
- **AI特征**: 异常检测相关计算特征
## 使用方式
直接导入 JSON 文件即可获取完整特征定义用于模型训练或实时监测。
```python
import json
with open('monitoring_features.json', 'r', encoding='utf-8') as f:
    features = json.load(f)
# 使用特征定义
for feature in features['system_features']:
    print(f"Feature: {feature['name']} ({feature['unit']})")
```
## 自动更新
本项目使用 GitHub Actions 自动验证和更新文档：
- ✅ 每次推送到 main 分支自动触发
- ✅ 验证 JSON 格式正确性
- ✅ 自动更新特征统计
- ✅ 重新生成 README 文档
本地手动更新文档：
```bash
python scripts/update-readme.py
```
## License
MIT
