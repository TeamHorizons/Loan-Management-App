from django.contrib import admin

from .models import Penalty

# Register your models here.

@admin.register(Penalty)
class PenaltyAdmin(admin.ModelAdmin):
    list_display = ('emi', 'amount', 'status', 'due_date', 'payment', 'created_at')
    list_filter = ('status', 'due_date', 'created_at')
    search_fields = ('emi__loan_ticket__borrower__first_name', 'emi__emi_no')
    raw_id_fields = ('emi', 'payment')
    readonly_fields = ('created_at',)
