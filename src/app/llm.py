"""LLM utilities for coordinator and synthesizer agents."""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from ..config import settings
from ..models.schemas import AnswerProposal


def get_llm():
    """Return Chat model (Gemini). Requires GOOGLE_API_KEY."""
    api_key = settings.google_api_key.get_secret_value() if settings.google_api_key else None
    return ChatGoogleGenerativeAI(
        model=settings.model_name,
        google_api_key=api_key,
        temperature=0.3,
    )


def synthesize_answer(query: str, context_chunks: list[str], citations: list[str]) -> AnswerProposal:
    """Synthesizer agent: produce an answer from retrieved context (structured output)."""
    llm = get_llm().with_structured_output(AnswerProposal)
    context = "\n\n---\n\n".join(context_chunks)
    prompt = f"""You are a precise assistant. Answer the user's question using ONLY the provided context. If the context does not contain enough information, say so and give a short answer.

Context:
{context}

User question: {query}

Provide your answer with citations (refer to the sources above) and set confidence to low/medium/high based on how well the context supports your answer."""
    result = llm.invoke([HumanMessage(content=prompt)])
    # Ensure citations list matches our sources
    if not result.citations and citations:
        result.citations = citations[:3]
    return result


def coordinator_decide(query: str) -> str:
    """Coordinator agent: decide action - 'answer_from_kb' or 'general_answer'."""
    llm = get_llm()
    prompt = f"""You are a coordinator. Given the user question, decide the best action.
- "answer_from_kb": the question should be answered using the knowledge base (factual, specific, or domain questions).
- "general_answer": the question is greeting, thanks, or not about the knowledge base.

User question: {query}

Reply with exactly one word: answer_from_kb or general_answer"""
    msg = llm.invoke([HumanMessage(content=prompt)])
    content = (msg.content or "").strip().lower()
    if "general_answer" in content:
        return "general_answer"
    return "answer_from_kb"
