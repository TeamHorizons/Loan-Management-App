from django.contrib import admin
from .models import Document

# Register your models here.

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_category', 'document_type', 'created_at')
    search_fields = ('document_category', 'document_type')
    readonly_fields = ('created_at',)
