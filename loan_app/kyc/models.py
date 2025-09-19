
from django.db import models
from borrower.models import Borrower
from document.models import Document

# import validators from custom py file
from custom.validators import validate_bvn, validate_tin

# Create your models here.
# KYC Model
class KYC(models.Model):
    """
    Represents Know Your Customer (KYC) details for a borrower.
    Corresponds to the `kyc` table.
    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Verified', 'Verified'),
        ('Rejected', 'Rejected'),
    ]

    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='kyc_details', blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending', null=False, blank=False)
    BVN_number = models.CharField(null=True, blank=True, unique=True, max_length=11, validators=[validate_bvn], help_text="Bank Verification Number")
    TIN_number = models.CharField(null=True, blank=True, unique=True, max_length=12, validators=[validate_tin], help_text="TAX Identification Number")
    documents = models.ManyToManyField(Document, blank=True, related_name='kyc_associations') # ManyToManyField for documents, as one KYC can have multiple documents
    completion_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "KYC"
        verbose_name_plural = "KYC Details"
        ordering = ['-created_at']

    def __str__(self):
        return f"KYC for {self.borrower.user_profile} ({self.status})"
    
        
