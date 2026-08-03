from django.conf import settings
from langchain_openai import OpenAIEmbeddings


class EmbeddingModel:

    @staticmethod
    def get():
        return OpenAIEmbeddings(
            model="text-embedding-3-small",
            api_key=settings.OPENAI_API_KEY,
        )