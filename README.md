# ADVOKAT-ASISTEN---AGENTIK-AI



 # Asisten Advokat AI ⚖️

**Sebuah Aplikasi Web Berbasis Agentik-AI untuk Analisis Awal Kasus Hukum di Indonesia**

Proyek ini adalah sebuah aplikasi berbasis web yang berfungsi sebagai asisten virtual untuk advokat, mahasiswa hukum, atau masyarakat umum. Aplikasi ini memanfaatkan arsitektur *Agentik AI* untuk menganalisis deskripsi kasus hukum (kasus posisi) dan memberikan ringkasan, analisis hukum, serta pasal-pasal yang relevan dari peraturan perundang-undangan di Indonesia.

[Demo Aplikasi Asisten Advokat AI]
<img width="1916" height="968" alt="image" src="https://github.com/user-attachments/assets/9677f8f9-fd2b-4bdd-ab3a-98eeb9416b04" />

---

## ✨ Fitur Utama

- **Analisis Kasus Otomatis**: Cukup masukkan deskripsi kasus (kasus posisi), dan AI akan menganalisisnya.
- **Klasifikasi Otomatis**: Sistem secara otomatis mengidentifikasi ranah hukum kasus (Perdata atau Pidana).
- **Pendekatan Agentik**: Menggunakan agen AI spesialis untuk setiap ranah hukum guna memastikan analisis yang relevan dan mendalam.
- **Referensi Pasal Hukum Akurat**: Hasil analisis didukung oleh pasal-pasal yang diambil dari basis data hukum internal menggunakan teknologi RAG (Retrieval-Augmented Generation).
- **Antarmuka Sederhana**: Dibangun dengan Streamlit untuk kemudahan penggunaan.

---

## ⚙️ Bagaimana Program Ini Bekerja (Alur Kerja Detail)

Program ini adalah aplikasi web berbasis AI yang berfungsi sebagai asisten hukum. Alur kerjanya dapat dipecah menjadi beberapa langkah utama, dari input pengguna hingga output analisis:

1.  **Antarmuka Pengguna (UI)**: Pengguna membuka aplikasi melalui browser. Tampilan yang dibuat dengan Streamlit (`app.py`) menyajikan sebuah kotak teks di mana pengguna dapat memasukkan deskripsi kasus hukum mereka.
2.  **Klasifikasi Kasus (Langkah 1)**:
    * Setelah pengguna menekan tombol "Analisis Kasus", teks deskripsi dikirim ke **Agen Klasifikasi** (`agents/classification_agent.py`).
    * Agen ini menggunakan Model Bahasa (LLM) yang telah diinstruksikan secara spesifik (melalui prompt) untuk menganalisis teks dan mengklasifikasikannya sebagai kasus "Perdata" atau "Pidana".
    * Hasil klasifikasi (misalnya, "perdata") ditampilkan kepada pengguna.
3.  **Pemilihan Agen Spesialis (Langkah 2)**:
    * Berdasarkan hasil klasifikasi, program secara cerdas memilih agen yang tepat untuk menangani analisis mendalam.
    * Jika hasilnya "perdata", maka **Agen Perdata** (`agents/perdata_agent.py`) akan diaktifkan.
    * Jika hasilnya "pidana", maka **Agen Pidana** (`agents/pidana_agent.py`) yang akan digunakan.
4.  **Retrieval-Augmented Generation (RAG)**:
    * Ini adalah inti dari kemampuan analisis aplikasi. Sebelum menghasilkan jawaban, agen spesialis (Perdata/Pidana) akan mencari informasi yang relevan terlebih dahulu.
    * Agen menggunakan **Retriever Tool** (`retriever/retriever_tool.py`) untuk mencari pasal-pasal atau dokumen hukum yang paling relevan dengan deskripsi kasus pengguna.
    * Pencarian ini dilakukan pada sebuah database vektor (**FAISS Index** di `retriever/index_store/`) yang sudah berisi "pengetahuan" dari dokumen hukum seperti KUHPerdata dan KUHPidana. Dokumen-dokumen ini sebelumnya telah diproses dan diubah menjadi format numerik (vektor) agar bisa dicari dengan cepat.

5.  **Analisis dan Penyusunan Jawaban (Langkah 3)**:
    * Agen spesialis (Perdata/Pidana) menerima dua jenis informasi: (1) deskripsi kasus dari pengguna dan (2) pasal-pasal relevan yang ditemukan oleh Retriever.
    * Dengan kedua informasi ini, agen mengirimkannya ke LLM dengan instruksi (prompt) untuk menyusun analisis hukum yang koheren, menjelaskan pasal yang berlaku, dan memberikan pandangan awal terhadap kasus tersebut.
    * Proses ini memastikan jawaban yang diberikan tidak hanya berdasarkan pengetahuan umum LLM, tetapi juga didasarkan pada konteks hukum yang relevan dari dokumen yang Anda sediakan.

6.  **Menampilkan Hasil**:
    * Analisis akhir yang sudah jadi kemudian dikirim kembali ke antarmuka Streamlit dan ditampilkan kepada pengguna dalam format yang rapi dan mudah dibaca.
---

## 🛠️ Teknologi yang Digunakan

Berikut adalah teknologi spesifik yang menyusun aplikasi ini:

* **Bahasa Pemrograman**: Python
* **Framework Aplikasi Web**: Streamlit (untuk membuat antarmuka pengguna interaktif dengan cepat).
* **Orkestrasi AI/LLM**: LangChain (framework untuk membangun aplikasi yang ditenagai oleh LLM. Ini digunakan untuk membuat "rantai" atau chain yang menghubungkan prompt, model, dan output parser, serta mengelola agen).
* **Pencarian Vektor (Vector Search)**: FAISS (Facebook AI Similarity Search) (digunakan untuk membuat database vektor dari dokumen hukum. Ini memungkinkan pencarian berbasis kemiripan makna yang sangat cepat dan efisien).
* **Model Bahasa (LLM)**: Kode tidak secara spesifik menyebutkan modelnya (misalnya GPT-4, Gemini, dll.), karena LangChain bersifat fleksibel. Model ini dikonfigurasi melalui API Key yang diatur di lingkungan sistem Anda (misalnya `OPENAI_API_KEY`).
* **Pengolahan Dokumen**: `python-docx` (untuk membaca file `.docx` seperti `Perdata.docx` dan `Pidana.docx`) dan `JSON` (untuk menyimpan data terstruktur).

---

## 🚀 Instalasi dan Cara Menjalankan

Berikut langkah-langkah untuk menginstal dan menjalankan proyek ini di komputer Anda:

1.  **Prasyarat**:
    * Pastikan Python (versi 3.9 atau lebih baru) sudah terinstal.
    * Anda memerlukan `pip` (Python package installer), yang biasanya sudah terpasang bersama Python.

2.  **Clone Repositori**
    ```bash
    git clone [https://github.com/NAMA_PENGGUNA_ANDA/NAMA_REPOSITORI_ANDA.git](https://github.com/NAMA_PENGGUNA_ANDA/NAMA_REPOSITORI_ANDA.git)
    cd NAMA_REPOSITORI_ANDA
    ```

3.  **Instalasi Dependensi**:
    * Buka terminal atau Command Prompt.
    * Arahkan ke direktori utama proyek Anda.
    * Jalankan perintah berikut untuk menginstal semua pustaka Python yang diperlukan dari file `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```


4.  **Menjalankan Aplikasi**:
    * Pastikan Anda masih berada di direktori utama proyek di terminal Anda.
    * Jalankan aplikasi Streamlit dengan perintah berikut:
    ```bash
    streamlit run app.py
    ```
    * Setelah perintah dieksekusi, terminal akan menampilkan URL lokal (biasanya `http://localhost:8501`). Buka URL tersebut di browser web Anda untuk mulai menggunakan aplikasi.

<img width="1470" height="498" alt="image" src="https://github.com/user-attachments/assets/69c20ba9-15d0-4928-a0d2-dde117157db2" />
<img width="1592" height="391" alt="image" src="https://github.com/user-attachments/assets/4b769781-5d6b-4179-a5e2-f2416613b9fc" />
<img width="1532" height="198" alt="image" src="https://github.com/user-attachments/assets/9c0ef8e3-dff3-4411-bfa6-cf05c6e57b97" />
<img width="1485" height="132" alt="image" src="https://github.com/user-attachments/assets/1e745767-3ca5-4e3d-bd75-b15cbb7bc5cf" />
<img width="1514" height="795" alt="image" src="https://github.com/user-attachments/assets/190bf828-f0b9-48f4-8b4a-ca0164874fd0" />



**(Opsional) Jika Anda Mengubah Dokumen Hukum**:
Indeks FAISS di `retriever/index_store/` sudah dibuat sebelumnya. Jika Anda mengubah atau menambah file `Perdata.docx` atau `Pidana.docx`, Anda perlu membuat ulang indeks tersebut dengan menjalankan skrip yang relevan (misalnya `index_perdata.py` atau skrip lain yang berfungsi untuk membangun indeks).

---

## @Saulamandren 2025










