from django.contrib import admin

from .models import Payment

# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'payment_mode', 'emi', 'bank_reference_id', 'payment_date', 'created_at')
    list_filter = ('payment_mode', 'payment_date', 'created_at')
    search_fields = ('bank_reference_id', 'emi__loan_ticket__borrower__first_name')
    raw_id_fields = ('emi',)
    readonly_fields = ('created_at',)
