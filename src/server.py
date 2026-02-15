"""Knowledge Assistant MCP Server – main entry point."""

import argparse

from fastmcp import FastMCP

from .config import settings
from .routers import register_prompts, register_resources, register_tools
from .utils.opik_utils import configure_opik


def create_mcp() -> FastMCP:
    """Create and configure the FastMCP server instance."""
    mcp = FastMCP(
        name=settings.server_name,
        version=settings.version,
    )
    register_tools(mcp)
    register_resources(mcp)
    register_prompts(mcp)
    return mcp


mcp = create_mcp()


def main() -> None:
    """Run the MCP server (stdio by default)."""
    if configure_opik():
        print(f"📊 Opik monitoring enabled for project: {settings.opik_project_name}")
    parser = argparse.ArgumentParser(description="Knowledge Assistant MCP Server")
    parser.add_argument(
        "--transport",
        "-t",
        type=str,
        choices=["stdio", "http"],
        default="stdio",
        help="Transport: stdio or http",
    )
    parser.add_argument("--port", "-p", type=int, default=8000, help="Port for HTTP transport")
    args = parser.parse_args()
    if args.transport == "http":
        mcp.run(transport="streamable-http", port=args.port)
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
