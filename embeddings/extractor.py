from pathlib import Path
from pypdf import PdfReader
from docx import Document as DocxDocument


class DocumentExtractor:

    @staticmethod
    def extract(file_path: str) -> str:
        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return DocumentExtractor._extract_pdf(file_path)

        if extension == ".docx":
            return DocumentExtractor._extract_docx(file_path)

        if extension == ".txt":
            return Path(file_path).read_text(encoding="utf-8")

        raise ValueError("Unsupported file type")

    @staticmethod
    def _extract_pdf(file_path):
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    @staticmethod
    def _extract_docx(file_path):
        doc = DocxDocument(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )