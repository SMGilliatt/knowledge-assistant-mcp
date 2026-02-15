"""Server configuration settings."""

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings for the Knowledge Assistant MCP Server."""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        env_file_encoding="utf-8",
    )

    # Server
    server_name: str = Field(
        default="Knowledge Assistant MCP Server",
        description="Name of the MCP server",
    )
    version: str = Field(default="0.1.0", description="Server version")

    # LLM
    model_name: str = Field(
        default="gemini-2.0-flash",
        alias="MODEL_NAME",
        description="LLM model for coordinator and synthesizer",
    )
    google_api_key: SecretStr | None = Field(
        default=None,
        alias="GOOGLE_API_KEY",
        description="Google AI (Gemini) API key",
    )

    # RAG / Chroma
    chroma_persist_dir: str = Field(
        default="./chroma_data",
        alias="CHROMA_PERSIST_DIR",
        description="Directory for ChromaDB persistence",
    )
    chroma_collection_name: str = Field(
        default="knowledge_base",
        alias="CHROMA_COLLECTION",
        description="ChromaDB collection name",
    )
    rag_top_k: int = Field(
        default=5,
        alias="RAG_TOP_K",
        description="Number of chunks to retrieve",
    )
    embedding_model: str = Field(
        default="models/gemini-embedding-001",
        alias="EMBEDDING_MODEL",
        description="Google embedding model for RAG (e.g. models/gemini-embedding-001)",
    )

    # Opik (optional)
    opik_api_key: SecretStr | None = Field(
        default=None,
        alias="OPIK_API_KEY",
        description="Opik API key for observability",
    )
    opik_project_name: str = Field(
        default="knowledge-assistant",
        alias="OPIK_PROJECT_NAME",
        description="Opik project name",
    )


settings = Settings()
