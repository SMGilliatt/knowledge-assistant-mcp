# Knowledge Assistant MCP Server - Docker image
FROM python:3.13-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Project files
COPY pyproject.toml .python-version ./
RUN uv sync --no-dev --no-install-project

COPY src ./src
RUN uv sync --no-dev

# Persist Chroma data if mounted
ENV CHROMA_PERSIST_DIR=/app/chroma_data
VOLUME /app/chroma_data

# Run MCP server (stdio by default; override for HTTP)
ENTRYPOINT ["uv", "run", "python", "-m", "src.server"]
CMD ["--transport", "stdio"]
