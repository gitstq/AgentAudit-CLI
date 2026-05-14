#!/usr/bin/env python3
"""
AgentAudit-CLI 🛡️
轻量级AI Agent行为合规审计引擎
Lightweight AI Agent Behavior Compliance Audit Engine

Zero dependencies, pure Python implementation
"""

import sys
import json
import re
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import argparse


class RiskLevel(Enum):
    """风险等级"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class RuleCategory(Enum):
    """规则类别"""
    SECURITY = "security"
    PRIVACY = "privacy"
    ETHICS = "ethics"
    PERFORMANCE = "performance"
    COMPLIANCE = "compliance"


@dataclass
class AuditRule:
    """审计规则"""
    id: str
    name: str
    description: str
    category: RuleCategory
    risk_level: RiskLevel
    pattern: str
    suggestion: str
    enabled: bool = True


@dataclass
class AuditFinding:
    """审计发现"""
    rule_id: str
    rule_name: str
    category: str
    risk_level: str
    message: str
    location: str
    line_number: int
    suggestion: str
    timestamp: str


@dataclass
class AuditReport:
    """审计报告"""
    target: str
    scan_time: str
    total_files: int
    total_lines: int
    findings: List[AuditFinding]
    summary: Dict[str, Any]


class RuleEngine:
    """规则引擎"""

    # 内置规则库
    DEFAULT_RULES = [
        # 安全类规则
        AuditRule(
            id="SEC-001",
            name="硬编码密钥检测",
            description="检测代码中硬编码的API密钥、密码等敏感信息",
            category=RuleCategory.SECURITY,
            risk_level=RiskLevel.CRITICAL,
            pattern=r'(?i)(api[_-]?key|password|secret|token)\s*[=:]\s*["\'][a-zA-Z0-9_\-]{16,}["\']',
            suggestion="使用环境变量或密钥管理服务存储敏感信息"
        ),
        AuditRule(
            id="SEC-002",
            name="不安全的反序列化",
            description="检测潜在的不安全反序列化操作",
            category=RuleCategory.SECURITY,
            risk_level=RiskLevel.HIGH,
            pattern=r'(?i)(pickle\.loads|yaml\.load\(|eval\(|exec\()',
            suggestion="使用安全的替代方案，如json.loads或yaml.safe_load"
        ),
        AuditRule(
            id="SEC-003",
            name="SQL注入风险",
            description="检测潜在的SQL注入漏洞",
            category=RuleCategory.SECURITY,
            risk_level=RiskLevel.CRITICAL,
            pattern=r'(?i)(execute\s*\(\s*["\'].*%s|f["\'].*SELECT|f["\'].*INSERT|f["\'].*UPDATE|f["\'].*DELETE)',
            suggestion="使用参数化查询或ORM框架"
        ),
        AuditRule(
            id="SEC-004",
            name="不安全的HTTP请求",
            description="检测禁用SSL验证的HTTP请求",
            category=RuleCategory.SECURITY,
            risk_level=RiskLevel.HIGH,
            pattern=r'(?i)(verify\s*=\s*False|ssl_verify\s*=\s*False)',
            suggestion="始终启用SSL证书验证"
        ),

        # 隐私类规则
        AuditRule(
            id="PRI-001",
            name="PII信息收集",
            description="检测可能收集个人身份信息(PII)的代码",
            category=RuleCategory.PRIVACY,
            risk_level=RiskLevel.MEDIUM,
            pattern=r'(?i)(ssn|social[_-]?security|credit[_-]?card|phone|email).{0,20}(collect|gather|store|save)',
            suggestion="确保符合GDPR/CCPA等隐私法规要求"
        ),
        AuditRule(
            id="PRI-002",
            name="用户数据记录",
            description="检测可能记录敏感用户数据的行为",
            category=RuleCategory.PRIVACY,
            risk_level=RiskLevel.MEDIUM,
            pattern=r'(?i)(log|print|debug).{0,30}(user|password|token|session)',
            suggestion="避免在日志中记录敏感信息"
        ),

        # 伦理类规则
        AuditRule(
            id="ETH-001",
            name="偏见性语言",
            description="检测代码中的潜在偏见性语言",
            category=RuleCategory.ETHICS,
            risk_level=RiskLevel.MEDIUM,
            pattern=r'(?i)(blacklist|whitelist|master|slave)',
            suggestion="使用包容性语言替代，如blocklist/allowlist、primary/secondary"
        ),
        AuditRule(
            id="ETH-002",
            name="自动化决策",
            description="检测可能影响用户的自动化决策逻辑",
            category=RuleCategory.ETHICS,
            risk_level=RiskLevel.HIGH,
            pattern=r'(?i)(auto[_-]?approve|auto[_-]?reject|decision.{0,20}automatic)',
            suggestion="确保自动化决策有适当的人工审核机制"
        ),

        # 性能类规则
        AuditRule(
            id="PER-001",
            name="无限循环风险",
            description="检测可能导致无限循环的代码模式",
            category=RuleCategory.PERFORMANCE,
            risk_level=RiskLevel.HIGH,
            pattern=r'(?i)(while\s*True|while\s*1\s*:)(?!.*break)',
            suggestion="确保循环有明确的退出条件"
        ),
        AuditRule(
            id="PER-002",
            name="资源泄漏",
            description="检测未正确关闭的文件或连接",
            category=RuleCategory.PERFORMANCE,
            risk_level=RiskLevel.MEDIUM,
            pattern=r'(?m)^.{0,100}(open\(|connect\().{0,100}$',
            suggestion="使用上下文管理器(with语句)确保资源正确释放"
        ),

        # 合规类规则
        AuditRule(
            id="COM-001",
            name="许可证声明缺失",
            description="检测源文件缺少许可证声明",
            category=RuleCategory.COMPLIANCE,
            risk_level=RiskLevel.LOW,
            pattern=r'^(?!.*(?:license|copyright|SPDX)).*$',
            suggestion="在文件头部添加适当的许可证声明"
        ),
        AuditRule(
            id="COM-002",
            name="TODO/FIXME标记",
            description="检测代码中的TODO和FIXME标记",
            category=RuleCategory.COMPLIANCE,
            risk_level=RiskLevel.INFO,
            pattern=r'(?i)(TODO|FIXME|XXX|HACK)',
            suggestion="在发布前解决或跟踪这些标记项"
        ),
    ]

    def __init__(self, custom_rules: Optional[List[AuditRule]] = None):
        self.rules = custom_rules or self.DEFAULT_RULES

    def add_rule(self, rule: AuditRule):
        """添加自定义规则"""
        self.rules.append(rule)

    def get_rules_by_category(self, category: RuleCategory) -> List[AuditRule]:
        """按类别获取规则"""
        return [r for r in self.rules if r.category == category and r.enabled]

    def get_rules_by_risk(self, level: RiskLevel) -> List[AuditRule]:
        """按风险等级获取规则"""
        return [r for r in self.rules if r.risk_level == level and r.enabled]


class AgentAuditor:
    """Agent审计器"""

    def __init__(self, rule_engine: Optional[RuleEngine] = None):
        self.rule_engine = rule_engine or RuleEngine()
        self.findings: List[AuditFinding] = []

    def scan_file(self, file_path: Path) -> List[AuditFinding]:
        """扫描单个文件"""
        findings = []

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
        except Exception as e:
            print(f"Warning: Could not read {file_path}: {e}")
            return findings

        for rule in self.rule_engine.rules:
            if not rule.enabled:
                continue

            try:
                matches = list(re.finditer(rule.pattern, content, re.MULTILINE))
                for match in matches:
                    # 计算行号
                    line_num = content[:match.start()].count('\n') + 1

                    finding = AuditFinding(
                        rule_id=rule.id,
                        rule_name=rule.name,
                        category=rule.category.value,
                        risk_level=rule.risk_level.value,
                        message=f"检测到 {rule.name}: {match.group()[:50]}...",
                        location=str(file_path),
                        line_number=line_num,
                        suggestion=rule.suggestion,
                        timestamp=datetime.now().isoformat()
                    )
                    findings.append(finding)
            except re.error as e:
                print(f"Warning: Invalid regex in rule {rule.id}: {e}")

        return findings

    def scan_directory(self, directory: Path, extensions: Optional[List[str]] = None) -> AuditReport:
        """扫描目录"""
        if extensions is None:
            extensions = ['.py', '.js', '.ts', '.java', '.go', '.rs', '.cpp', '.c', '.h']

        all_findings = []
        total_files = 0
        total_lines = 0

        for ext in extensions:
            for file_path in directory.rglob(f'*{ext}'):
                if '.git' in str(file_path) or 'node_modules' in str(file_path) or '__pycache__' in str(file_path):
                    continue

                findings = self.scan_file(file_path)
                all_findings.extend(findings)
                total_files += 1

                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        total_lines += len(f.readlines())
                except:
                    pass

        # 生成摘要
        summary = self._generate_summary(all_findings)

        return AuditReport(
            target=str(directory),
            scan_time=datetime.now().isoformat(),
            total_files=total_files,
            total_lines=total_lines,
            findings=all_findings,
            summary=summary
        )

    def _generate_summary(self, findings: List[AuditFinding]) -> Dict[str, Any]:
        """生成审计摘要"""
        summary = {
            "total_findings": len(findings),
            "by_risk_level": {},
            "by_category": {},
            "top_issues": []
        }

        # 按风险等级统计
        for level in RiskLevel:
            count = len([f for f in findings if f.risk_level == level.value])
            if count > 0:
                summary["by_risk_level"][level.value] = count

        # 按类别统计
        for category in RuleCategory:
            count = len([f for f in findings if f.category == category.value])
            if count > 0:
                summary["by_category"][category.value] = count

        # 获取最常见的问题
        rule_counts = {}
        for finding in findings:
            rule_counts[finding.rule_name] = rule_counts.get(finding.rule_name, 0) + 1

        summary["top_issues"] = sorted(rule_counts.items(), key=lambda x: x[1], reverse=True)[:5]

        return summary


class ReportGenerator:
    """报告生成器"""

    @staticmethod
    def generate_json(report: AuditReport) -> str:
        """生成JSON格式报告"""
        return json.dumps({
            "target": report.target,
            "scan_time": report.scan_time,
            "total_files": report.total_files,
            "total_lines": report.total_lines,
            "summary": report.summary,
            "findings": [asdict(f) for f in report.findings]
        }, indent=2, ensure_ascii=False)

    @staticmethod
    def generate_html(report: AuditReport) -> str:
        """生成HTML格式报告"""
        risk_colors = {
            "critical": "#dc2626",
            "high": "#ea580c",
            "medium": "#ca8a04",
            "low": "#16a34a",
            "info": "#0891b2"
        }

        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AgentAudit 报告 - {report.target}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #1e3a8a 0%, #3730a3 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .header p {{ opacity: 0.9; font-size: 1.1em; }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8fafc;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        .stat-value {{ font-size: 2em; font-weight: bold; color: #3730a3; }}
        .stat-label {{ color: #64748b; margin-top: 5px; }}
        .findings {{
            padding: 30px;
        }}
        .finding {{
            background: #f8fafc;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            border-left: 4px solid;
        }}
        .finding.critical {{ border-left-color: #dc2626; }}
        .finding.high {{ border-left-color: #ea580c; }}
        .finding.medium {{ border-left-color: #ca8a04; }}
        .finding.low {{ border-left-color: #16a34a; }}
        .finding.info {{ border-left-color: #0891b2; }}
        .finding-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }}
        .finding-title {{ font-weight: 600; color: #1e293b; }}
        .risk-badge {{
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75em;
            font-weight: 600;
            text-transform: uppercase;
            color: white;
        }}
        .finding-meta {{
            color: #64748b;
            font-size: 0.9em;
            margin-bottom: 10px;
        }}
        .finding-message {{
            background: white;
            padding: 12px;
            border-radius: 8px;
            font-family: monospace;
            font-size: 0.9em;
            color: #334155;
            margin-bottom: 10px;
        }}
        .finding-suggestion {{
            background: #dbeafe;
            padding: 12px;
            border-radius: 8px;
            color: #1e40af;
            font-size: 0.9em;
        }}
        .footer {{
            text-align: center;
            padding: 20px;
            color: #64748b;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🛡️ AgentAudit 审计报告</h1>
            <p>扫描目标: {report.target} | 扫描时间: {report.scan_time}</p>
        </div>
        <div class="stats">
            <div class="stat-card">
                <div class="stat-value">{report.total_files}</div>
                <div class="stat-label">扫描文件数</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{report.total_lines:,}</div>
                <div class="stat-label">代码行数</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{report.summary['total_findings']}</div>
                <div class="stat-label">发现问题</div>
            </div>
        </div>
        <div class="findings">
            <h2 style="margin-bottom: 20px; color: #1e293b;">审计发现</h2>
"""

        for finding in report.findings:
            color = risk_colors.get(finding.risk_level, "#64748b")
            html += f"""
            <div class="finding {finding.risk_level}">
                <div class="finding-header">
                    <span class="finding-title">{finding.rule_name}</span>
                    <span class="risk-badge" style="background: {color};">{finding.risk_level}</span>
                </div>
                <div class="finding-meta">
                    📁 {finding.location}:{finding.line_number} | 🏷️ {finding.category}
                </div>
                <div class="finding-message">{finding.message}</div>
                <div class="finding-suggestion">
                    💡 建议: {finding.suggestion}
                </div>
            </div>
"""

        html += """
        </div>
        <div class="footer">
            Generated by AgentAudit-CLI 🛡️
        </div>
    </div>
</body>
</html>"""

        return html

    @staticmethod
    def generate_markdown(report: AuditReport) -> str:
        """生成Markdown格式报告"""
        md = f"""# 🛡️ AgentAudit 审计报告

## 扫描概览

| 项目 | 数值 |
|------|------|
| 扫描目标 | `{report.target}` |
| 扫描时间 | {report.scan_time} |
| 扫描文件数 | {report.total_files} |
| 代码行数 | {report.total_lines:,} |
| 发现问题总数 | {report.summary['total_findings']} |

## 风险分布

"""

        for level, count in report.summary.get("by_risk_level", {}).items():
            emoji = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢", "info": "🔵"}.get(level, "⚪")
            md += f"- {emoji} **{level.upper()}**: {count} 项\n"

        md += "\n## 类别分布\n\n"

        for category, count in report.summary.get("by_category", {}).items():
            md += f"- 📂 **{category}**: {count} 项\n"

        md += "\n## 详细发现\n\n"

        for finding in report.findings:
            emoji = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢", "info": "🔵"}.get(finding.risk_level, "⚪")
            md += f"""### {emoji} {finding.rule_name}

- **风险等级**: {finding.risk_level.upper()}
- **类别**: {finding.category}
- **位置**: `{finding.location}:{finding.line_number}`
- **描述**: {finding.message}
- **建议**: {finding.suggestion}

---

"""

        return md


def create_cli():
    """创建命令行接口"""
    parser = argparse.ArgumentParser(
        description="🛡️ AgentAudit-CLI - 轻量级AI Agent行为合规审计引擎",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s scan ./my-project
  %(prog)s scan ./src --format html --output report.html
  %(prog)s scan ./src --category security,privacy
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # scan 命令
    scan_parser = subparsers.add_parser('scan', help='扫描代码仓库')
    scan_parser.add_argument('path', help='要扫描的路径')
    scan_parser.add_argument('-f', '--format', choices=['json', 'html', 'markdown', 'console'],
                            default='console', help='输出格式 (默认: console)')
    scan_parser.add_argument('-o', '--output', help='输出文件路径')
    scan_parser.add_argument('-c', '--category', help='只扫描特定类别，逗号分隔 (security,privacy,ethics,performance,compliance)')
    scan_parser.add_argument('-r', '--risk', help='只报告特定风险等级，逗号分隔 (critical,high,medium,low,info)')
    scan_parser.add_argument('-e', '--extensions', help='文件扩展名，逗号分隔 (默认: .py,.js,.ts,.java,.go,.rs)')

    # rules 命令
    rules_parser = subparsers.add_parser('rules', help='列出所有审计规则')
    rules_parser.add_argument('-c', '--category', help='按类别过滤')
    rules_parser.add_argument('-r', '--risk', help='按风险等级过滤')

    # version 命令
    version_parser = subparsers.add_parser('version', help='显示版本信息')

    return parser


def main():
    """主函数"""
    parser = create_cli()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == 'version':
        print("🛡️ AgentAudit-CLI v1.0.0")
        print("轻量级AI Agent行为合规审计引擎")
        print("Zero dependencies, pure Python")
        return

    if args.command == 'rules':
        engine = RuleEngine()
        rules = engine.rules

        if args.category:
            categories = args.category.split(',')
            rules = [r for r in rules if r.category.value in categories]

        if args.risk:
            risks = args.risk.split(',')
            rules = [r for r in rules if r.risk_level.value in risks]

        print(f"\n🛡️ 审计规则列表 (共 {len(rules)} 条)\n")
        print("-" * 80)

        for rule in rules:
            emoji = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢", "info": "🔵"}.get(rule.risk_level.value, "⚪")
            print(f"\n{emoji} [{rule.id}] {rule.name}")
            print(f"   类别: {rule.category.value} | 风险: {rule.risk_level.value}")
            print(f"   描述: {rule.description}")
            print(f"   建议: {rule.suggestion}")

        return

    if args.command == 'scan':
        target_path = Path(args.path)

        if not target_path.exists():
            print(f"❌ 错误: 路径不存在: {args.path}")
            sys.exit(1)

        # 配置规则引擎
        engine = RuleEngine()

        if args.category:
            categories = args.category.split(',')
            for rule in engine.rules:
                rule.enabled = rule.category.value in categories

        if args.risk:
            risks = args.risk.split(',')
            for rule in engine.rules:
                if rule.enabled:
                    rule.enabled = rule.risk_level.value in risks

        # 配置扩展名
        extensions = None
        if args.extensions:
            extensions = [f".{ext.lstrip('.')}" for ext in args.extensions.split(',')]

        # 执行扫描
        print(f"🛡️ AgentAudit 开始扫描...")
        print(f"   目标: {target_path.absolute()}")
        print(f"   规则: {len([r for r in engine.rules if r.enabled])} 条启用")
        print()

        auditor = AgentAuditor(engine)

        if target_path.is_file():
            findings = auditor.scan_file(target_path)
            report = AuditReport(
                target=str(target_path),
                scan_time=datetime.now().isoformat(),
                total_files=1,
                total_lines=0,
                findings=findings,
                summary=auditor._generate_summary(findings)
            )
        else:
            report = auditor.scan_directory(target_path, extensions)

        # 生成报告
        generator = ReportGenerator()

        if args.format == 'json':
            output = generator.generate_json(report)
        elif args.format == 'html':
            output = generator.generate_html(report)
        elif args.format == 'markdown':
            output = generator.generate_markdown(report)
        else:  # console
            output = None

        # 输出结果
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output if output else generator.generate_markdown(report))
            print(f"✅ 报告已保存: {args.output}")
        else:
            if output:
                print(output)
            else:
                # 控制台输出
                print(f"\n📊 扫描结果")
                print(f"   文件数: {report.total_files}")
                print(f"   代码行: {report.total_lines:,}")
                print(f"   发现项: {report.summary['total_findings']}")
                print()

                if report.findings:
                    print("🚨 审计发现:")
                    for finding in report.findings:
                        emoji = {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢", "info": "🔵"}.get(finding.risk_level, "⚪")
                        print(f"\n{emoji} [{finding.risk_level.upper()}] {finding.rule_name}")
                        print(f"   📁 {finding.location}:{finding.line_number}")
                        print(f"   📝 {finding.message[:100]}...")
                        print(f"   💡 {finding.suggestion}")
                else:
                    print("✅ 未发现合规问题！")

        return


if __name__ == '__main__':
    main()
