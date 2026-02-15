"""Structured outputs (Pydantic) for agent responses."""

from pydantic import BaseModel, Field


class RetrievedChunk(BaseModel):
    """A single chunk retrieved from the knowledge base."""

    content: str = Field(description="Text content of the chunk")
    source: str = Field(description="Source document or identifier")
    score: float = Field(description="Relevance score 0-1")


class SearchResult(BaseModel):
    """Result of a RAG search over the knowledge base."""

    query: str = Field(description="The search query")
    chunks: list[RetrievedChunk] = Field(description="Retrieved chunks")
    total: int = Field(description="Number of chunks returned")


class AnswerProposal(BaseModel):
    """Proposed answer from the synthesizer (before user approval)."""

    answer: str = Field(description="The proposed answer text")
    citations: list[str] = Field(default_factory=list, description="Source references")
    confidence: str = Field(
        default="medium",
        description="One of: low, medium, high",
    )


class SynthesisResult(BaseModel):
    """Final synthesis result (after optional user approval)."""

    answer: str = Field(description="The final answer text")
    citations: list[str] = Field(default_factory=list, description="Source references")
    approved_by_user: bool = Field(
        default=False,
        description="Whether the user approved the proposal",
    )
