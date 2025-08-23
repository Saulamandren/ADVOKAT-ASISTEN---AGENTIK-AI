# retriever/index_builder.py

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def build_index(doc_path, index_path):
    loader = Docx2txtLoader(doc_path)
    documents = loader.load()

    # Split dokumen menjadi chunk
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = splitter.split_documents(documents)

    # Embedding
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Bangun vectorstore
    vectorstore = FAISS.from_documents(split_docs, embeddings)

    # Simpan index
    vectorstore.save_local(index_path)
    print(f"✅ Index berhasil disimpan di: {index_path}")

if __name__ == "__main__":
    os.makedirs("retriever/index_store", exist_ok=True)

    # Bangun index untuk KUHPerdata
    build_index("data/Perdata.docx", "retriever/index_store/Perdata")

    # Bangun index untuk Pidana
    build_index("data/Pidana.docx", "retriever/index_store/Pidana")
