"""MCP tools: query knowledge base and add documents."""

from langchain_core.documents import Document

from ..app.rag import add_documents_to_knowledge_base, search_knowledge_base
from ..app.orchestrator import run_agent_pipeline
from ..models.schemas import AnswerProposal, SearchResult


def query_knowledge_base_tool(query: str, top_k: int = 5) -> dict:
    """
    Multi-agent pipeline: coordinator decides, retriever fetches from RAG, synthesizer proposes an answer.
    Returns a proposal for human review; use approve_or_edit_answer to confirm or request changes.
    """
    decision, proposal, search_result = run_agent_pipeline(query, top_k=top_k)
    if decision == "general_answer":
        return {
            "status": "general",
            "message": "This question is best answered without the knowledge base. Ask a specific factual question to use RAG.",
            "proposal": None,
            "search_result": None,
        }
    out: dict = {
        "status": "proposal",
        "message": "Review the proposed answer below. Use the approve_or_edit_answer tool to approve or request edits (human-in-the-loop).",
        "proposal": proposal.model_dump() if proposal else None,
        "search_result": search_result.model_dump() if search_result else None,
    }
    return out


def add_documents_tool(text: str, source: str = "user_input") -> dict:
    """Add a document (or chunk of text) to the knowledge base. Source is a label for citations."""
    doc = Document(page_content=text.strip(), metadata={"source": source})
    n = add_documents_to_knowledge_base([doc])
    return {"status": "success", "added": n, "source": source}


def search_only_tool(query: str, top_k: int = 5) -> dict:
    """Retriever-only: search the knowledge base and return chunks (no synthesis)."""
    result = search_knowledge_base(query, top_k=top_k)
    return result.model_dump()


def approve_or_edit_answer_tool(
    approved: bool,
    proposal_answer: str,
    user_feedback: str | None = None,
) -> dict:
    """
    Human-in-the-loop: approve the proposed answer or request edits.
    Call this after reviewing the output of query_knowledge_base.
    """
    if approved:
        return {
            "status": "approved",
            "final_answer": proposal_answer,
            "message": "Answer approved by user.",
        }
    return {
        "status": "edit_requested",
        "original_answer": proposal_answer,
        "user_feedback": user_feedback or "(no feedback provided)",
        "message": "User requested changes. Use the proposal and feedback to generate a revised answer.",
    }
