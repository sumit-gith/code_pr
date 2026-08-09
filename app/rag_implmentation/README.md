# RAG Implementation From Scratch

A simple Retrieval-Augmented Generation (RAG) system built using:

- Python
- FAISS (facebook ai search)
- Sentence Transformers
- OpenAI API

This project demonstrates how to:
- ingest PDF documents
- create embeddings
- store vectors in FAISS
- retrieve relevant chunks
- generate contextual answers using an LLM

---

# Project Structure

```bash
app/rag_implmentation/
│
├── data/
│   ├── docs/
│   └── processed/
│
├── embeddings/
│   └── faiss_index/
│
├── src/
│   ├── embded.py
│   ├── ingest.py
│   ├── rag.py
│   ├── retreive.py
│   └── utils.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# Features

- PDF document ingestion
- Text chunking
- Embedding generation
- FAISS vector search
- Semantic retrieval
- LLM-based response generation

---

# Installation

Clone the repository:

```bash
git clone <your_repo_url>
cd app/rag_implmentation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Setup Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# Add Documents

Place PDF files inside:

```bash
data/docs/
```

Example:

```bash
data/docs/
├── ai.pdf
├── rag.pdf
└── notes.pdf
```

---

# Build Vector Database

Run ingestion script:

```bash
cd src
python ingest.py
```

This will:
- read PDFs
- chunk text
- create embeddings
- build FAISS index

---

# Run RAG Application

From project root:

```bash
python app.py
```

Example:

```text
Ask Question: What is Retrieval-Augmented Generation?
```

---

# Technologies Used

- Python
- FAISS
- Sentence Transformers
- OpenAI API
- PyPDF2

---

# Future Improvements

- Hybrid Search (BM25 + Dense Retrieval)
- Reranking
- Metadata filtering
- Streamlit UI
- FastAPI backend
- ChromaDB / Pinecone integration
- Conversation memory

---

# Notes

Recommended renaming:

```text
embded.py   -> embeddings.py
retreive.py -> retrieve.py
rag_implmentation -> rag_implementation
```

---

# License

MIT License