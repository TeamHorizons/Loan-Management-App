from django.contrib import admin

from .models import KYC


# Register your models here.

@admin.register(KYC)
class KYCAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'status', 'aadhar_number', 'pan_number', 'completion_date', 'created_at')
    list_filter = ('status', 'completion_date', 'created_at')
    search_fields = ('borrower__first_name', 'borrower__last_name', 'aadhar_number', 'pan_number')
    raw_id_fields = ('borrower',)
    filter_horizontal = ('documents',) # For ManyToManyField with a nice widget
    readonly_fields = ('created_at',)