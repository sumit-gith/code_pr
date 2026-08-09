import os
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# NEW Chroma client format
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(
    name="documents",
    metadata={"hnsw:space": "cosine"}
)

def embed_text(text: str):
    return model.encode(text).tolist()

def ingest_file(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    embedding = embed_text(text)

    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[file_path]
    )

    print(f"Ingested: {file_path}")

if __name__ == "__main__":
    folder = "./data"

    if not os.path.exists(folder):
        os.makedirs(folder)
        print("⚠️ Created empty ./data folder. Add files to ingest.")
        exit()

    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        ingest_file(path)

    print("Ingestion complete.")
