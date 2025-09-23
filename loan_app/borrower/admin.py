

from django.contrib import admin
from .models import Borrower

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
            'fields': ('address', 'district', 'state')
        }),
        ('Bank Details', {
            'fields': ('account_number', 'bank_name', 'branch_name')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',) # Makes this section collapsible
        }),
    )
    readonly_fields = ('created_at',)