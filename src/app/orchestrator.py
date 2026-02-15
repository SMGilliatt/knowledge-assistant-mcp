"""Multi-agent orchestration: coordinator, retriever, synthesizer."""

from ..models.schemas import AnswerProposal, SearchResult

from .llm import coordinator_decide, synthesize_answer
from .rag import search_knowledge_base


def run_agent_pipeline(query: str, top_k: int | None = None) -> tuple[str, AnswerProposal | None, SearchResult | None]:
    """
    Run coordinator -> retriever -> synthesizer.

    Returns:
        (decision, answer_proposal_or_none, search_result_or_none)
        - If decision is "general_answer", proposal and search_result are None.
        - If "answer_from_kb", proposal and search_result are set.
    """
    decision = coordinator_decide(query)
    if decision == "general_answer":
        return "general_answer", None, None

    search_result = search_knowledge_base(query, top_k=top_k)
    if not search_result.chunks:
        proposal = AnswerProposal(
            answer="No relevant documents found in the knowledge base for this query.",
            citations=[],
            confidence="low",
        )
        return "answer_from_kb", proposal, search_result

    context_chunks = [c.content for c in search_result.chunks]
    citations = [c.source for c in search_result.chunks]
    proposal = synthesize_answer(query, context_chunks, citations)
    return "answer_from_kb", proposal, search_result
