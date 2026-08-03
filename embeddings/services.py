import uuid

from .extractor import DocumentExtractor
from .chunker import TextChunker
from .vector_store import VectorStore


class EmbeddingService:

    @staticmethod
    def ingest(document):
        text = DocumentExtractor.extract(document.file.path)

        chunks = TextChunker.split(text)

        db = VectorStore.get()

        ids = [str(uuid.uuid4()) for _ in chunks]

        metadatas = [
            {
                "document_id": str(document.id),
                "title": document.title,
            }
            for _ in chunks
        ]

        db.add_texts(
            texts=chunks,
            metadatas=metadatas,
            ids=ids,
        )