from django.conf import settings
from langchain_openai import ChatOpenAI


class OpenAIModel:

    @staticmethod
    def get():
        return ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0.2,
            api_key=settings.OPENAI_API_KEY,
        )