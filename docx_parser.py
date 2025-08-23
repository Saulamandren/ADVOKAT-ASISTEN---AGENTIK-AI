# docx_parser.py

import os
import json
import re
from docx import Document

def extract_text_from_docx(file_path):
    """Ekstrak teks dari dokumen .docx"""
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def split_to_pasals(text, sumber):
    """Pisahkan teks menjadi pasal-pasal berdasarkan pola 'Pasal xx'"""
    pattern = r'(Pasal\s+\d+[A-Z]*)(.*?)(?=Pasal\s+\d+[A-Z]*|$)'  # Tangkap semua pasal
    matches = re.findall(pattern, text, flags=re.DOTALL)
    pasals = []

    for title, content in matches:
        pasals.append({
            "judul": title.strip(),
            "isi": content.strip(),
            "sumber": sumber
        })

    return pasals

def convert_docx_to_json(docx_path, output_path):
    """Konversi satu file DOCX ke JSON"""
    sumber = os.path.basename(docx_path)
    text = extract_text_from_docx(docx_path)
    pasals = split_to_pasals(text, sumber)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(pasals, f, ensure_ascii=False, indent=2)

    print(f"✅ {sumber} → {output_path} (Total: {len(pasals)} pasal)")

def convert_all_docx_in_folder(input_folder="data", output_folder="retriever/index_store"):
    """Proses semua file .docx dalam folder 'data'"""
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".docx"):
            docx_path = os.path.join(input_folder, filename)
            json_name = os.path.splitext(filename)[0].replace(" ", "_") + ".json"
            output_path = os.path.join(output_folder, json_name)
            convert_docx_to_json(docx_path, output_path)

if __name__ == "__main__":
    convert_all_docx_in_folder()
