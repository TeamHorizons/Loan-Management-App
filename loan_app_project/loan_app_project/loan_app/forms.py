
from django import forms
from .models import Borrower, LoanTicket, EMI, Document, KYC, Penalty, Payment

# Borrower Form
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = '__all__' # Include all fields from the model
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'alternate_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'account_number': forms.TextInput(attrs={'class': 'form-control'}),
            'ifsc_code': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'branch_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

# LoanTicket Form
class LoanTicketForm(forms.ModelForm):
    class Meta:
        model = LoanTicket
        fields = '__all__'
        widgets = {
            'borrower': forms.Select(attrs={'class': 'form-control'}),
            'loan_type': forms.TextInput(attrs={'class': 'form-control'}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'loan_tenure_in_months': forms.NumberInput(attrs={'class': 'form-control'}),
            'interest_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# EMI Form
class EMIForm(forms.ModelForm):
    class Meta:
        model = EMI
        fields = '__all__'
        widgets = {
            'loan_ticket': forms.Select(attrs={'class': 'form-control'}),
            'emi_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'emi_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'outstanding_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'payment': forms.Select(attrs={'class': 'form-control'}), # Can be null, so select allows empty
            'status': forms.Select(attrs={'class': 'form-control'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'penalty': forms.Select(attrs={'class': 'form-control'}), # Can be null
        }

# Document Form
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        widgets = {
            'document_name': forms.TextInput(attrs={'class': 'form-control'}),
            'document_folder': forms.TextInput(attrs={'class': 'form-control'}),
        }

# KYC Form
class KYCForm(forms.ModelForm):
    class Meta:
        model = KYC
        fields = '__all__'
        widgets = {
            'borrower': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control'}),
            'pan_number': forms.TextInput(attrs={'class': 'form-control'}),
            'documents': forms.SelectMultiple(attrs={'class': 'form-control'}), # For ManyToMany
            'completion_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# Penalty Form
class PenaltyForm(forms.ModelForm):
    class Meta:
        model = Penalty
        fields = '__all__'
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'emi': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment': forms.Select(attrs={'class': 'form-control'}), # Can be null
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# Payment Form
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control'}),
            'emi': forms.Select(attrs={'class': 'form-control'}), # Can be null
            'bank_reference_id': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
