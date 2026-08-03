from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from .models import Conversation
from .services import ChatService
from rest_framework import generics

from .models import Conversation
from .serializers import ConversationSerializer

class ChatAPIView(APIView):

    def post(self, request):

        conversation_id = request.data.get(
            "conversation_id"
        )

        question = request.data.get(
            "question"
        )

        if not conversation_id:
            return Response(
                {
                    "error": "conversation_id required"
                },
                status=400,
            )

        if not question:
            return Response(
                {
                    "error": "question required"
                },
                status=400,
            )

        return Response(
            ChatService.ask(
                conversation_id,
                question,
            )
        )
class ConversationCreateAPIView(
    generics.CreateAPIView
):

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class ConversationListAPIView(
    generics.ListAPIView
):

    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    
class ConversationDetailAPIView(generics.RetrieveAPIView):
    queryset = Conversation.objects.prefetch_related("messages")
    serializer_class = ConversationSerializer

class ConversationDeleteAPIView(
    generics.DestroyAPIView
):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def destroy(self, request, *args, **kwargs):
        conversation = self.get_object()

        conversation.delete()

        return Response(
            {
                "message": "Conversation deleted successfully."
            },
            status=status.HTTP_200_OK,
        )