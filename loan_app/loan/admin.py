
from django.contrib import admin
from .models import TransactionId
from payment.models import Payment
from emi.models import EMI
from penalty.models import Penalty

# Register your models here.
# admin.py
class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0

class PenaltyInline(admin.TabularInline):
    model = Penalty
    extra = 0

class EMIInline(admin.TabularInline):
    model = EMI
    extra = 0

@admin.register(TransactionId)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'created_at')
    inlines = [PaymentInline, PenaltyInline, EMIInline]
