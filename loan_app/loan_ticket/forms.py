
from django import forms
from loan_ticket.models import LoanTicket
from datetime import timedelta



# LoanTicketSubmit Form
class LoanTicketForm(forms.ModelForm):
    class Meta:
        model = LoanTicket
        fields = ['loan_type', 'loan_tenure', 'start_date', 'end_date', 'status', 'remark',]
        widgets = {
            'loan_type': forms.Select(attrs={'class': 'form-control'}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'loan_tenure': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
# loan_ticket/forms.py


class LoanTicketSubmit(forms.ModelForm):
    class Meta:
        model = LoanTicket
        fields = ['loan_type', 'loan_amount', 'loan_tenure', 'start_date']  
        widgets = {
            'loan_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Type of Loan'}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Loan Amount'}),
            'loan_tenure': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Loan Tenure'}),
            'start_date':  forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

    def save(self, commit=True):
        loan_ticket = super().save(commit=False)

        # Auto-apply business rules
        # Example: simple fixed interest rate
        loan_ticket.interest_rate = 10.0  

        # Calculate end_date
        loan_ticket.end_date = loan_ticket.start_date + timedelta(
            days=30 * loan_ticket.loan_tenure
        )

        # borrower will be attached from the logged-in user in the view
        if commit:
            loan_ticket.save()
        return loan_ticket
