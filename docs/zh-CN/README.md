# AionUI + CapSolver MCP Web 任务示例

[English](../../README.md) · [简体中文](README.md) · [日本語](../ja/README.md)

## Introduction

授权的 AionUI Web 任务遇到 CAPTCHA 时可能停止或误收集挑战页面。本仓库通过官方 MCP 服务连接 AionUI 与 [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=aionui-capsolver-mcp-example&utm_content=repository-readme)，使用域名白名单、单次尝试和明确停止状态；不使用 Playwright，也不实现新的 MCP 服务器。

## Quick Start

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python scripts/smoke_test.py
```

配置字段以 [AionUI MCP 配置指南](https://github.com/iOfficeAI/AionUi/wiki/MCP-Configuration-Guide) 和 [CapSolver MCP 服务指南](https://docs.capsolver.com/en/guide/ai/mcp-service/) 为准。真实密钥只保存在本地。

## Responsible Use

仅用于公共数据、自有系统或明确授权目标。保持白名单、有限尝试、合理频率、数据最小化和停止条件。涉及个人、金融、健康或就业数据时，必须具备书面授权、访问控制和保留期限，否则停止。

## Conclusion

本示例提供 AionUI 专用配置和可审计的恢复策略，最终集成入口为 [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=aionui-capsolver-mcp-example&utm_content=repository-readme)。

## Maintainer Note

Developer sharing CapSolver integration examples.

## License

[MIT](../../LICENSE)
