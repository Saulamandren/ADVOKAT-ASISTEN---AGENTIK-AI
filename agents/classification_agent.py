# agents/classification_agent.py

from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

# 1. Inisialisasi LLM
llm = OllamaLLM(model="llama3:instruct")

# 2. Buat Prompt Template untuk Klasifikasi
#    Prompt ini sangat spesifik dan menginstruksikan LLM untuk hanya mengeluarkan satu kata.
classification_template = """
Anda adalah seorang ahli hukum yang bertugas mengklasifikasikan sebuah kasus ke dalam kategori Hukum Perdata atau Hukum Pidana.
Balas HANYA dengan satu kata: 'perdata' atau 'pidana'. Jangan memberikan penjelasan atau kalimat lain.

- **Hukum Perdata**: Fokus pada sengketa antar individu, seperti perjanjian, utang-piutang, ganti rugi, warisan, sengketa tanah, atau perceraian.
- **Hukum Pidana**: Fokus pada tindakan yang melanggar hukum publik dan diancam sanksi oleh negara, seperti pencurian, penipuan, penganiayaan, pembunuhan, atau korupsi.

Kasus yang perlu diklasifikasikan:
"{question}"

Klasifikasi (hanya satu kata):
"""

classification_prompt = PromptTemplate(
    template=classification_template,
    input_variables=["question"],
)

# 3. Buat Chain untuk Klasifikasi
#    Chain ini akan mengambil pertanyaan, memasukkannya ke dalam prompt, dan LLM akan menghasilkan klasifikasi.
classification_chain = (
    classification_prompt
    | llm
)

if __name__ == "__main__":
    # Contoh pengujian cepat
    test_case_perdata = "Seseorang tidak membayar utangnya sesuai perjanjian."
    test_case_pidana = "Seseorang mengambil dompet orang lain di bus."
    
    print("Menguji kasus perdata...")
    result_perdata = classification_chain.invoke({"question": test_case_perdata})
    print(f"Hasil: {result_perdata}")

    print("\nMenguji kasus pidana...")
    result_pidana = classification_chain.invoke({"question": test_case_pidana})
    print(f"Hasil: {result_pidana}")