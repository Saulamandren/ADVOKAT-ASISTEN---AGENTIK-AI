from langchain_core.output_parsers import BaseOutputParser

class PerdataOutputParser(BaseOutputParser):
    def parse(self, text: str) -> str:
        # Hapus whitespace berlebihan
        cleaned = text.strip()

        # Terjemahan atau post-processing jika perlu
        cleaned = cleaned.replace("legal remedies", "upaya hukum")
        cleaned = cleaned.replace("filing a lawsuit", "mengajukan gugatan")
        cleaned = cleaned.replace("Wahyu has breached his obligation", "Wahyu telah melanggar kewajibannya")

        return cleaned
