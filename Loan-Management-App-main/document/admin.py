from django.contrib import admin
from .models import Document

# Register your models here.

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_name', 'document_folder', 'created_at')
    search_fields = ('document_name', 'document_folder')
    readonly_fields = ('created_at',)
