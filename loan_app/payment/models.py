from django.db import models
from django.utils import timezone
from loan.models import TransactionId

# Create your models here.


# Payment Model (Forward declared for EMI and Penalty)
class Payment(models.Model):
    """
    Represents a payment made.
    Corresponds to the `payments` table.
    """
    PAYMENT_MODE_CHOICES = [
        ('Cash', 'Cash'),
        ('Bank Transfer', 'Bank Transfer'),
        ('Online', 'Online'),
        ('Cheque', 'Cheque'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES, null=False, blank=False)
    """
    # emi_id is a ForeignKey, but can be null if it's a general payment not tied to a specific EMI initially
    # or if it's a payment for penalty. The SQL indicates it's NOT NULL, so we'll keep it as such.
    # However, the SQL also makes payment_id a FK in EMI and Penalty, creating a circular dependency.
    # To break this, we'll make payment_id in EMI and Penalty a ForeignKey to Payment,
    # and here, `emi_id` refers to the EMI that this payment is for.
    # This implies a payment is primarily for an EMI.
    # If a payment can exist independently of an EMI (e.g., for a penalty directly),
    # then `emi` should be null=True. Given the SQL, it's NOT NULL.
    # We will assume a payment is always tied to an EMI.
    """
    transaction_id = models.ForeignKey(TransactionId, on_delete=models.CASCADE, related_name='payment_trans_id', null=True)
    emi = models.ForeignKey('emi.EMI', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments_made')
    bank_reference_id = models.CharField(max_length=50, null=False, blank=False, unique=True) # Assuming unique
    payment_date = models.DateTimeField(blank=True, null=True) # Can be set later
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ['-payment_date']

    def __str__(self):
        return f"Payment {self.id} - {self.amount} via {self.payment_mode}"
