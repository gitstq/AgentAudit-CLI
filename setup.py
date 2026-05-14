#!/usr/bin/env python3
"""
AgentAudit-CLI Setup
轻量级AI Agent行为合规审计引擎
"""

from setuptools import setup, find_packages
from pathlib import Path

# 读取README
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""

setup(
    name="agentaudit-cli",
    version="1.0.0",
    author="gitstq",
    author_email="",
    description="轻量级AI Agent行为合规审计引擎 | Lightweight AI Agent Behavior Compliance Audit Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gitstq/agentaudit-cli",
    py_modules=["agentaudit"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "agentaudit=agentaudit:main",
            "aa=agentaudit:main",
        ],
    },
    keywords="ai agent security audit compliance privacy ethics",
    project_urls={
        "Bug Reports": "https://github.com/gitstq/agentaudit-cli/issues",
        "Source": "https://github.com/gitstq/agentaudit-cli",
    },
)
