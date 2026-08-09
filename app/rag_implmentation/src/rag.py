from openai import OpenAI
from retreive import Retriever
import os

class RAG:
    def __init__(self):
        self.retriever = Retriever()
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def ask(self, query):
        contexts = self.retriever.search(query)
        context_text = "\n\n".join(contexts)
        prompt = f"""
You are a helpful assistant.

Use the following context to answer the question.

Context:
{context_text}

Question:
{query}
"""
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content