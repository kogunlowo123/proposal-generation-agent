# Proposal Generation Agent

[![CI](https://github.com/kogunlowo123/proposal-generation-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/proposal-generation-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Sales | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Proposal generation agent that creates customized sales proposals, incorporates pricing configurations, adds case studies and social proof, manages proposal workflows, and tracks proposal engagement.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_proposal` | Generate a customized sales proposal from template and deal data |
| `configure_pricing` | Configure pricing for a proposal based on deal parameters |
| `add_case_studies` | Select and add relevant case studies to the proposal |
| `send_proposal` | Send proposal with tracking and e-signature |
| `track_proposal` | Track proposal views, time spent per section, and signatures |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/proposal-generation/execute` | Execute primary action |
| `POST` | `/api/v1/proposal-generation/analyze` | Run analysis |
| `GET` | `/api/v1/proposal-generation/metrics` | Get metrics |
| `PUT` | `/api/v1/proposal-generation/configure` | Configure settings |
| `POST` | `/api/v1/proposal-generation/report` | Generate report |

## Features

- Proposal
- Generation
- Analytics
- Automation

## Integrations

- Salesforce
- Hubspot
- Outreach
- Apollo
- Linkedin Sales Navigator

## Architecture

```
proposal-generation-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── proposal_generation_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**CRM + Sales Engagement + LLM**

---

Built as part of the Enterprise AI Agent Platform.
