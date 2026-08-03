from .vector_store import VectorStore


class DocumentRetriever:

    @staticmethod
    def search(question, limit=5):

        db = VectorStore.get()

        results = db.similarity_search(
            question,
            k=limit
        )

        return results