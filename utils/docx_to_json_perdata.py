import json
import re
from docx import Document
import os

# Path file input dan output
input_path = os.path.join("data", "Perdata.docx")
output_path = os.path.join("retriever", "index_store", "Perdata.json")

def docx_to_json(docx_path, json_path):
    doc = Document(docx_path)
    data = []
    current_pasal = None
    current_text = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue

        # Deteksi awal pasal
        match = re.match(r"^Pasal\s+\d+", text, re.IGNORECASE)
        if match:
            if current_pasal and current_text:
                data.append({
                    "dokumen": "KUHPerdata",
                    "pasal": current_pasal,
                    "isi": " ".join(current_text).strip()
                })
                current_text = []
            current_pasal = match.group(0)
        else:
            current_text.append(text)

    if current_pasal and current_text:
        data.append({
            "dokumen": "KUHPerdata",
            "pasal": current_pasal,
            "isi": " ".join(current_text).strip()
        })

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[✔] KUHPerdata berhasil dikonversi ke {json_path}")

if __name__ == "__main__":
    docx_to_json(input_path, output_path)
