from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .rag_pipeline import RAGPipeline


app = FastAPI(
    title="Offline RAG API",
    description="Question answering over locally indexed documents.",
    version="1.0.0",
)
rag = RAGPipeline()


class Query(BaseModel):
    question: str = Field(..., min_length=3, max_length=2_000)


@app.post("/ask")
async def ask(query: Query):
    question = query.question.strip()
    if not question:
        raise HTTPException(status_code=422, detail="Question cannot be empty.")

    try:
        return {"question": question, "response": rag.query(question)}
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Failed to process the question.",
        ) from exc


@app.get("/")
async def root():
    return {"service": "offline-rag", "status": "running", "docs": "/docs"}


@app.get("/health", tags=["system"])
async def health():
    return {"status": "healthy"}