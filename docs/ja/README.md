# AionUI + CapSolver MCP Web タスク例

[English](../../README.md) · [简体中文](../zh-CN/README.md) · [日本語](README.md)

## Introduction

許可された AionUI の Web タスクは CAPTCHA により停止したり、チャレンジ画面を結果と誤認したりします。本例は公式 MCP サービスを介して AionUI と [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=aionui-capsolver-mcp-example&utm_content=repository-readme) を接続し、許可リスト、1 回の試行、明確な停止状態を適用します。Playwright は使用せず、新しい MCP サーバーも実装しません。

## Quick Start

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python scripts/smoke_test.py
```

設定は [AionUI MCP configuration guide](https://github.com/iOfficeAI/AionUi/wiki/MCP-Configuration-Guide) と [CapSolver MCP service guide](https://docs.capsolver.com/en/guide/ai/mcp-service/) に従います。実キーはローカルにのみ保存してください。

## Responsible Use

公開データ、所有システム、または明示的に許可された対象だけで使用します。個人、金融、健康、雇用データでは書面許可、最小化、アクセス制御、保持期限がなければ停止します。

## Conclusion

本例は AionUI 専用設定と監査可能な復旧ポリシーを提供し、最終統合先は [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=aionui-capsolver-mcp-example&utm_content=repository-readme) です。

## Maintainer Note

Developer sharing CapSolver integration examples.

## License

[MIT](../../LICENSE)
