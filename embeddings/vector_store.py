from langchain_chroma import Chroma

from .embedding import EmbeddingModel


class VectorStore:

    @staticmethod
    def get():

        return Chroma(
            persist_directory="chroma_db",
            embedding_function=EmbeddingModel.get(),
        )