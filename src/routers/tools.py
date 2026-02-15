"""Register MCP tools with FastMCP."""

from fastmcp import FastMCP

from ..tools import (
    add_documents_tool,
    approve_or_edit_answer_tool,
    query_knowledge_base_tool,
    search_only_tool,
)


def register_tools(mcp: FastMCP) -> None:
    """Register all MCP tools."""

    @mcp.tool()
    def query_knowledge_base(query: str, top_k: int = 5) -> dict:
        """
        Ask the knowledge assistant a question. Runs a multi-agent pipeline:
        coordinator -> retriever (RAG) -> synthesizer. Returns a proposed answer for your review.
        After reviewing, call approve_or_edit_answer to approve or request edits (human-in-the-loop).
        """
        return query_knowledge_base_tool(query, top_k=top_k)

    @mcp.tool()
    def approve_or_edit_answer(
        approved: bool,
        proposal_answer: str,
        user_feedback: str | None = None,
    ) -> dict:
        """
        Human-in-the-loop: approve the proposed answer from query_knowledge_base, or request edits.
        Set approved=True to accept, or approved=False and provide user_feedback for changes.
        """
        return approve_or_edit_answer_tool(
            approved=approved,
            proposal_answer=proposal_answer,
            user_feedback=user_feedback,
        )

    @mcp.tool()
    def add_documents(text: str, source: str = "user_input") -> dict:
        """Add a document (text) to the knowledge base. Use source to label where it came from."""
        return add_documents_tool(text=text, source=source)

    @mcp.tool()
    def search_knowledge_base(query: str, top_k: int = 5) -> dict:
        """Search the knowledge base only (retriever); returns chunks without generating an answer."""
        return search_only_tool(query=query, top_k=top_k)
