"""RAG: ChromaDB vector store and retrieval."""

from pathlib import Path

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

from ..config import settings
from ..models.schemas import RetrievedChunk, SearchResult


def get_embedding_model():
    """Return embedding model (Google). Requires GOOGLE_API_KEY."""
    return GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",  # or "gemini-embedding-001" depending on API
        google_api_key=settings.google_api_key.get_secret_value() if settings.google_api_key else None,
    )


def get_vector_store():
    """Create or load Chroma vector store with persistence."""
    persist_dir = Path(settings.chroma_persist_dir)
    persist_dir.mkdir(parents=True, exist_ok=True)
    embeddings = get_embedding_model()
    return Chroma(
        collection_name=settings.chroma_collection_name,
        embedding_function=embeddings,
        persist_directory=str(persist_dir),
    )


def search_knowledge_base(query: str, top_k: int | None = None) -> SearchResult:
    """Retrieve relevant chunks from the knowledge base (retriever agent)."""
    vs = get_vector_store()
    k = top_k or settings.rag_top_k
    try:
        results = vs.similarity_search_with_score(query, k=k)
    except Exception:
        results = []
    chunks = [
        RetrievedChunk(
            content=doc.page_content,
            source=doc.metadata.get("source", "unknown"),
            score=1.0 - score if score <= 1.0 else 1.0 / (1.0 + score),
        )
        for doc, score in results
    ]
    return SearchResult(query=query, chunks=chunks, total=len(chunks))


def add_documents_to_knowledge_base(documents: list[Document]) -> int:
    """Add documents to the vector store. Returns count added."""
    if not documents:
        return 0
    vs = get_vector_store()
    ids = vs.add_documents(documents)
    return len(ids)
