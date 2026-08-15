from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import RAGPipeline


app = FastAPI()
rag = RAGPipeline()


class Query(BaseModel):
    question: str


@app.post("/ask")
async def ask(query: Query):
    return {"response": rag.query(query.question)}


@app.get("/")
async def root():
    return {"message": "Offline RAG server running!"}