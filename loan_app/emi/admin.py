from django.contrib import admin

from .models import EMI

# Register your models here.


@admin.register(EMI)
class EMIAdmin(admin.ModelAdmin):
    list_display = ('loan_ticket', 'emi_no', 'emi_amount', 'outstanding_amount', 'status', 'start_date', 'end_date', 'payment', 'penalty')
    list_filter = ('status', 'start_date', 'end_date', 'loan_ticket__loan_type')
    search_fields = ('loan_ticket__borrower__first_name', 'loan_ticket__id', 'emi_no')
    raw_id_fields = ('loan_ticket', 'payment', 'penalty') # raw_id_fields for ForeignKeys
    readonly_fields = ('created_at',)
