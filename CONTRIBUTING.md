# 🤝 Contributing to AgentAudit-CLI

感谢您对 AgentAudit-CLI 的兴趣！我们欢迎所有形式的贡献。

## 🚀 如何贡献

### 报告问题

如果您发现了 bug 或有功能建议，请通过 GitHub Issues 提交：

1. 检查是否已有类似问题
2. 使用问题模板创建新 Issue
3. 提供详细的复现步骤和环境信息

### 提交代码

1. **Fork 仓库**
   ```bash
   git clone https://github.com/gitstq/agentaudit-cli.git
   cd agentaudit-cli
   ```

2. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **提交更改**
   ```bash
   git add .
   git commit -m "feat: 添加新功能"
   ```

4. **推送并创建 PR**
   ```bash
   git push origin feature/your-feature-name
   ```

### 代码规范

- 遵循 PEP 8 规范
- 添加适当的注释和文档字符串
- 确保代码通过所有测试
- 保持零依赖设计原则

### 提交信息规范

我们使用 Conventional Commits 规范：

- `feat:` 新功能
- `fix:` 修复问题
- `docs:` 文档更新
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具相关

## 📋 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/gitstq/agentaudit-cli.git
cd agentaudit-cli

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 安装开发依赖
pip install -e .
```

## 🧪 测试

```bash
# 运行测试
python -m pytest tests/

# 检查代码风格
black agentaudit.py
flake8 agentaudit.py
```

## 📄 许可证

通过提交 PR，您同意您的贡献将在 MIT 许可证下发布。

## 💬 联系我们

如有任何问题，欢迎通过 GitHub Discussions 与我们交流！
