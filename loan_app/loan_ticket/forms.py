
from django import forms
from loan_ticket.models import LoanTicket, LoanSettings
from datetime import timedelta



# LoanTicketSubmit Form
class LoanTicketForm(forms.ModelForm):
    class Meta:
        model = LoanTicket
        fields = ['loan_type', 'loan_tenure', 'start_date', 'end_date', 'status', 'remark',]
        widgets = {
            'loan_type': forms.Select(attrs={'class': 'form-control'}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'loan_tenure': forms.TextInput(attrs={'class': 'form-control'}),
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
            'loan_tenure': forms.NumberInput(attrs={'min': 1,'class': 'form-control', 'placeholder': 'Enter loan tenure in months'}),
            'start_date':  forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }

    def save(self, commit=True):
        loan_ticket = super().save(commit=False)

        # ✅ Safely assign the latest interest rate
        try:
            latest_setting = LoanSettings.objects.latest('updated_at')
            loan_ticket.interest_rate = latest_setting.interest_rate
        except LoanSettings.DoesNotExist:
            loan_ticket.interest_rate = 0  # fallback default

        if commit:
            loan_ticket.save()

        return loan_ticket
