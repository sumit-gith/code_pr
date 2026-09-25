from .retreiver import retrieve_relevant_docs
from sentence_transformers import SentenceTransformer
import nltk


nltk.download('punkt', quiet=True)
model = SentenceTransformer("all-MiniLM-L6-v2")


class RAGPipeline:
    def __init__(self):
        pass


    def query(self, question: str):
        docs = retrieve_relevant_docs(question)
        if not docs:
            return "No relevant documents found."


        context = "\n".join(docs)


# Offline simple answer: return context + echo question
        return f"Context:\n{context}\n\nAnswer (simple offline): {question} relates to above documents."