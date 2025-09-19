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
    LOAN_TYPE_CHOICES = [
        ('personal loan', 'PERSONAL LOAN'),
        ('mortgage', 'MORTGAGE (HOME LOAN)'),
        ('auto loan', 'AUTO LOAN'),
        ('student loan', 'STUDENT LOAN'),
        ('business loan', 'BUSINESS LOAN'),
        ('payday loan', 'PAYDAY LOAN'),
        ('credit card loan', 'CREDIT CARD LOAN'),
        ('debt consolidation loan', 'DEBT CONSOLIDATION LOAN'),
        ('microfinance loan', 'MICROFINANCE LOAN'),
        ('agricultural loan', 'AGRICULTURAL LOAN'),
        ('bridge loan', 'BRIDGE LOAN'),
        ('equipment financing', 'EQUIPMENT FINANCING'),
        ('line of credit', 'LINE OF CREDIT'),
        ('secured loan', 'SECURED LOAN'),
        ('unsecured loan', 'UNSECURED LOAN'),
    ]

    LOAN_TENURE_CHOICES = [
        ('one month', 'ONE MONTH'),
        ('two months', 'TWO MONTH'),
        ('three months', 'THREE MONTH'),
        ('four months', 'FOUR MONTH'),
        ('five months', 'FIVE MONTH'),
        ('six months', 'SIX MONTH'),
        ('seven months', 'SEVEN MONTH'),
        ('eight months', 'EIGHT MONTH'),
        ('nine months', 'NINE MONTH'),
        ('two years', 'TWO YEARS'),
        ('five years', 'FIVE YEARS'),
        ('ten years', 'TEN YEARS'),
        ]
    
    STATUS_CHOICES = [
            ('Ongoing', 'ONGOING'),
            ('Approved', 'APPROVED'),
            ('Rejected', 'REJECTED'),
            ('Completed', 'COMPLETED'),
            ('Defaulted', 'DEFAULTED'),
        ]

    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='loanticket_details', blank=True, null=True)
    loan_type = models.CharField(max_length=50, null=False, blank=False, choices=LOAN_TYPE_CHOICES)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    loan_tenure = models.CharField(null=False, blank=False , choices=LOAN_TENURE_CHOICES, default='one month')
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False) # Changed from 3,2 to 5,2 for more flexibility
    transaction_id = models.UUIDField(null=True, auto_created=True, unique=True, max_length=12, help_text='An automatic generated identification number(s) for a transaction')
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
        return f"Loan {self.id} for {self.borrower.user_profile} - ({self.status})"
