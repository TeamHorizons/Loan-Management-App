from django.db import models
from django.utils import timezone

from borrower.models import Borrower
import json # For handling array-like fields for non-PostgreSQL databases


# Create your models here.


# LoanTicket Model
class LoanTicket(models.Model):
    """
    Represents a loan application ticket.
    Corresponds to the `loan_ticket` table.
    """
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
        ('Defaulted', 'Defaulted'),
    ]

    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='loanticket_details', blank=True, null=True)
    loan_type = models.CharField(max_length=50, null=False, blank=False)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    loan_tenure_in_months = models.IntegerField(null=False, blank=False)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False) # Changed from 3,2 to 5,2 for more flexibility
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Ongoing', null=False, blank=False)
    remark = models.TextField(blank=True, null=True) # Remark can be optional
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Loan Ticket"
        verbose_name_plural = "Loan Tickets"
        ordering = ['-created_at']

    def __str__(self):
        return f"Loan {self.id} for {self.borrower.first_name} - {self.borrower.user_profile} - ({self.status})"
