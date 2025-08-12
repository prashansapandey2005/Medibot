from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM
import os

# Step 1: Load Data
DATA_PATH = "data/"

def load_pdf_files(data):
    print("Loading PDF files...")
    loader = DirectoryLoader(data, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    print("PDF files loaded.")
    return documents

documents = load_pdf_files(data=DATA_PATH)
print("Length of PDF pages:", len(documents))

# Step 2: Create Chunks
def create_chunks(extracted_data):
    print("Creating text chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50
    )
    text_chunks = text_splitter.split_documents(extracted_data)
    print("Text chunks created.")
    return text_chunks

text_chunks = create_chunks(extracted_data=documents)
print("Length of Text Chunks:", len(text_chunks))

# Step 3: Create Vector Embeddings
def get_embedding_model():
    print("Getting embedding model...")
    embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    print("Embedding model loaded.")
    return embedding_model

embedding_model = get_embedding_model()

# Step 4: Store Embeddings in FAISS
DB_FAISS_PATH = "vectorstore/db_faiss"
print("Storing embeddings in FAISS...")
import time
start_time = time.time()
db = FAISS.from_documents(text_chunks, embedding_model)
db.save_local(DB_FAISS_PATH)
end_time = time.time()
print(f"Embeddings stored in FAISS at: {DB_FAISS_PATH}")
print(f"FAISS indexing time: {end_time - start_time:.2f} seconds")

print("Script execution completed.")