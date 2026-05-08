#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动更新 README 文档中的特征统计
运行方式：python scripts/update-readme.py
"""
import json
import os
def update_readme():
    """自动更新 README.md 中的特征统计"""
    # 读取特征库
    feature_file = "monitoring_features.json"
    with open(feature_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 统计各分类特征数量
    stats = {}
    for key in data:
        if key.endswith("_features") and isinstance(data[key], list):
            category_name = key.replace("_", " ").title()
            stats[category_name] = len(data[key])
    
    total_features = sum(stats.values())
    version = data.get("version", "1.0.0")
    description = data.get("description", "Feature library for AI-powered monitoring backend")
    
    # 生成新的 README
    readme_template = f"""# 监测后台 AI 特征库
{description}
## 📊 特征统计
- **版本**: {version}
- **总特征数**: **{total_features}**
"""
    for cat, count in stats.items():
        readme_template += f"- **{cat}**: {count} 个\n"
    readme_template += """
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
"""
    
    # 保存更新后的 README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_template)
    
    print(f"✅ README.md 更新完成！")
    print(f"📊 总特征数: {total_features}")
    for cat, count in stats.items():
        print(f"   {cat}: {count}")
    
    return True
if __name__ == "__main__":
    success = update_readme()
    exit(0 if success else 1)