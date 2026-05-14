# 🛡️ AgentAudit-CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/零依赖-✓-brightgreen.svg" alt="零依赖">
  <img src="https://img.shields.io/badge/许可证-MIT-yellow.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/平台-跨平台-lightgrey.svg" alt="跨平台">
</p>

<p align="center">
  <b>🌐 多语言文档</b> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.md">English</a>
</p>

---

## 🎉 项目介绍

**AgentAudit-CLI** 是一款轻量级AI Agent行为合规审计引擎，专为帮助开发者检测AI Agent代码中潜在的安全风险、隐私合规问题、伦理隐患和性能瓶颈而设计。

### 💡 核心价值

在AI Agent爆发式增长的今天，代码安全与合规变得至关重要。AgentAudit-CLI提供**开箱即用、零依赖**的解决方案，让您能够快速审计AI Agent代码，确保其符合安全最佳实践和合规要求。

### ✨ 自研差异化亮点

- 🚀 **零依赖设计**：纯Python标准库实现，无需任何外部依赖
- 🎯 **多维度检测**：覆盖安全、隐私、伦理、性能、合规五大维度
- 📊 **多格式报告**：支持JSON/HTML/Markdown/Console多种输出格式
- 🔧 **高度可扩展**：内置12+规则，支持自定义规则扩展
- ⚡ **轻量快速**：单文件设计，即拿即用

---

## ✨ 核心特性

| 特性 | 描述 | 状态 |
|------|------|------|
| 🔒 **安全检测** | 硬编码密钥、SQL注入、不安全反序列化 | ✅ |
| 🔐 **隐私合规** | PII信息收集、敏感数据记录 | ✅ |
| ⚖️ **伦理审查** | 偏见性语言、自动化决策风险 | ✅ |
| 🚀 **性能分析** | 无限循环、资源泄漏 | ✅ |
| 📋 **合规检查** | 许可证声明、TODO标记 | ✅ |
| 📊 **可视化报告** | 美观的HTML报告，数据可视化 | ✅ |

### 🎯 内置审计规则（12+）

<details>
<summary>点击查看所有规则</summary>

| 规则ID | 名称 | 类别 | 风险等级 |
|--------|------|------|----------|
| SEC-001 | 硬编码密钥检测 | 安全 | 🔴 严重 |
| SEC-002 | 不安全反序列化 | 安全 | 🟠 高 |
| SEC-003 | SQL注入风险 | 安全 | 🔴 严重 |
| SEC-004 | 不安全HTTP请求 | 安全 | 🟠 高 |
| PRI-001 | PII信息收集 | 隐私 | 🟡 中 |
| PRI-002 | 用户数据记录 | 隐私 | 🟡 中 |
| ETH-001 | 偏见性语言 | 伦理 | 🟡 中 |
| ETH-002 | 自动化决策 | 伦理 | 🟠 高 |
| PER-001 | 无限循环风险 | 性能 | 🟠 高 |
| PER-002 | 资源泄漏 | 性能 | 🟡 中 |
| COM-001 | 许可证声明缺失 | 合规 | 🟢 低 |
| COM-002 | TODO/FIXME标记 | 合规 | 🔵 信息 |

</details>

---

## 🚀 快速开始

### 📋 环境要求

- **Python**: 3.8 或更高版本
- **操作系统**: Windows / macOS / Linux
- **依赖项**: 无（零依赖设计）

### 📦 安装

#### 方式一：直接下载（推荐）

```bash
# 克隆仓库
git clone https://github.com/gitstq/AgentAudit-CLI.git
cd AgentAudit-CLI

# 直接运行
python agentaudit.py --help
```

#### 方式二：通过pip安装

```bash
pip install git+https://github.com/gitstq/AgentAudit-CLI.git
```

#### 方式三：setup安装

```bash
git clone https://github.com/gitstq/AgentAudit-CLI.git
cd AgentAudit-CLI
pip install -e .

# 全局使用命令
agentaudit --help
```

### 🎯 基本使用

```bash
# 扫描当前目录
python agentaudit.py scan .

# 扫描指定目录
python agentaudit.py scan ./src

# 生成HTML报告
python agentaudit.py scan ./src --format html --output report.html

# 只扫描安全和隐私类别
python agentaudit.py scan ./src --category security,privacy

# 只报告高风险及以上问题
python agentaudit.py scan ./src --risk critical,high
```

---

## 📖 详细使用指南

### 🔍 扫描命令

```bash
# 基础扫描
agentaudit scan <路径> [选项]

# 选项:
#   -f, --format      输出格式: json/html/markdown/console
#   -o, --output      输出文件路径
#   -c, --category    过滤类别: security,privacy,ethics,performance,compliance
#   -r, --risk        过滤风险等级: critical,high,medium,low,info
#   -e, --extensions  文件扩展名: .py,.js,.ts
```

### 📋 查看规则

```bash
# 列出所有规则
agentaudit rules

# 按类别过滤
agentaudit rules --category security

# 按风险等级过滤
agentaudit rules --risk critical,high
```

### 📊 报告示例

#### 控制台输出

```bash
$ agentaudit scan ./example

🛡️ AgentAudit 开始扫描...
   目标: /path/to/example
   规则: 12 条已启用

📊 扫描结果
   文件数: 5
   代码行: 1,234
   发现项: 3

🚨 审计发现:

🔴 [严重] 硬编码密钥检测
   📁 example/config.py:15
   📝 检测到 硬编码密钥检测: api_key = "sk-1234567890abcdef...
   💡 使用环境变量或密钥管理服务存储敏感信息

🟠 [高] SQL注入风险
   📁 example/database.py:42
   📝 检测到 SQL注入风险: cursor.execute(f"SELECT * FROM...
   💡 使用参数化查询或ORM框架
```

#### HTML报告预览

生成的HTML报告包含：
- 📊 可视化统计卡片
- 🎨 颜色编码的风险等级
- 📁 详细问题定位
- 💡 修复建议

---

## 💡 设计思路与迭代规划

### 🎯 设计理念

1. **零依赖**：仅使用Python标准库，确保最大兼容性
2. **轻量快速**：单文件设计，即拿即用
3. **可扩展性**：模块化规则引擎，方便添加自定义规则
4. **开发者优先**：清晰的命令行界面，多种输出格式

### 📈 迭代计划

- [ ] **v1.1.0**: 添加SARIF格式输出，CI/CD集成
- [ ] **v1.2.0**: 支持更多编程语言（Java、Go、Rust）
- [ ] **v1.3.0**: 添加AI驱动的智能规则推荐
- [ ] **v2.0.0**: Web UI仪表板，团队协作功能

### 🤝 社区贡献

欢迎社区贡献！您可以：
- 🐛 提交Bug报告
- 💡 建议新功能
- 🔧 贡献代码
- 🌍 改进文档

查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

---

## 📦 打包与部署指南

### 📋 本地开发

```bash
# 克隆仓库
git clone https://github.com/gitstq/AgentAudit-CLI.git
cd AgentAudit-CLI

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 开发模式安装
pip install -e .
```

### 🔨 构建分发包

```bash
# 安装构建工具
pip install build twine

# 构建包
python -m build

# 上传到PyPI（需要权限）
python -m twine upload dist/*
```

### 🐳 Docker部署

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY agentaudit.py .

ENTRYPOINT ["python", "agentaudit.py"]
CMD ["--help"]
```

```bash
# 构建镜像
docker build -t agentaudit-cli .

# 运行容器
docker run -v $(pwd):/code agentaudit-cli scan /code
```

---

## 🤝 贡献指南

### 📝 PR提交规范

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: 添加 amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

### 🐛 Issue反馈规则

- 使用Issue模板
- 提供详细的复现步骤
- 包含环境信息
- 附上相关日志或截图

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

---

## 🌟 Star历史

如果这个项目对您有帮助，请给我们一个 ⭐️！

[![Star History Chart](https://api.star-history.com/svg?repos=gitstq/AgentAudit-CLI&type=Date)](https://star-history.com/#gitstq/AgentAudit-CLI&Date)

---

<p align="center">
  用 ❤️ 由 <a href="https://github.com/gitstq">gitstq</a> 制作
</p>

<p align="center">
  <a href="https://github.com/gitstq/AgentAudit-CLI">GitHub</a> •
  <a href="https://github.com/gitstq/AgentAudit-CLI/issues">Issues</a> •
  <a href="https://github.com/gitstq/AgentAudit-CLI/discussions">Discussions</a>
</p>
