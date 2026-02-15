"""Register MCP resources with FastMCP."""

from fastmcp import FastMCP

from ..resources.server_info import get_server_info


def register_resources(mcp: FastMCP) -> None:
    """Register MCP resources."""

    @mcp.resource("knowledge-assistant://server_info")
    def server_info() -> dict:
        """Server and knowledge base configuration (name, version, collection, RAG settings)."""
        return get_server_info()
