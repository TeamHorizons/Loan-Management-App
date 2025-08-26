from django.contrib import admin

from .models import Payment

# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'amount', 'email', 'payment_mode', 'emi',
        'bank_reference_id', 'payment_date', 'status', 'created_at'
    )
    list_filter = ('payment_mode', 'status', 'payment_date', 'created_at')
    search_fields = ('email', 'bank_reference_id', 'emi__loan_ticket__borrower__first_name', 'emi__loan_ticket__borrower__last_name')
    raw_id_fields = ('emi',)
    readonly_fields = ('created_at', 'payment_date')
    ordering = ('-created_at',)
    actions = ['mark_as_confirmed']

    def mark_as_confirmed(self, request, queryset):
        updated = queryset.update(status='confirmed')
        self.message_user(request, f'{updated} payment(s) marked as confirmed.')
    mark_as_confirmed.short_description = '✅ Mark selected payments as confirmed'
