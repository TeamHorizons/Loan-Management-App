
from django.db import models
from borrower.models import Borrower
from document.models import Document


import json # For handling array-like fields for non-PostgreSQL databases

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

    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='kyc_details')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending', null=False, blank=False)
    aadhar_number = models.CharField(max_length=12, unique=True, blank=True, null=True) # Aadhar can be optional
    pan_number = models.CharField(max_length=10, unique=True, blank=True, null=True) # PAN can be optional # ManyToManyField for documents, as one KYC can have multiple documents
    documents = models.ManyToManyField(Document, blank=True, related_name='kyc_associations')
    completion_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    remark = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "KYC"
        verbose_name_plural = "KYC Details"
        ordering = ['-created_at']

    def __str__(self):
        return f"KYC for {self.borrower.first_name} ({self.status})"
