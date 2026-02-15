"""Register MCP prompts with FastMCP."""

from fastmcp import FastMCP

from ..prompts.workflow_prompt import KNOWLEDGE_ASSISTANT_WORKFLOW


def register_prompts(mcp: FastMCP) -> None:
    """Register MCP prompts."""

    @mcp.prompt()
    def knowledge_assistant_workflow() -> str:
        """Multi-agent RAG workflow with human-in-the-loop: query → review proposal → approve or edit."""
        return KNOWLEDGE_ASSISTANT_WORKFLOW
