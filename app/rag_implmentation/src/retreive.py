import faiss
import numpy as np

from embded import EmbeddingModel
from utils import load_pickle

INDEX_PATH = "../embeddings/faiss_index/index.faiss"
META_PATH = "../embeddings/faiss_index/metadata.pkl"

class Retriever:
    def __init__(self):
        self.index = faiss.read_index(INDEX_PATH)
        self.documents = load_pickle(META_PATH)
        self.embedder = EmbeddingModel()

    def search(self, query, top_k=3):
        query_embedding = self.embedder.encode([query])
        query_embedding = np.array(
            query_embedding
        ).astype("float32")
        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:
            results.append(self.documents[idx])

        return results