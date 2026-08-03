from django.db import models


class Document(models.Model):

    FILE_TYPES = (
        ("pdf", "PDF"),
        ("docx", "DOCX"),
        ("txt", "TXT"),
    )

    title = models.CharField(max_length=255)

    file = models.FileField(upload_to="documents/")

    file_type = models.CharField(
        max_length=10,
        choices=FILE_TYPES,
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title