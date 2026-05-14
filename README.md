# 🛡️ AgentAudit-CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Zero%20Dependencies-✓-brightgreen.svg" alt="Zero Dependencies">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/Platform-Cross--Platform-lightgrey.svg" alt="Cross Platform">
</p>

<p align="center">
  <b>🌐 多语言文档</b> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.md">English</a>
</p>

---

## 🎉 Project Introduction

**AgentAudit-CLI** is a lightweight AI Agent behavior compliance audit engine designed to help developers detect potential security risks, privacy compliance issues, ethical concerns, and performance bottlenecks in AI Agent code.

### 💡 Core Value

In the era of explosive AI Agent growth, code security and compliance have become crucial. AgentAudit-CLI provides an **out-of-the-box, zero-dependency** solution that allows you to quickly audit your AI Agent code to ensure it meets security best practices and compliance requirements.

### ✨ Self-Developed Differentiation Highlights

- 🚀 **Zero Dependencies**: Pure Python standard library implementation, no external dependencies
- 🎯 **Multi-Dimensional Detection**: Covers security, privacy, ethics, performance, and compliance
- 📊 **Multiple Report Formats**: Supports JSON/HTML/Markdown/Console output
- 🔧 **Highly Extensible**: Built-in 12+ rules, supports custom rule extensions
- ⚡ **Lightweight & Fast**: Single-file design, ready to use out of the box

---

## ✨ Core Features

| Feature | Description | Status |
|---------|-------------|--------|
| 🔒 **Security Detection** | Hardcoded keys, SQL injection, unsafe deserialization | ✅ |
| 🔐 **Privacy Compliance** | PII collection, sensitive data logging | ✅ |
| ⚖️ **Ethics Review** | Bias language, automated decision-making risks | ✅ |
| 🚀 **Performance Analysis** | Infinite loops, resource leaks | ✅ |
| 📋 **Compliance Check** | License declarations, TODO tracking | ✅ |
| 📊 **Visual Reports** | Beautiful HTML reports with data visualization | ✅ |

### 🎯 Built-in Audit Rules (12+)

<details>
<summary>Click to view all rules</summary>

| Rule ID | Name | Category | Risk Level |
|---------|------|----------|------------|
| SEC-001 | Hardcoded Key Detection | Security | 🔴 Critical |
| SEC-002 | Unsafe Deserialization | Security | 🟠 High |
| SEC-003 | SQL Injection Risk | Security | 🔴 Critical |
| SEC-004 | Insecure HTTP Requests | Security | 🟠 High |
| PRI-001 | PII Collection | Privacy | 🟡 Medium |
| PRI-002 | User Data Logging | Privacy | 🟡 Medium |
| ETH-001 | Bias Language | Ethics | 🟡 Medium |
| ETH-002 | Automated Decision-Making | Ethics | 🟠 High |
| PER-001 | Infinite Loop Risk | Performance | 🟠 High |
| PER-002 | Resource Leaks | Performance | 🟡 Medium |
| COM-001 | Missing License | Compliance | 🟢 Low |
| COM-002 | TODO/FIXME Tags | Compliance | 🔵 Info |

</details>

---

## 🚀 Quick Start

### 📋 Environment Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows / macOS / Linux
- **Dependencies**: None (Zero dependency design)

### 📦 Installation

#### Method 1: Direct Download (Recommended)

```bash
# Clone repository
git clone https://github.com/gitstq/AgentAudit-CLI.git
cd AgentAudit-CLI

# Run directly
python agentaudit.py --help
```

#### Method 2: Install via pip

```bash
pip install git+https://github.com/gitstq/AgentAudit-CLI.git
```

#### Method 3: Setup Install

```bash
git clone https://github.com/gitstq/AgentAudit-CLI.git
cd AgentAudit-CLI
pip install -e .

# Use command anywhere
agentaudit --help
```

### 🎯 Basic Usage

```bash
# Scan current directory
python agentaudit.py scan .

# Scan specific directory
python agentaudit.py scan ./src

# Generate HTML report
python agentaudit.py scan ./src --format html --output report.html

# Scan only security and privacy categories
python agentaudit.py scan ./src --category security,privacy

# Only report high-risk and above issues
python agentaudit.py scan ./src --risk critical,high
```

---

## 📖 Detailed Usage Guide

### 🔍 Scan Commands

```bash
# Basic scan
agentaudit scan <path> [options]

# Options:
#   -f, --format      Output format: json/html/markdown/console
#   -o, --output      Output file path
#   -c, --category    Filter categories: security,privacy,ethics,performance,compliance
#   -r, --risk        Filter risk levels: critical,high,medium,low,info
#   -e, --extensions  File extensions: .py,.js,.ts
```

### 📋 View Rules

```bash
# List all rules
agentaudit rules

# Filter by category
agentaudit rules --category security

# Filter by risk level
agentaudit rules --risk critical,high
```

### 📊 Report Examples

#### Console Output

```bash
$ agentaudit scan ./example

🛡️ AgentAudit Starting Scan...
   Target: /path/to/example
   Rules: 12 enabled

📊 Scan Results
   Files: 5
   Lines: 1,234
   Issues: 3

🚨 Audit Findings:

🔴 [CRITICAL] Hardcoded Key Detection
   📁 example/config.py:15
   📝 Detected Hardcoded Key Detection: api_key = "sk-1234567890abcdef...
   💡 Use environment variables or a secrets management service

🟠 [HIGH] SQL Injection Risk
   📁 example/database.py:42
   📝 Detected SQL Injection Risk: cursor.execute(f"SELECT * FROM...
   💡 Use parameterized queries or ORM frameworks
```

#### HTML Report Preview

The generated HTML report includes:
- 📊 Visual statistics cards
- 🎨 Color-coded risk levels
- 📁 Detailed issue locations
- 💡 Fix suggestions

---

## 💡 Design Philosophy & Iteration Plan

### 🎯 Design Philosophy

1. **Zero Dependencies**: Use only Python standard library to ensure maximum compatibility
2. **Lightweight & Fast**: Single-file design, ready to use out of the box
3. **Extensibility**: Modular rule engine for easy custom rule addition
4. **Developer-First**: Clear command-line interface, multiple output formats

### 📈 Iteration Plan

- [ ] **v1.1.0**: Add SARIF format output, CI/CD integration
- [ ] **v1.2.0**: Support more programming languages (Java, Go, Rust)
- [ ] **v1.3.0**: Add AI-powered intelligent rule recommendations
- [ ] **v2.0.0**: Web UI dashboard, team collaboration features

### 🤝 Community Contribution

We welcome community contributions! You can:
- 🐛 Submit bug reports
- 💡 Suggest new features
- 🔧 Contribute code
- 🌍 Improve documentation

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📦 Packaging & Deployment Guide

### 📋 Local Development

```bash
# Clone repository
git clone https://github.com/gitstq/AgentAudit-CLI.git
cd AgentAudit-CLI

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# Install in development mode
pip install -e .
```

### 🔨 Build Distribution Package

```bash
# Install build tools
pip install build twine

# Build package
python -m build

# Upload to PyPI (requires permissions)
python -m twine upload dist/*
```

### 🐳 Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY agentaudit.py .

ENTRYPOINT ["python", "agentaudit.py"]
CMD ["--help"]
```

```bash
# Build image
docker build -t agentaudit-cli .

# Run container
docker run -v $(pwd):/code agentaudit-cli scan /code
```

---

## 🤝 Contribution Guide

### 📝 PR Submission Standards

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'feat: Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

### 🐛 Issue Feedback Rules

- Use issue templates
- Provide detailed reproduction steps
- Include environment information
- Attach relevant logs or screenshots

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🌟 Star History

If you find this project helpful, please give us a ⭐️!

[![Star History Chart](https://api.star-history.com/svg?repos=gitstq/AgentAudit-CLI&type=Date)](https://star-history.com/#gitstq/AgentAudit-CLI&Date)

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/gitstq">gitstq</a>
</p>

<p align="center">
  <a href="https://github.com/gitstq/AgentAudit-CLI">GitHub</a> •
  <a href="https://github.com/gitstq/AgentAudit-CLI/issues">Issues</a> •
  <a href="https://github.com/gitstq/AgentAudit-CLI/discussions">Discussions</a>
</p>
