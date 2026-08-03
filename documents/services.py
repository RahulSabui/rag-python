from pathlib import Path

from .models import Document


class DocumentService:

    @staticmethod
    def detect_file_type(filename):

        extension = Path(filename).suffix.lower()

        if extension == ".pdf":
            return "pdf"

        if extension == ".docx":
            return "docx"

        if extension == ".txt":
            return "txt"

        raise ValueError("Unsupported File")