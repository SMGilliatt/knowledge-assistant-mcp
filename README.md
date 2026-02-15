# Knowledge Assistant MCP Server

A **multi-agent RAG (Retrieval-Augmented Generation)** MCP server built with **FastMCP** in Python. It answers questions from your documents using a coordinator, retriever, and synthesizer agents, and includes a **human-in-the-loop** step where you approve or request edits before finalizing answers.

## What it does

- **Query your knowledge base**: Ask questions in natural language; the server retrieves relevant chunks and proposes an answer with citations.
- **Multi-agent pipeline**: A coordinator decides whether to use the knowledge base, a retriever (RAG) fetches relevant documents, and a synthesizer produces a structured answer proposal.
- **Human-in-the-loop**: You review the proposed answer and either approve it or request edits before the answer is finalized.
- **Add documents**: Ingest text into the vector store (ChromaDB) so the assistant can answer from your own content.

**Use cases**: Internal knowledge assistant, FAQ over your docs, Q&A over notes or wikis, and similar RAG workflows that require a human approval step.

---

## Project Structure

```
knowledge-assistant-mcp/
├── src/
│   ├── server.py           # FastMCP app entry point
│   ├── config/
│   │   └── settings.py     # pydantic-settings (server name, API keys, model, RAG settings)
│   ├── routers/
│   │   ├── tools.py        # Register MCP tools
│   │   ├── resources.py    # Register MCP resources
│   │   └── prompts.py      # Register MCP prompts
│   ├── tools/              # Tool implementations
│   ├── resources/          # Resource implementations
│   ├── prompts/            # Prompt content (workflow with human-in-the-loop)
│   ├── app/                # Core logic: RAG, LLM, orchestrator (coordinator/retriever/synthesizer)
│   ├── models/             # Pydantic schemas (structured outputs)
│   └── utils/              # Helpers (e.g. Opik)
├── pyproject.toml
├── .env.sample
├── Dockerfile
└── README.md
```

---

## Setup

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/knowledge-assistant-mcp.git
cd knowledge-assistant-mcp
```

### Install dependencies with `uv`

```bash
uv sync
```

This creates a virtual environment (Python 3.13) and installs dependencies from `pyproject.toml`.

### Configure environment variables

```bash
cp .env.sample .env
```

Edit `.env` and set at least:

- **`GOOGLE_API_KEY`** (required): Used for Gemini (LLM and embeddings).  
  Get it from [Google AI Studio](https://aistudio.google.com/app/apikey).

Optional:

- **`OPIK_API_KEY`**: For observability (tracing). Get it from [Opik](https://www.comet.com/site/products/opik/).
- **`OPIK_PROJECT_NAME`**: Opik project name (default: `knowledge-assistant`).
- **`MODEL_NAME`**: Gemini model (default: `gemini-2.0-flash`).
- **`CHROMA_PERSIST_DIR`**: Directory for ChromaDB (default: `./chroma_data`).
- **`CHROMA_COLLECTION`**: Collection name (default: `knowledge_base`).
- **`RAG_TOP_K`**: Number of chunks to retrieve (default: `5`).
- **`EMBEDDING_MODEL`**: Google embedding model for RAG (default: `models/gemini-embedding-001`). Override if your API uses a different model.

### Run the server

**Stdio (for Cursor / Claude Desktop):**

```bash
uv run python -m src.server --transport stdio
```

**HTTP:**

```bash
uv run python -m src.server --transport http --port 8000
```

Or use the entry point:

```bash
uv run knowledge-assistant-mcp --transport stdio
```

---

## Environment variables

Variables you can set in `.env`, and where to get API keys:

### Environment variables summary

| Variable            | Required | Description |
|---------------------|----------|-------------|
| `GOOGLE_API_KEY`    | Yes      | Google AI (Gemini) API key – [Google AI Studio](https://aistudio.google.com/app/apikey) |
| `OPIK_API_KEY`      | No       | Opik API key for observability – [Opik](https://www.comet.com/site/products/opik/) |
| `OPIK_PROJECT_NAME` | No       | Opik project name (default: `knowledge-assistant`) |
| `MODEL_NAME`        | No       | Gemini model (default: `gemini-2.0-flash`) |
| `CHROMA_PERSIST_DIR`| No       | ChromaDB persistence directory (default: `./chroma_data`) |
| `CHROMA_COLLECTION` | No       | ChromaDB collection name (default: `knowledge_base`) |
| `RAG_TOP_K`         | No       | Number of chunks to retrieve (default: `5`) |
| `EMBEDDING_MODEL`   | No       | Google embedding model for RAG (default: `models/gemini-embedding-001`) |

---

## Connecting from Cursor (or another MCP client)

Add this to your Cursor MCP settings (e.g. `.cursor/mcp.json`), replacing the path and API key as needed:

```json
{
  "mcpServers": {
    "knowledge-assistant": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/knowledge-assistant-mcp",
        "run",
        "python",
        "-m",
        "src.server",
        "--transport",
        "stdio"
      ],
      "env": {
        "GOOGLE_API_KEY": "your-google-api-key-here"
      }
    }
  }
}
```

You can also rely on a `.env` file in the project directory and omit `env` or only set `ENV_FILE_PATH` if your client supports it.

---

## Features

**Core:**

FastMCP server (`src/server.py`) with tools (`query_knowledge_base`, `approve_or_edit_answer`, `add_documents`, `search_knowledge_base`), one workflow prompt (`knowledge_assistant_workflow`) with a human-in-the-loop step (review proposal → approve or edit via `approve_or_edit_answer`), `uv`-based setup, and the structure above. No API keys in the repo; `.env.sample` and `.gitignore` are included.

**Additional:**

- **Multi-agent orchestration** – Coordinator, retriever (RAG), and synthesizer agents in `src/app/orchestrator.py`.
- **RAG with vector database** – ChromaDB + LangChain + Google embeddings; `search_knowledge_base` and `add_documents`; persistence via `CHROMA_PERSIST_DIR`.
- **MCP resource** – `knowledge-assistant://server_info` exposes server name, version, collection, and RAG settings.
- **Human-in-the-loop validation** – Workflow returns a proposal; the user approves or requests edits with `approve_or_edit_answer` before finalizing.
- **Structured outputs** – Pydantic models (`AnswerProposal`, `SearchResult`, `RetrievedChunk`, `SynthesisResult`) for synthesizer and API responses.
- **Observability (Opik)** – Optional tracing when `OPIK_API_KEY` is set.

---

## Docker

Build and run with Docker:

```bash
docker build -t knowledge-assistant-mcp .
docker run --rm -e GOOGLE_API_KEY=your-key -v $(pwd)/chroma_data:/app/chroma_data knowledge-assistant-mcp --transport stdio
```

For HTTP on port 8000:

```bash
docker run --rm -p 8000:8000 -e GOOGLE_API_KEY=your-key -v $(pwd)/chroma_data:/app/chroma_data knowledge-assistant-mcp --transport http --port 8000
```

---

## License

MIT (or your chosen license).
