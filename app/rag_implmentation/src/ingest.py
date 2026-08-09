import os
import faiss
import numpy as np

from utils import read_pdf, chunk_text, save_pickle
from embded import EmbeddingModel

DOCS_PATH = "../data/docs"
INDEX_PATH = "../embeddings/faiss_index/index.faiss"
META_PATH = "../embeddings/faiss_index/metadata.pkl"

def load_documents():
    documents = []
    for file in os.listdir(DOCS_PATH):
        path = os.path.join(DOCS_PATH, file)
        if file.endswith(".pdf"):
            text = read_pdf(path)
            chunks = chunk_text(text)
            documents.extend(chunks)

    return documents

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index

def main():
    print("Loading documents...")
    docs = load_documents()
    print(f"Loaded {len(docs)} chunks")
    embedder = EmbeddingModel()
    print("Creating embeddings...")
    embeddings = embedder.encode(docs)
    embeddings = np.array(embeddings).astype("float32")
    print("Building FAISS index...")
    index = create_faiss_index(embeddings)
    faiss.write_index(index, INDEX_PATH)
    save_pickle(docs, META_PATH)
    print("Ingestion completed!")

if __name__ == "__main__":
    main()