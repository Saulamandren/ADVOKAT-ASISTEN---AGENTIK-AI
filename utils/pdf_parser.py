from pdfminer.high_level import extract_text
import json
import re
import os

def extract_text_from_pdf(file_path):
    return extract_text(file_path)

def split_to_pasals(text, sumber):
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

def convert_pdf_to_json(pdf_path, output_path):
    sumber = os.path.basename(pdf_path)
    text = extract_text_from_pdf(pdf_path)
    pasals = split_to_pasals(text, sumber)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(pasals, f, ensure_ascii=False, indent=2)

    print(f"✅ Berhasil disimpan ke: {output_path} (Total: {len(pasals)} pasal)")

if __name__ == "__main__":
    convert_pdf_to_json("data/KUHP.pdf", "retriever/index_store/pasal_terstruktur.json")
