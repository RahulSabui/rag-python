from typing import TypedDict


class AgentState(TypedDict):
    question: str
    history: list

    context: str

    answer: str

    sources: list