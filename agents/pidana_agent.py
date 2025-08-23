# agents/pidana_agent.py

from langchain_ollama.llms import OllamaLLM
from retriever.retriever_tool import pidana_retriever
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

# 1. Gunakan LLM
llm = OllamaLLM(model="llama3:instruct")

# 2. Definisikan Prompt Template yang Jelas
prompt_template = """
Anda adalah seorang Advokat AI, ahli Hukum Pidana di Indonesia.
Tugas Anda adalah menganalisis kasus hukum berdasarkan pasal-pasal KUHP yang relevan.

**KONTEKS PASAL HUKUM:**
{context}

**KASUS DARI PENGGUNA:**
{question}

**INSTRUKSI:**
1.  Berdasarkan **KONTEKS PASAL HUKUM** di atas, berikan analisis hukum yang tajam dan jelas untuk **KASUS DARI PENGGUNA**.
2.  Sebutkan pasal-pasal yang menjadi dasar analisis Anda.
3.  Jika konteks tidak memberikan informasi yang cukup, jelaskan bahwa informasi tidak ditemukan dalam dokumen yang tersedia.
4.  Gunakan Bahasa Indonesia yang formal, baku, dan sesuai kaidah hukum.
5.  Struktur jawaban Anda dalam format berikut:
    - **Dasar Hukum:** (Sebutkan pasal-pasal yang relevan)
    - **Analisis Hukum:** (Jelaskan analisis Anda secara rinci)
    - **Kesimpulan:** (Berikan kesimpulan atau langkah hukum yang disarankan)

**HASIL ANALISIS ANDA:**
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"],
)

# 3. Buat Rantai (Chain) Analisis Pidana
#    Chain ini siap untuk diimpor dan digunakan oleh agen router utama.
pidana_chain = (
    {"context": RunnableLambda(lambda x: pidana_retriever(x['question'])), "question": RunnablePassthrough()}
    | prompt
    | llm
)
