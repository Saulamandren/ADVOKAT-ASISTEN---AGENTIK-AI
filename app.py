# app.py

import streamlit as st
import sys
import os

# Tambahkan direktori root ke sys.path untuk impor yang benar
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.classification_agent import classification_chain
from agents.perdata_agent import perdata_chain
from agents.pidana_agent import pidana_chain

def main_app():
    st.set_page_config(page_title="Advokat AI Terpadu", page_icon="⚖️", layout="wide")

    st.title("⚖️ Advokat AI Terpadu")
    st.caption("Ditenagai oleh Model Bahasa untuk Analisis Hukum Indonesia")

    st.sidebar.header("Tentang Aplikasi")
    st.sidebar.info(
        "**Advokat AI** adalah sistem cerdas yang membantu menganalisis dan mengklasifikasikan "
        "kasus hukum di Indonesia. Masukkan deskripsi kasus Anda, dan AI akan menentukan "
        "apakah kasus tersebut termasuk dalam ranah **hukum perdata** atau **hukum pidana**, "
        "lalu memberikan analisis awal berdasarkan peraturan yang relevan."
    )
    st.sidebar.warning("⚠️ **Disclaimer:** Analisis ini adalah hasil dari AI dan tidak dapat menggantikan nasihat hukum profesional. Selalu konsultasikan dengan advokat terkualifikasi untuk masalah hukum Anda.")

    query = st.text_area("Silakan masukkan deskripsi lengkap kasus Anda di sini:", height=150, placeholder="Contoh: Seseorang meminjam uang saya dan tidak mau mengembalikannya meskipun sudah jatuh tempo...")

    if st.button("Analisis Kasus", use_container_width=True):
        if not query.strip():
            st.error("❌ Input tidak boleh kosong. Harap masukkan deskripsi kasus Anda.")
        else:
            with st.spinner("Menganalisis kasus Anda... Harap tunggu sejenak."):
                try:
                    # --- Langkah 1: Klasifikasi Kasus ---
                    st.subheader("Langkah 1: Klasifikasi Jenis Kasus")
                    with st.status("Menganalisis dan mengklasifikasikan...", expanded=True) as status:
                        classification_result = classification_chain.invoke({"question": query}).strip().lower()
                        st.write(f"**Hasil Klasifikasi:** Kasus Anda teridentifikasi sebagai **{classification_result.capitalize()}**.")
                        status.update(label="Klasifikasi Selesai!", state="complete")

                    # --- Langkah 2: Rute ke Agen yang Sesuai ---
                    st.subheader("Langkah 2: Memilih Advokat AI yang Tepat")
                    analysis_chain = None
                    if 'perdata' in classification_result:
                        analysis_chain = perdata_chain
                        st.info("🤖 Kasus Anda akan ditangani oleh **Advokat AI Hukum Perdata**.")
                    elif 'pidana' in classification_result:
                        analysis_chain = pidana_chain
                        st.info("🤖 Kasus Anda akan ditangani oleh **Advokat AI Hukum Pidana**.")
                    else:
                        st.error(f"❌ Tidak dapat menentukan jenis kasus dari klasifikasi: '{classification_result}'. Coba jelaskan kasus Anda dengan lebih detail.")
                        st.stop()
                    
                    # --- Langkah 3: Dapatkan Analisis Akhir ---
                    st.subheader("Langkah 3: Analisis Hukum dan Pasal Terkait")
                    with st.spinner("Mencari pasal dan menyusun analisis hukum..."):
                        final_result = analysis_chain.invoke({"question": query})
                    
                    st.success("Analisis Hukum Berhasil Disusun!")
                    st.markdown("---")
                    
                    with st.expander("Lihat Hasil Analisis Hukum Lengkap", expanded=True):
                        st.markdown(final_result)

                except Exception as e:
                    st.error(f"Terjadi kesalahan teknis: {e}")
                    st.error("Harap coba lagi atau ubah deskripsi kasus Anda. Jika masalah berlanjut, hubungi administrator.")

if __name__ == "__main__":
    main_app()