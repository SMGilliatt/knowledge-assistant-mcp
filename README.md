# Knowledge Assistant MCP Server

A **multi-agent RAG (Retrieval-Augmented Generation)** MCP server built with **FastMCP** in Python. It answers questions from your documents using a coordinator, retriever, and synthesizer agents, and includes a **human-in-the-loop** step where you approve or request edits before finalizing answers.

## 3. What your MCP server does and its use cases

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

## 4. Step-by-step project setup

### 4.1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/knowledge-assistant-mcp.git
cd knowledge-assistant-mcp
```

### 4.2. Install dependencies with `uv`

```bash
uv sync
```

This creates a virtual environment (Python 3.14) and installs dependencies from `pyproject.toml`.

### 4.3. Configure environment variables

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

### 4.4. Run the server

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

## 5. Environment variables and API keys

All variables that may be added to `.env`, and where to get API keys:

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

---

## 6. JSON configuration to connect from an MCP client (e.g. Cursor)

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

## 7. Required features implemented

Brief description of each mandatory feature:

- **MCP server in Python with FastMCP**: Implemented in `src/server.py`; creates a `FastMCP` instance and registers routers.
- **At least one MCP tool with meaningful functionality**: Multiple tools: `query_knowledge_base`, `approve_or_edit_answer`, `add_documents`, `search_knowledge_base`.
- **At least one MCP prompt that ties tools into an agentic workflow with a user feedback/confirmation step**: The `knowledge_assistant_workflow` prompt describes the flow: (1) use `query_knowledge_base` to get a proposed answer, (2) review the proposal, (3) use `approve_or_edit_answer` to approve or request edits. This implements the required human-in-the-loop step.
- **Project initialized with `uv`**: `pyproject.toml`, `.python-version`; dependencies installed with `uv sync`.
- **Clear structure**: `src/`, `src/server.py`, `src/routers/` (tools, resources, prompts), `src/tools/`, `src/resources/`, `src/prompts/`, `src/app/`, `src/utils/`, `src/config/settings.py` (pydantic-settings).
- **README**: This file: description, setup, env vars, Cursor JSON, required/custom features.
- **No API keys in repo**: Keys in `.env`; `.env.sample` with fake values; `.env` in `.gitignore`.
- **`.env.sample`**: Provided with placeholder values and structure.

---

## 8. Custom features implemented

Brief description of each custom feature (at least 4 required; we implemented 6):

1. **Multi-agent orchestration**: Coordinator agent (decides answer_from_kb vs general_answer), retriever agent (RAG over ChromaDB), synthesizer agent (produces structured answer proposal). Implemented in `src/app/orchestrator.py` and used by `query_knowledge_base`.
2. **RAG with vector database**: ChromaDB with LangChain and Google embeddings; `search_knowledge_base` and ingestion via `add_documents`. Persistence via `CHROMA_PERSIST_DIR`.
3. **MCP resources**: `server_info` resource exposes server name, version, knowledge base collection name, and RAG settings for client context.
4. **Human-in-the-loop validation**: “AI generation → validation” pattern: the workflow returns a **proposal**; the user must call `approve_or_edit_answer` to approve or request edits before finalizing.
5. **Structured outputs**: Pydantic models (`AnswerProposal`, `SearchResult`, `RetrievedChunk`, `SynthesisResult`) used for synthesizer output and API responses.
6. **Observability (Opik)**: Optional Opik integration for tracing; configured when `OPIK_API_KEY` is set; used at server startup and available for tool/LLM tracing.

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
