# Capstone project – status and context

**Last updated:** Feb 2025 (session paused)

## What this is

Multi-agent RAG **Knowledge Assistant MCP Server** for the AI Agents course capstone. Built in **Python 3.13**, FastMCP, with mandatory + 4+ custom features.

## What’s done

- **Structure:** `src/server.py`, `src/routers/` (tools, resources, prompts), `src/tools/`, `src/app/`, `src/config/settings.py`, `src/models/schemas.py`, `src/utils/`, etc.
- **Mandatory:** MCP server (FastMCP), multiple tools, one workflow prompt with **human-in-the-loop** (query → propose answer → user approves/edits via `approve_or_edit_answer`).
- **Custom (6):** Multi-agent (coordinator + retriever + synthesizer), RAG (ChromaDB + Google embeddings), MCP resource (`server_info`), human-in-the-loop validation, structured outputs (Pydantic), Opik observability (optional).
- **Extras:** `.env.sample`, Dockerfile, `.github/workflows/ci.yml` (Ruff), README with setup, env vars, Cursor JSON, required/custom features listed.
- **Python:** Set to **3.13** (`.python-version`, `pyproject.toml`, Dockerfile, CI) for ChromaDB compatibility.

## Location

This folder is the project root. For certification, push it to a **public GitHub repo** as the repo root; do **not** run `uv init` (project is already initialized).

## What you still need to do

1. In this project folder, run `uv sync` (install deps).
2. Copy `.env.sample` to `.env`, set `GOOGLE_API_KEY` (and optionally `OPIK_API_KEY`).
3. Test: `uv run python -m src.server --transport stdio`.
4. Create a new GitHub repo, push this project as the repo root, ensure no `.env`/secrets committed.
5. Optional: run `uv lock`, commit `uv.lock`, for reproducible Docker/CI.

## Ruff

Ruff target is `py313`; CI uses Python 3.13.

## Quick reference

- **Tools:** `query_knowledge_base`, `approve_or_edit_answer`, `add_documents`, `search_knowledge_base`.
- **Prompt:** `knowledge_assistant_workflow` – describes the flow and the required human approval step.
- **Resource:** `knowledge-assistant://server_info`.

## Requirements (single source of truth)

**`COURSE_REQUIREMENTS.md`** in this folder contains the full project requirements (mandatory, custom, README, JSON example, Making Your Project Stand Out). Use it to check the implementation and README for accuracy.

When you return, you can say: “Continue from CAPSTONE_STATUS.md” and share any blockers or next steps you want to tackle.

---

## Chat history / session summary

*(Condensed so you or a future session can pick up context.)*

1. **Project requirements** – Mandatory: MCP server, tools, prompt with human-in-the-loop, uv, structure, README, no secrets, .env.sample; at least 4 custom features.

2. **Build** – Implemented: FastMCP server, config (pydantic-settings), RAG (ChromaDB + Google embeddings), multi-agent orchestrator, tools (query_knowledge_base, approve_or_edit_answer, add_documents, search_knowledge_base), workflow prompt with human-in-the-loop, structured outputs (Pydantic), MCP resource (knowledge-assistant://server_info), optional Opik, .env.sample, Dockerfile, CI (Ruff), README.

3. **Python 3.13** – .python-version, pyproject.toml, Dockerfile, and CI use Python 3.13 (ChromaDB does not support 3.14). Don’t run `uv init`; the project is already initialized. Use `uv sync` to install dependencies.

4. **Pause + remember** – This CAPSTONE_STATUS.md was created to preserve context across sessions; chat history was condensed above.
