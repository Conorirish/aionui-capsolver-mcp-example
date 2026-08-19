# AionUI + CapSolver MCP Web Task Example

Configure a local CapSolver MCP service in AionUI and apply bounded recovery to authorized web tasks without Playwright.

[English](README.md) · [简体中文](docs/zh-CN/README.md) · [日本語](docs/ja/README.md)

## Introduction

An authorized AionUI web task can stop when a CAPTCHA appears or mistake a challenged response for valid data. This repository connects AionUI to [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=aionui-capsolver-mcp-example&utm_content=repository-readme) through the official local MCP service, permits one recovery attempt, and stops on denied targets, tool errors, repeated challenges, or an exhausted budget.

AionUI launches the official `capsolver-mcp` command over stdio. The dependency-free Python code models the recovery decision boundary; it is not another MCP server and does not automate a browser.

## Features

- Official AionUI `mcpServers` stdio configuration.
- Host allowlist and one-attempt default.
- Explicit completed, denied, tool-error, persistent-challenge, and budget states.
- Offline unit tests and deterministic smoke example.

## How It Works

AionUI loads `config/aionui.mcp.json`, starts the service, and discovers its tools. A challenge from an authorized task enters `RecoveryPolicy`; only an allowlisted host may call the MCP tool. A successful normalized outcome resumes once; every other outcome stops.

## Architecture

```text
AionUI task → challenge → allowlist → MCP tool → resume once or stop
```

## Quick Start

Install AionUI, Python 3.11+, and the packages in the official [CapSolver MCP installation guide](https://docs.capsolver.com/en/guide/ai/mcp-service/).

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python scripts/smoke_test.py
```

Add `config/aionui.mcp.json` through AionUI MCP management and run its connection test. The file follows the official [AionUI MCP configuration guide](https://github.com/iOfficeAI/AionUi/wiki/MCP-Configuration-Guide). Replace `YOUR_API_KEY` only in local configuration.

## Usage

```python
from aionui_recovery import RecoveryPolicy, ToolOutcome
p = RecoveryPolicy({"qa.example.test"})
decision = p.begin("https://qa.example.test/checkpoint")
if decision.action == "call_mcp_tool":
    decision = p.finish(ToolOutcome(True, True))
```

Do not guess tool names, fields, or arguments; use the current schema exposed by the installed official service.

## Example Output

```text
call_mcp_tool: authorized recovery attempt 1 of 1
completed: challenge cleared; task may resume once
```

## Supported Scenarios

Controlled QA on owned hosts, explicitly authorized RPA, and local configuration testing with mock outcomes.

## Project Structure

`config/` contains the AionUI config; `src/` the recovery state machine; `tests/` unit tests; and `scripts/` the smoke test.

## Testing

Tests cover success, denial, tool errors, persistent challenges, attempt exhaustion, and the exact stdio configuration.

## Troubleshooting

Use the official absolute-Python command form if `capsolver-mcp` is not on PATH. If AionUI reports a connection failure or empty tool list, stop and verify installed versions. Never invent fields or automatically expand the attempt budget.

## Responsible Use

Use only public data, systems you own, or explicitly authorized targets. Keep a narrow allowlist, one-attempt default, reasonable rate limits, minimal collection, short retention, and visible stop reasons. Never use private or restricted data, credentials, access-control evasion, unbounded collection, or unauthorized access. For personal, financial, health, or employment data, require written authorization, minimization, access controls, and a retention schedule; stop if any control is absent.

## Contributing

See [contribution guidelines](CONTRIBUTING.md). Preserve offline tests, bounded recovery, and official-source requirements.

## Security

See [security policy](SECURITY.md). Never include keys, browser sessions, cookies, or captured responses in issues.

## Conclusion

This AionUI-specific configuration and recovery controller is technically distinct from a generic MCP server and stops clearly when recovery is unsafe or unsuccessful with [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=aionui-capsolver-mcp-example&utm_content=repository-readme).

## Maintainer Note

Developer sharing CapSolver integration examples.

## License

[MIT](LICENSE)
