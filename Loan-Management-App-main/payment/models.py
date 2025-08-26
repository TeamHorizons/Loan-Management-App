from django.db import models
from django.utils import timezone
import json # For handling array-like fields for non-PostgreSQL databases


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

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('failed', 'Failed'),
        ('manual', 'Manually Confirmed'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES, null=False, blank=False)
    emi = models.ForeignKey('emi.EMI', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments_made')
    bank_reference_id = models.CharField(max_length=50, null=False, blank=False, unique=True)
    payment_date = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')  # ✅ Added this

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['-payment_date']

    def __str__(self):
        return f'Payment {self.id} - {self.amount} via {self.payment_mode} ({self.status})'