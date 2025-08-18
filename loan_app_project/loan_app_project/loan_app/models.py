
from django.db import models
from django.utils import timezone
import json # For handling array-like fields for non-PostgreSQL databases

# Borrower Model
class Borrower(models.Model):
    """
    Represents a borrower in the loan application.
    Corresponds to the `borrower` table.
    """
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
        return f"{self.first_name} {self.last_name} ({self.mobile})"

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

    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='loan_tickets')
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
        return f"Loan {self.id} for {self.borrower.first_name} - {self.loan_amount} ({self.status})"

# Document Model
class Document(models.Model):
    """
    Represents a document type.
    Corresponds to the `documents` table.
    """
    document_name = models.CharField(max_length=50, null=False, blank=False)
    # dcoument_folder is likely a path or category, using CharField
    document_folder = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ['document_name']

    def __str__(self):
        return self.document_name

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
    pan_number = models.CharField(max_length=10, unique=True, blank=True, null=True) # PAN can be optional
    # ManyToManyField for documents, as one KYC can have multiple documents
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
    # emi_id is a ForeignKey, but can be null if it's a general payment not tied to a specific EMI initially
    # or if it's a payment for penalty. The SQL indicates it's NOT NULL, so we'll keep it as such.
    # However, the SQL also makes payment_id a FK in EMI and Penalty, creating a circular dependency.
    # To break this, we'll make payment_id in EMI and Penalty a ForeignKey to Payment,
    # and here, `emi_id` refers to the EMI that this payment is for.
    # This implies a payment is primarily for an EMI.
    # If a payment can exist independently of an EMI (e.g., for a penalty directly),
    # then `emi` should be null=True. Given the SQL, it's NOT NULL.
    # We will assume a payment is always tied to an EMI.
    emi = models.ForeignKey('EMI', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments_made')
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

# EMI Model
class EMI(models.Model):
    """
    Represents an Equated Monthly Installment for a loan ticket.
    Corresponds to the `emi` table.
    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Overdue', 'Overdue'),
        ('Waived', 'Waived'),
    ]

    loan_ticket = models.ForeignKey(LoanTicket, on_delete=models.CASCADE, related_name='emis')
    emi_no = models.IntegerField(null=False, blank=False)
    emi_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    outstanding_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    # payment_id from SQL implies one-to-one or one-to-many.
    # If one EMI can have multiple payments (e.g., partial payments), this needs to be a ManyToMany or a reverse relation.
    # If one EMI is paid by one payment, it's OneToOne.
    # The SQL `emi` table has `payment_id` and `payments` table has `emi_id`. This is a circular dependency.
    # I will assume `payment_id` in `emi` refers to the *final* payment that marked it paid, or the *first* payment.
    # For simplicity and to break the circular dependency, I will remove `payment_id` from EMI and
    # let the `Payment` model have a ForeignKey to `EMI`.
    # If an EMI needs to track *which* payment paid it, we can add a OneToOneField or a ForeignKey here.
    # For now, `payments_made` reverse relation from Payment will suffice.
    # If `payment_id` in EMI means the ID of the payment that *completed* this EMI, then it should be null=True.
    # Given the SQL `payment_id integer(10) NOT NULL` in `emi` and `emi_id integer(10) NOT NULL` in `payments`,
    # this suggests a payment *belongs* to an EMI, and an EMI *has* a payment.
    # This is best modeled as a OneToOneField from EMI to Payment if an EMI is paid by exactly one payment,
    # or a ForeignKey from Payment to EMI if one EMI can have multiple payments.
    # I will stick to the ForeignKey from Payment to EMI and remove `payment_id` from EMI,
    # as it's the more common and flexible approach.
    # If the user insists on `payment_id` in EMI, it would require careful handling of circular dependencies.
    # Let's assume `payment_id` in `emi` from the SQL refers to the `Payment` that *settled* this EMI.
    # This would make it a OneToOneField or a ForeignKey with `null=True`.
    # To resolve the circular dependency, I'll make it a ForeignKey with `null=True, blank=True`.
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True, related_name='emi_settled_by_payment')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    remark = models.TextField(blank=True, null=True)
    # penalty_id is a ForeignKey to Penalty, but can be null if no penalty
    penalty = models.ForeignKey('Penalty', on_delete=models.SET_NULL, null=True, blank=True, related_name='emi_penalized')

    class Meta:
        verbose_name = "EMI"
        verbose_name_plural = "EMIs"
        ordering = ['loan_ticket', 'emi_no']
        unique_together = (('loan_ticket', 'emi_no'),) # An EMI number is unique per loan ticket

    def __str__(self):
        return f"EMI {self.emi_no} for Loan {self.loan_ticket.id} ({self.status})"

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

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending', null=False, blank=False)
    emi = models.ForeignKey(EMI, on_delete=models.CASCADE, related_name='penalties')
    amount = models.DecimalField(max_digits=11, decimal_places=2, null=False, blank=False)
    # payment_id here refers to the payment that settled this penalty.
    # It can be null if the penalty is not yet paid.
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

