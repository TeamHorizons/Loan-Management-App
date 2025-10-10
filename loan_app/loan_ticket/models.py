from django.db import models
from borrower.models import Borrower
from loan.models import TransactionId


#Loan Settings Model
class LoanSettings(models.Model):
    interest_rate = models.DecimalField(
        max_digits=5, decimal_places=2,
        help_text="Default interest rate (%) applied to new loans"
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Default Interest Rate: {self.interest_rate}%"

    class Meta:
        verbose_name = "Loan Setting"
        verbose_name_plural = "Loan Settings"
        get_latest_by = 'updated_at'


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

    
    STATUS_CHOICES = [
            ('Ongoing', 'ONGOING'),
            ('Approved', 'APPROVED'),
            ('Rejected', 'REJECTED'),
            ('Completed', 'COMPLETED'),
            ('Defaulted', 'DEFAULTED'),
        ]

    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='loanticket_details', blank=True, null=True)
    loan_type = models.CharField(max_length=50, null=False, blank=False, choices=LOAN_TYPE_CHOICES, default='personal loan')
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    loan_tenure = models.PositiveIntegerField(help_text="Enter loan tenure in months")
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False) # Changed from 3,2 to 5,2 for more flexibility
    transaction_id = models.ForeignKey(TransactionId, on_delete=models.CASCADE,  related_name='loanticket_trans_id', null=True)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Ongoing', null=False, blank=False)
    remark = models.TextField(blank=True, null=True) # Remark can be optional
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Loan Ticket"
        verbose_name_plural = "Loan Tickets"
        ordering = ['-created_at']


    def save(self, *args, **kwargs):
        # STEP 2: Auto-fill interest_rate if not provided
        if not self.interest_rate:
            try:
                self.interest_rate = LoanSettings.objects.latest('updated_at').interest_rate
            except LoanSettings.DoesNotExist:
                self.interest_rate = 0  # fallback
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Loan {self.id} for {self.borrower.user_profile} - ({self.status})"
    