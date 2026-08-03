from django.shortcuts import get_object_or_404

from agents.graph import graph

from .models import Conversation, Message


class ChatService:

    @staticmethod
    def ask(conversation_id, question):

        conversation = get_object_or_404(
            Conversation,
            pk=conversation_id,
        )

        # Save user message
        Message.objects.create(
            conversation=conversation,
            role="user",
            content=question,
        )

        # Build conversation history
        history = list(
            Message.objects.filter(
                conversation=conversation
            )
            .order_by("-created_at")[:10]
        )

        history.reverse()

        history_messages = []

        for msg in history:
            history_messages.append(
                {
                    "role": msg.role,
                    "content": msg.content,
                }
            )

        # Execute LangGraph
        result = graph.invoke(
            {
                "question": question,
                "history": history_messages,
                "context": "",
                "answer": "",
                "sources": [],
            }
        )

        # Save assistant response
        assistant = Message.objects.create(
            conversation=conversation,
            role="assistant",
            content=result["answer"],
            sources=result["sources"],
        )

        return {
            "conversation_id": str(conversation.id),
            "message_id": assistant.id,
            "answer": assistant.content,
            "sources": assistant.sources,
        }