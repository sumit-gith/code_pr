import os
import pickle
from PyPDF2 import PdfReader

def read_pdf(pdf_path):
    text = ""
    reader = PdfReader(pdf_path)
    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

def save_pickle(data, file_path):
    with open(file_path, "wb") as f:
        pickle.dump(data, f)

def load_pickle(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)