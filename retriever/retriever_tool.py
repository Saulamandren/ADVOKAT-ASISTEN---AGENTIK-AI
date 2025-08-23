# retriever/retriever_tool.py
import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Inisialisasi embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Dapatkan path absolut ke direktori root proyek
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Tentukan path ke direktori index_store
index_store_path = os.path.join(project_root, "retriever", "index_store")


# Fungsi retriever untuk KUHPerdata
def perdata_retriever(query: str):
    # Load vectorstore dari index_store/Perdata
    perdata_path = os.path.join(index_store_path, "Perdata")
    vectorstore = FAISS.load_local(perdata_path, embeddings, allow_dangerous_deserialization=True)
    docs = vectorstore.similarity_search(query, k=3)
    return "\n\n".join([f"Pasal: {doc.page_content}" for doc in docs])


# Fungsi retriever untuk KUHPidana
def pidana_retriever(query: str):
    # Load vectorstore dari index_store/Pidana
    pidana_path = os.path.join(index_store_path, "Pidana")
    vectorstore = FAISS.load_local(pidana_path, embeddings, allow_dangerous_deserialization=True)
    docs = vectorstore.similarity_search(query, k=3)
    return "\n\n".join([f"Pasal: {doc.page_content}" for doc in docs])