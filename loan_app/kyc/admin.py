from django.contrib import admin

from .models import KYC


# Register your models here.

@admin.register(KYC)
class KYCAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'status', 'bvn_number', 'tin_number', 'completion_date', 'created_at')
    list_filter = ('status', 'completion_date', 'created_at')
    search_fields = ('borrower__first_name', 'borrower__last_name')
    raw_id_fields = ('borrower',)
    readonly_fields = ('created_at',)