# Offline RAG API

A local Retrieval-Augmented Generation (RAG) project for asking questions over indexed documents. The project exposes a FastAPI endpoint and keeps the vector database on the local machine.

## Current architecture

- `app/server.py` — FastAPI application with `/`, `/health`, and `/ask` endpoints.
- `app/rag_pipeline.py` — active RAG pipeline used by the API.
- `app/ingest.py` — document ingestion entry point.
- `app/retreiver.py` — current retrieval implementation (the filename is kept for compatibility; prefer `retriever.py` for future code).
- `app/rag_implmentation/` — experimental/legacy FAISS and OpenAI implementation.
- `chroma_db/` — generated local vector-store data; do not commit it.
- `data/` — local source documents.

## Setup

```bash
cd /Users/sumit/code_pr
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If you already have the virtual environment, activate it instead:

```bash
source venv/bin/activate
```

## Run the API

Run from the repository root, not from `app/`:

```bash
uvicorn app.server:app --reload
```

Endpoints:

- `GET http://127.0.0.1:8000/`
- `GET http://127.0.0.1:8000/health`
- Swagger UI: `http://127.0.0.1:8000/docs`
- `POST http://127.0.0.1:8000/ask`

Example request:

```bash
curl -X POST http://127.0.0.1:8000/ask \
  -H 'Content-Type: application/json' \
  -d '{"question":"What is this document about?"}'
```

## Ingestion

Use the existing ingestion script after placing documents in the expected `data/` location:

```bash
python -m app.ingest
```

Review `app/ingest.py` before changing the input path or database settings. Existing `chroma_db/` data is generated state and can be rebuilt when required.

## Testing and checks

```bash
python -m pytest
python -m compileall app
```

The API creates the RAG pipeline at import time. If startup fails, verify that the local model and vector-store dependencies are installed and that the required model/data files exist.

## Known limitations

- The project currently contains an active implementation and a separate experimental implementation under `app/rag_implmentation/`.
- The legacy implementation requires optional FAISS, OpenAI, and PDF dependencies and is not used by the FastAPI server.
- Retrieval quality is not yet benchmarked. A useful next step is adding a small evaluation set with expected answers and retrieval metrics.
- Local model downloads may require network access on first run.

## Suggested resume bullet

> Built a local Retrieval-Augmented Generation API with document ingestion, vector retrieval, local persistence, FastAPI endpoints, health checks, and reproducible Python tooling.
