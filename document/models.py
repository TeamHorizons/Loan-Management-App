from django.db import models
from django.utils import timezone
import json # For handling array-like fields for non-PostgreSQL databases

# Create your models here.


# Document Model
class Document(models.Model):
    """
    Represents a document type.
    Corresponds to the `documents` table.
    """
    document_name = models.CharField(max_length=50, null=False, blank=False)
    # dcoument_folder is likely a path or category, using CharField
    document_folder = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ['document_name']

    def __str__(self):
        return self.document_name
