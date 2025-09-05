
from django.db import models
from django.utils import timezone
import json # For handling array-like fields for non-PostgreSQL databases

from django.conf import settings
# Create your models here.

# Borrower Model
class Borrower(models.Model):
    """
    Represents a borrower in the loan application.
    Corresponds to the `borrower` table.
    """
    """
    settings.AUTH_USER_MODEL links to the custom user models ensures compatibility,
    links borrower to a single user account.
    """
    user_profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    # Using BigIntegerField for mobile numbers to avoid integer overflow issues
    # and allow for potential leading zeros if treated as numbers.
    # It's often better to store phone numbers as CharField if they are not used in calculations.
    mobile = models.CharField(max_length=15, null=False, blank=False)
    alternate_mobile = models.CharField(max_length=15, blank=True, null=True) # Can be null or blank
    state = models.CharField(max_length=50, null=False, blank=False)
    district = models.CharField(max_length=50, null=False, blank=False)
    pincode = models.CharField(max_length=10, null=False, blank=False) # Pincode can have leading zeros, better as CharField
    address = models.CharField(max_length=250, null=False, blank=False)
    account_number = models.CharField(max_length=50, null=False, blank=False)
    ifsc_code = models.CharField(max_length=11, null=False, blank=False)
    bank_name = models.CharField(max_length=50, null=False, blank=False)
    branch_name = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Borrower"
        verbose_name_plural = "Borrowers"
        ordering = ['-created_at'] # Order by creation date, newest first

    def __str__(self):
        return f"{self.user_profile} | User Mobile:({self.mobile})"
