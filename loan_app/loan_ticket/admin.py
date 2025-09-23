from django.contrib import admin

from .models import LoanTicket, LoanSettings

# Register your models here.
@admin.register(LoanSettings)
class LoanSettingsAdmin(admin.ModelAdmin):
    list_display = ('interest_rate', 'updated_at')

    # This ensures the admin can't create multiple LoanSettings records
    def has_add_permission(self, request):
        # Only allow adding if no LoanSettings exist
        return not LoanSettings.objects.exists() or super().has_add_permission(request)


@admin.register(LoanTicket)
class LoanTicketAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'loan_type', 'loan_amount', 'loan_tenure', 'interest_rate', 'status', 'start_date', 'end_date')
    list_filter = ('loan_type', 'status', 'start_date', 'end_date')
    search_fields = ('borrower__first_name', 'borrower__last_name', 'loan_type', 'status')
    raw_id_fields = ('borrower',) # Use raw_id_fields for ForeignKey to improve performance with many related objects
    readonly_fields = ('created_at',)
