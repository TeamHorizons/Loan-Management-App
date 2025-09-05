from django.db import models
from django.utils import timezone

from payment.models import Payment
from borrower.models import Borrower

import json # For handling array-like fields for non-PostgreSQL databases


# Create your models here.


# Penalty Model
class Penalty(models.Model):
    """
    Represents a penalty applied to an EMI.
    Corresponds to the `penalty` table.
    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Waived', 'Waived'),
    ]
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending', null=False, blank=False)
    emi = models.ForeignKey("emi.EMI", on_delete=models.CASCADE, related_name='penalties')
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=False, blank=False)# payment_id here refers to the payment that settled this penalty.# It can be null if the penalty is not yet paid.
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True, related_name='penalties_paid')
    due_date = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Added created_at as per other tables

    class Meta:
        verbose_name = "Penalty"
        verbose_name_plural = "Penalties"
        ordering = ['-created_at']

    def __str__(self):
        return f"Penalty for EMI {self.emi.emi_no} of Loan {self.emi.loan_ticket.id} - {self.amount} ({self.status})"

