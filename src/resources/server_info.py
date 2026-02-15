"""MCP resource: server and knowledge base info."""

from ..config import settings


def get_server_info() -> dict:
    """Return server name, version, and KB collection name for context."""
    return {
        "server_name": settings.server_name,
        "version": settings.version,
        "knowledge_base_collection": settings.chroma_collection_name,
        "rag_top_k": settings.rag_top_k,
    }
