from .llm import OpenAIModel


def generate_answer(state):

    llm = OpenAIModel.get()

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful AI assistant.\n"
                "Only answer using the provided context.\n"
                "If the answer is not present, say you don't know."
            ),
        }
    ]

    messages.extend(state["history"])

    messages.append(
        {
            "role": "user",
            "content": f"""
                Context:

                {state["context"]}

                Question:

                {state["question"]}
            """,
        }
    )

    response = llm.invoke(messages)

    return {
        "answer": response.content,
    }