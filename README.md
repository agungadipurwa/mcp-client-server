![Python](https://img.shields.io/badge/language-python-blue)
![MCP](https://img.shields.io/badge/mcp-grey?logo=anthropic&link=https%3A%2F%2Fmodelcontextprotocol.io%2Fintroduction)
![Streamlit.io](https://img.shields.io/badge/streamlit.io-grey?logo=streamlit)


<h1 align="center">
Logtime Summarizer 🤖
</h1>
<p align="center">
  <strong>A Chatbot for seamless track project health and employee performance by analyzing log time data from various data source</strong>
</p>

## Table of Contens
- [1. Overview](#overview)
- [2. Key Features](#key-features)
- [3. Tech Stacks](#tech-stacks)
- [4. Installation](#installation)
    - [Getting Started](#getting-started)
    - [Installing Python](#installing-python)
    - [Installing uv package manager](#installing-uv-package-manager)
    - [Setup dependecies](#setup-dependecies)
    - [Setup .env configuration](#setup-env-configuration)
- [5. Test Server](#test-server)
    - [Using npx as inspector](#using-npx-as-inspector)
    - [Using uv](#using-uv)
- [6. Future Roadmap](#future-roadmap)
## Overview

This Chatbot power with **Model Context Protocol (MCP)** as standardized way to connect AI models to different data sources and tools.

## Key Features

The main feature is a **Chatbot Assistant** that answers summary about:

- **Projects:** Check on budgets, timelines, and overall progress.
- **Employees:** View team performance, workload, and efficiency.
- **Clients:** Track project status and resources for each client account.

## Tech Stacks
- **Client**: Streamlit, Cursor
- **Server**: Python, FastAPI, OpenAI, MCP

## Installation
### Getting started
Clone the project using HTTPS

```bash
  git clone https://git.gits.id/ai-for-gits/ai-multi-agent-crew-ai-be.git
```

### Installing Python 
Recommendation to use python version 3.12.10, you can get it [here](https://www.python.org/downloads/windows/) or directly download the .exe file by [click this url](https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe)

### Installing uv package manager
This project power with UV Python package and project manager. Here common method for installat UV
```bash
  pip install uv
```

You can learn more other methode on [UV Documentation](https://docs.astral.sh/uv/getting-started/installation/)

### Setup dependecies
Initialization uv package manager by create virtual enviroment and install the dependencies
```bash
  uv init
  uv venv --python 3.12
  uv add -r requirements.txt
```
Your folder will update with .venv, pyproject.toml, main.py, and uv.lock
```md
logtime-summarize
├── .venv
├── ...
├── api
│   └── ...   
├── front
│   └── ...
├── mcp-server
│   └── ...
├── main.py
├── pyproject.toml
├── README.md
├── requirement.txt
└── uv.lock
```
### Setup .env configuration
Make file .env, _do double enter while run the script below_
```bash
  echo > ".env"
```
Copy setup on .env.example to .env

### Setup credentials configuration
Make file credentials json file, _do double enter while run the script below_
```bash
  echo > "./mcp-server/credentials.json"
```
Copy setup on credentials.example.json to credentials.json

### Test Server
#### Using npx as inspector
<img src="https://mintlify.s3.us-west-1.amazonaws.com/mcp/logo/dark.svg" alt="Alt text" width="250">

```bash
  npx @modelcontextprotocol/inspector    
```
- COMMAND: `{add-your-own-path}/logtime-summarizer/mcp-server/main.py`
- ARGUMENTS: `{add-your-own-path}/logtime-summarizer/mcp-server/main.py`
- CONFIGURATE:
    - ...
    - Inspector Proxy Address: `copy from terminal after running npx`
    - Proxy Session Token: `copy from terminal after running npx`

**Got an error?** Learn more about the [inspector]("https://modelcontextprotocol.io/docs/tools/inspector")
#### Using uv
```bash
  uv run mcp dev ./mcp-server/main.py
```
do same things like npx exclude setup command and arguments
- CONFIGURATE:
    - ...
    - Inspector Proxy Address: `copy from terminal after running uv`
    - Proxy Session Token: `copy from terminal after running uv`
    
### Configuration Host for MCP client (Cursor, Claude Desktop or other IDEs)
```python
{
    "mcpServers": {
        "logtime-summarizer": {
            "command": "add-your-own-path}/.local/bin/uv.exe",
            "args": [
                "run",
                "--directory",
                "C:\\D\\Work\\daily-reminder\\utils\\gsheet",
                "stdio.py"
            ],
            "env": {
                "OPENAI_API_KEY": "<your-openai-api-key>"
            }
        }
    }
}
```
* **Cursor** `~/.cursor/mcp.json`
    
    Learn more [Cursor Model Contex Protocol (MCP)](https://docs.cursor.com/context/mcp)

* **Trae** `~/.cursor/mcp.json`
    
    Learn more [Trae Model Contex Protocol (MCP)](https://docs.trae.ai/ide/model-context-protocol)

* **Windsurf** `~/.codeium/windsurf/mcp_config.json`
    
    Learn more [Windsurf Model Contex Protocol (MCP)](https://docs.windsurf.com/windsurf/cascade/mcp)
* **Claude Desktop** `~/Library/Application\ Support/Claude/claude_desktop_config.json`

    Learn more [Claude Desktop Model Contex Protocol (MCP)](https://modelcontextprotocol.io/quickstart/user)
* **Claude Code** `~/.claude.json`

    Learn more [Claude Code Model Contex Protocol (MCP)](https://docs.anthropic.com/en/docs/claude-code/mcp)

#### Learn more other [MCP Clients](https://modelcontextprotocol.io/clients) that support MCP

## Future Roadmap
- [ ] Custom MCP Client (UI) using Streamlit
- [ ] Deploy public MCP server
- [ ] Integration MCP server with Slack Bot