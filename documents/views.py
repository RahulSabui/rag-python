from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Document
from .serializers import DocumentSerializer
from .services import DocumentService
from embeddings.services import EmbeddingService


class UploadDocumentView(APIView):

    def post(self, request):

        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        file_type = DocumentService.detect_file_type(uploaded_file.name)

        document = Document.objects.create(
            title=uploaded_file.name,
            file=uploaded_file,
            file_type=file_type,
        )

        EmbeddingService.ingest(document)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)