from embeddings.retriever import DocumentRetriever


def search_documents(state):

    question = state["question"]

    documents = DocumentRetriever.search(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return {
        "context": context,
        "sources": [
            document.metadata
            for document in documents
        ],
    }