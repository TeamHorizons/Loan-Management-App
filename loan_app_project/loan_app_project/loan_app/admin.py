
from django.contrib import admin
from .models import Borrower, LoanTicket, EMI, Document, KYC, Penalty, Payment

# Register your models here.

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile', 'state', 'created_at')
    search_fields = ('first_name', 'last_name', 'mobile', 'account_number')
    list_filter = ('state', 'district', 'created_at')
    # Add fields to be displayed in the detail view
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'mobile', 'alternate_mobile')
        }),
        ('Address Details', {
            'fields': ('address', 'pincode', 'district', 'state')
        }),
        ('Bank Details', {
            'fields': ('account_number', 'ifsc_code', 'bank_name', 'branch_name')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',) # Makes this section collapsible
        }),
    )
    readonly_fields = ('created_at',)


@admin.register(LoanTicket)
class LoanTicketAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'loan_type', 'loan_amount', 'loan_tenure_in_months', 'interest_rate', 'status', 'start_date', 'end_date')
    list_filter = ('loan_type', 'status', 'start_date', 'end_date')
    search_fields = ('borrower__first_name', 'borrower__last_name', 'loan_type', 'status')
    raw_id_fields = ('borrower',) # Use raw_id_fields for ForeignKey to improve performance with many related objects
    readonly_fields = ('created_at',)


@admin.register(EMI)
class EMIAdmin(admin.ModelAdmin):
    list_display = ('loan_ticket', 'emi_no', 'emi_amount', 'outstanding_amount', 'status', 'start_date', 'end_date', 'payment', 'penalty')
    list_filter = ('status', 'start_date', 'end_date', 'loan_ticket__loan_type')
    search_fields = ('loan_ticket__borrower__first_name', 'loan_ticket__id', 'emi_no')
    raw_id_fields = ('loan_ticket', 'payment', 'penalty') # raw_id_fields for ForeignKeys
    readonly_fields = ('created_at',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_name', 'document_folder', 'created_at')
    search_fields = ('document_name', 'document_folder')
    readonly_fields = ('created_at',)


@admin.register(KYC)
class KYCAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'status', 'aadhar_number', 'pan_number', 'completion_date', 'created_at')
    list_filter = ('status', 'completion_date', 'created_at')
    search_fields = ('borrower__first_name', 'borrower__last_name', 'aadhar_number', 'pan_number')
    raw_id_fields = ('borrower',)
    filter_horizontal = ('documents',) # For ManyToManyField with a nice widget
    readonly_fields = ('created_at',)


@admin.register(Penalty)
class PenaltyAdmin(admin.ModelAdmin):
    list_display = ('emi', 'amount', 'status', 'due_date', 'payment', 'created_at')
    list_filter = ('status', 'due_date', 'created_at')
    search_fields = ('emi__loan_ticket__borrower__first_name', 'emi__emi_no')
    raw_id_fields = ('emi', 'payment')
    readonly_fields = ('created_at',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'payment_mode', 'emi', 'bank_reference_id', 'payment_date', 'created_at')
    list_filter = ('payment_mode', 'payment_date', 'created_at')
    search_fields = ('bank_reference_id', 'emi__loan_ticket__borrower__first_name')
    raw_id_fields = ('emi',)
    readonly_fields = ('created_at',)
