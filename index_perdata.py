from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
import os

# Lokasi file KUHPerdata (format JSON)
DATA_FILE = "data/kuhperdata.json"
DB_PATH = "db/perdata_faiss"

# Muat data JSON KUHPerdata
with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Gabungkan semua pasal
documents = []
for pasal in data:
    content = f"Pasal {pasal['pasal']}: {pasal['isi']}"
    documents.append(content)

# Split teks menjadi chunk
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.create_documents(documents)

# Buat embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Simpan ke FAISS
vectorstore = FAISS.from_documents(docs, embeddings)
vectorstore.save_local(DB_PATH)

print(f"✅ Indexing selesai! Disimpan di {DB_PATH}")
