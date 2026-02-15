"""Optional Opik observability for LLM and tool calls."""

import os
from functools import wraps

from ..config import settings


def is_opik_enabled() -> bool:
    """Return True if Opik is configured."""
    return settings.opik_api_key is not None and len(settings.opik_api_key.get_secret_value() or "") > 0


def configure_opik() -> bool:
    """Configure Opik if OPIK_API_KEY is set. Returns True if configured."""
    if not is_opik_enabled():
        return False
    try:
        import opik
        os.environ.setdefault("OPIK_PROJECT_NAME", settings.opik_project_name)
        opik.configure(
            api_key=settings.opik_api_key.get_secret_value(),
            use_local=False,
            force=True,
        )
        return True
    except Exception:
        return False


def track_tool(name: str):
    """Decorator to track a function as a tool in Opik (no-op if Opik not enabled)."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if is_opik_enabled():
                import opik
                with opik.trace(name=name, type="tool"):
                    return func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator
