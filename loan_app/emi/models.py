import uuid
from django.db import models

from borrower.models import Borrower
from payment.models import Payment
from loan_ticket.models import LoanTicket

# Create your models here.


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
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='emi_details', blank=True, null=True)
    loan_ticket = models.ForeignKey(LoanTicket, on_delete=models.CASCADE, related_name='emis')
    emi_no = models.IntegerField(null=False, blank=False)
    emi_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    outstanding_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    end_date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    """ 
    payment_id from SQL implies one-to-one or one-to-many.
    If one EMI can have multiple payments (e.g., partial payments), this needs to be a ManyToMany or a reverse relation.
    If one EMI is paid by one payment, it's OneToOne.
    The SQL `emi` table has `payment_id` and `payments` table has `emi_id`. This is a circular dependency.
    I will assume `payment_id` in `emi` refers to the *final* payment that marked it paid, or the *first* payment.
    For simplicity and to break the circular dependency, I will remove `payment_id` from EMI and
    let the `Payment` model have a ForeignKey to `EMI`.
    If an EMI needs to track *which* payment paid it, we can add a OneToOneField or a ForeignKey here.
    For now, `payments_made` reverse relation from Payment will suffice.
    If `payment_id` in EMI means the ID of the payment that *completed* this EMI, then it should be null=True.
    Given the SQL `payment_id integer(10) NOT NULL` in `emi` and `emi_id integer(10) NOT NULL` in `payments`,
    this suggests a payment *belongs* to an EMI, and an EMI *has* a payment.
    This is best modeled as a OneToOneField from EMI to Payment if an EMI is paid by exactly one payment,
    or a ForeignKey from Payment to EMI if one EMI can have multiple payments.
    I will stick to the ForeignKey from Payment to EMI and remove `payment_id` from EMI,
    as it's the more common and flexible approach.
    If the user insists on `payment_id` in EMI, it would require careful handling of circular dependencies.
    Let's assume `payment_id` in `emi` from the SQL refers to the `Payment` that *settled* this EMI.
    This would make it a OneToOneField or a ForeignKey with `null=True`.
    To resolve the circular dependency, I'll make it a ForeignKey with `null=True, blank=True`.
    """
    transaction_id = models.UUIDField(null=False, auto_created=True, unique=True, max_length=12, default=uuid.uuid4, editable=False, help_text='An automatic generated identification number(s) for a transaction')
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True, related_name='emi_settled_by_payment')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    remark = models.TextField(blank=True, null=True)
    # penalty_id is a ForeignKey to Penalty, but can be null if no penalty
    penalty = models.ForeignKey("penalty.Penalty", on_delete=models.SET_NULL, null=True, blank=True, related_name='emi_penalized')

    class Meta:
        verbose_name = "EMI"
        verbose_name_plural = "EMIs"
        ordering = ['loan_ticket', 'emi_no']
        unique_together = (('loan_ticket', 'emi_no'),) # An EMI number is unique per loan ticket

    def __str__(self):
        return f"EMI {self.emi_no} for Loan {self.loan_ticket.id} ({self.status})"
