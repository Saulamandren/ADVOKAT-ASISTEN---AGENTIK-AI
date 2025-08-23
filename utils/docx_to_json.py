from docx import Document
import re
import json
import os

DATA_FOLDER = "data"
OUTPUT_FOLDER = "retriever/index_store"

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = []

    for para in doc.paragraphs:
        content = para.text.strip()
        if content:
            # Tambahkan newline sebelum setiap "Pasal X"
            content = re.sub(r'(?<!\n)(Pasal\s+\d+[A-Z]*)', r'\n\1', content)
            text.append(content)

    return '\n'.join(text)

def split_to_pasals(text, sumber):
    raw_pasals = re.split(r'\n?Pasal\s+(\d+[A-Z]*)\n', text)
    pasals = []

    for i in range(1, len(raw_pasals), 2):
        nomor = raw_pasals[i].strip()
        isi = raw_pasals[i + 1].strip()
        pasals.append({
            "judul": f"Pasal {nomor}",
            "isi": isi,
            "sumber": sumber
        })

    return pasals

def convert_docx_to_json(docx_path, json_output_path):
    text = extract_text_from_docx(docx_path)
    pasals = split_to_pasals(text, os.path.basename(docx_path))

    os.makedirs(os.path.dirname(json_output_path), exist_ok=True)

    with open(json_output_path, "w", encoding="utf-8") as f:
        json.dump(pasals, f, ensure_ascii=False, indent=2)

    print(f"✅ {len(pasals)} pasal berhasil disimpan ke: {json_output_path}")


# === EKSEKUSI UNTUK SEMUA FILE DI FOLDER ===
if __name__ == "__main__":
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".docx"):
            input_path = os.path.join(DATA_FOLDER, filename)
            name_without_ext = os.path.splitext(filename)[0]
            output_path = os.path.join(OUTPUT_FOLDER, f"{name_without_ext}.json")
            
            print(f"🔄 Memproses: {filename}")
            convert_docx_to_json(input_path, output_path)
