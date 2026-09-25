# Architecture

## Request flow

1. A client sends a question to `POST /ask`.
2. FastAPI validates the request using the `Query` schema.
3. `RAGPipeline.query()` retrieves relevant documents from the local vector store.
4. The pipeline builds context and returns the generated answer.
5. The API returns the normalized question and answer as JSON.

## Data flow

```text
data/ -> ingestion -> embeddings/vector store -> retrieval -> context -> answer
```

## Runtime components

- **API:** FastAPI and Uvicorn.
- **Pipeline:** `app/rag_pipeline.py`.
- **Persistence:** local Chroma data under `chroma_db/`.
- **Experiments:** `app/rag_implmentation/` is kept separate from the active API path.

## Design decisions

- Generated vector-store files are excluded from source control.
- The API is started from the repository root using `uvicorn app.server:app`.
- The legacy FAISS/OpenAI implementation is not imported by the API, so its optional dependencies should not be required for the active server unless that implementation is used.
