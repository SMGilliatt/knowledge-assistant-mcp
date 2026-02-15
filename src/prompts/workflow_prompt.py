"""Workflow prompt: multi-agent RAG with human-in-the-loop."""

KNOWLEDGE_ASSISTANT_WORKFLOW = """# Knowledge Assistant Workflow (Multi-Agent + Human-in-the-Loop)

This workflow uses multiple agents and requires your approval before finalizing.

## Step 1: Ask a question
Use the **query_knowledge_base** tool with your question. Example:
- query_knowledge_base(query="What is our refund policy?")
- query_knowledge_base(query="How do I reset my password?", top_k=5)

The system will:
1. **Coordinator agent**: Decide whether to answer from the knowledge base or respond generally.
2. **Retriever agent**: Search the RAG vector store for relevant chunks.
3. **Synthesizer agent**: Propose an answer with citations and confidence.

## Step 2: Review the proposal (REQUIRED – human-in-the-loop)
You will receive a **proposed answer** and optional **search_result** (retrieved chunks). Review them.

## Step 3: Approve or request edits
Use the **approve_or_edit_answer** tool to complete the workflow:

- **To approve**: approve_or_edit_answer(approved=True, proposal_answer="<paste the proposed answer here>")
- **To request changes**: approve_or_edit_answer(approved=False, proposal_answer="<proposed answer>", user_feedback="<your edit instructions>")

This step is required: the system does not finalize the answer until you approve or provide feedback.

## Optional: Add documents
To add content to the knowledge base, use **add_documents**(text="...", source="optional_label").

## Summary
1. query_knowledge_base(question) → get proposal
2. Review proposal
3. approve_or_edit_answer(approved=..., proposal_answer=..., user_feedback=...) → finalize
"""
