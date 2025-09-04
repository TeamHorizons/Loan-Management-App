from django.db import models
from django.utils import timezone
# Create your models here.

class Loan(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED','Rejected'),
        ('DISBURSED', 'Disbursed'),
        ('CLOSED', 'Closed'),
    ]

    borrower = models.ForeignKey('borrower.Borrower', on_delete=models.CASCADE, related_name='loans')
    kyc = models.OneToOneField('kyc.KYC', on_delete=models.CASCADE, null=True, blank=True)
    document = models.OneToOneField('document.Document', on_delete=models.CASCADE, null=True, blank=True)
    emi = models.OneToOneField('emi.EMI', on_delete=models.CASCADE, null=True, blank=True)


    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tenure_months = models.IntegerField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)


    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Loan {self.id} - {self.borrower} ({self.status})"
