# 🛡️ AgentAudit-CLI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/零依賴-✓-brightgreen.svg" alt="零依賴">
  <img src="https://img.shields.io/badge/許可證-MIT-yellow.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/平台-跨平台-lightgrey.svg" alt="跨平台">
</p>

<p align="center">
  <b>🌐 多語言文檔</b> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="README.zh-TW.md">繁體中文</a> |
  <a href="README.md">English</a>
</p>

---

## 🎉 專案介紹

**AgentAudit-CLI** 是一款輕量級AI Agent行為合規審計引擎，專為幫助開發者檢測AI Agent程式碼中潛在的安全風險、隱私合規問題、倫理隱患和效能瓶頸而設計。

### 💡 核心價值

在AI Agent爆發式增長的今天，程式碼安全與合規變得至關重要。AgentAudit-CLI提供**開箱即用、零依賴**的解決方案，讓您能夠快速審計AI Agent程式碼，確保其符合安全最佳實踐和合規要求。

### ✨ 自研差異化亮點

- 🚀 **零依賴設計**：純Python標準庫實現，無需任何外部依賴
- 🎯 **多維度檢測**：覆蓋安全、隱私、倫理、效能、合規五大維度
- 📊 **多格式報告**：支援JSON/HTML/Markdown/Console多種輸出格式
- 🔧 **高度可擴展**：內建12+規則，支援自定義規則擴展
- ⚡ **輕量快速**：單檔案設計，即拿即用

---

## ✨ 核心特性

| 特性 | 描述 | 狀態 |
|------|------|------|
| 🔒 **安全檢測** | 硬編碼密鑰、SQL注入、不安全反序列化 | ✅ |
| 🔐 **隱私合規** | PII資訊收集、敏感資料記錄 | ✅ |
| ⚖️ **倫理審查** | 偏見性語言、自動化決策風險 | ✅ |
| 🚀 **效能分析** | 無限迴圈、資源洩漏 | ✅ |
| 📋 **合規檢查** | 許可證聲明、TODO標記 | ✅ |
| 📊 **視覺化報告** | 美觀的HTML報告，資料視覺化 | ✅ |

### 🎯 內建審計規則（12+）

<details>
<summary>點擊查看所有規則</summary>

| 規則ID | 名稱 | 類別 | 風險等級 |
|--------|------|------|----------|
| SEC-001 | 硬編碼密鑰檢測 | 安全 | 🔴 嚴重 |
| SEC-002 | 不安全反序列化 | 安全 | 🟠 高 |
| SEC-003 | SQL注入風險 | 安全 | 🔴 嚴重 |
| SEC-004 | 不安全HTTP請求 | 安全 | 🟠 高 |
| PRI-001 | PII資訊收集 | 隱私 | 🟡 中 |
| PRI-002 | 使用者資料記錄 | 隱私 | 🟡 中 |
| ETH-001 | 偏見性語言 | 倫理 | 🟡 中 |
| ETH-002 | 自動化決策 | 倫理 | 🟠 高 |
| PER-001 | 無限迴圈風險 | 效能 | 🟠 高 |
| PER-002 | 資源洩漏 | 效能 | 🟡 中 |
| COM-001 | 許可證聲明缺失 | 合規 | 🟢 低 |
| COM-002 | TODO/FIXME標記 | 合規 | 🔵 資訊 |

</details>

---

## 🚀 快速開始

### 📋 環境要求

- **Python**: 3.8 或更高版本
- **作業系統**: Windows / macOS / Linux
- **依賴項**: 無（零依賴設計）

### 📦 安裝

#### 方式一：直接下載（推薦）

```bash
# 克隆倉庫
git clone https://github.com/gitstq/AgentAudit-CLI.git
cd AgentAudit-CLI

# 直接執行
python agentaudit.py --help
```

#### 方式二：透過pip安裝

```bash
pip install git+https://github.com/gitstq/AgentAudit-CLI.git
```

#### 方式三：setup安裝

```bash
git clone https://github.com/gitstq/AgentAudit-CLI.git
cd AgentAudit-CLI
pip install -e .

# 全域使用命令
agentaudit --help
```

### 🎯 基本使用

```bash
# 掃描當前目錄
python agentaudit.py scan .

# 掃描指定目錄
python agentaudit.py scan ./src

# 生成HTML報告
python agentaudit.py scan ./src --format html --output report.html

# 只掃描安全和隱私類別
python agentaudit.py scan ./src --category security,privacy

# 只報告高風險及以上問題
python agentaudit.py scan ./src --risk critical,high
```

---

## 📖 詳細使用指南

### 🔍 掃描命令

```bash
# 基礎掃描
agentaudit scan <路徑> [選項]

# 選項:
#   -f, --format      輸出格式: json/html/markdown/console
#   -o, --output      輸出檔案路徑
#   -c, --category    過濾類別: security,privacy,ethics,performance,compliance
#   -r, --risk        過濾風險等級: critical,high,medium,low,info
#   -e, --extensions  檔案副檔名: .py,.js,.ts
```

### 📋 查看規則

```bash
# 列出所有規則
agentaudit rules

# 按類別過濾
agentaudit rules --category security

# 按風險等級過濾
agentaudit rules --risk critical,high
```

### 📊 報告範例

#### 控制台輸出

```bash
$ agentaudit scan ./example

🛡️ AgentAudit 開始掃描...
   目標: /path/to/example
   規則: 12 條已啟用

📊 掃描結果
   檔案數: 5
   程式碼行: 1,234
   發現項: 3

🚨 審計發現:

🔴 [嚴重] 硬編碼密鑰檢測
   📁 example/config.py:15
   📝 檢測到 硬編碼密鑰檢測: api_key = "sk-1234567890abcdef...
   💡 使用環境變數或密鑰管理服務儲存敏感資訊

🟠 [高] SQL注入風險
   📁 example/database.py:42
   📝 檢測到 SQL注入風險: cursor.execute(f"SELECT * FROM...
   💡 使用參數化查詢或ORM框架
```

#### HTML報告預覽

生成的HTML報告包含：
- 📊 視覺化統計卡片
- 🎨 顏色編碼的風險等級
- 📁 詳細問題定位
- 💡 修復建議

---

## 💡 設計理念與迭代規劃

### 🎯 設計理念

1. **零依賴**：僅使用Python標準庫，確保最大相容性
2. **輕量快速**：單檔案設計，即拿即用
3. **可擴展性**：模組化規則引擎，方便添加自定義規則
4. **開發者優先**：清晰的命令列介面，多種輸出格式

### 📈 迭代計劃

- [ ] **v1.1.0**: 添加SARIF格式輸出，CI/CD整合
- [ ] **v1.2.0**: 支援更多程式語言（Java、Go、Rust）
- [ ] **v1.3.0**: 添加AI驅動的智慧規則推薦
- [ ] **v2.0.0**: Web UI儀表板，團隊協作功能

### 🤝 社群貢獻

歡迎社群貢獻！您可以：
- 🐛 提交Bug報告
- 💡 建議新功能
- 🔧 貢獻程式碼
- 🌍 改進文件

查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解詳情。

---

## 📦 打包與部署指南

### 📋 本地開發

```bash
# 克隆倉庫
git clone https://github.com/gitstq/AgentAudit-CLI.git
cd AgentAudit-CLI

# 建立虛擬環境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 開發模式安裝
pip install -e .
```

### 🔨 建構分發包

```bash
# 安裝建構工具
pip install build twine

# 建構包
python -m build

# 上傳到PyPI（需要權限）
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
# 建構映像檔
docker build -t agentaudit-cli .

# 執行容器
docker run -v $(pwd):/code agentaudit-cli scan /code
```

---

## 🤝 貢獻指南

### 📝 PR提交規範

1. Fork 本倉庫
2. 建立特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: 添加 amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 建立 Pull Request

### 🐛 Issue回饋規則

- 使用Issue模板
- 提供詳細的復現步驟
- 包含環境資訊
- 附上相關日誌或截圖

---

## 📄 開源協議

本專案採用 [MIT License](LICENSE) 開源協議。

---

## 🌟 Star歷史

如果這個專案對您有幫助，請給我們一個 ⭐️！

[![Star History Chart](https://api.star-history.com/svg?repos=gitstq/AgentAudit-CLI&type=Date)](https://star-history.com/#gitstq/AgentAudit-CLI&Date)

---

<p align="center">
  用 ❤️ 由 <a href="https://github.com/gitstq">gitstq</a> 製作
</p>

<p align="center">
  <a href="https://github.com/gitstq/AgentAudit-CLI">GitHub</a> •
  <a href="https://github.com/gitstq/AgentAudit-CLI/issues">Issues</a> •
  <a href="https://github.com/gitstq/AgentAudit-CLI/discussions">Discussions</a>
</p>
