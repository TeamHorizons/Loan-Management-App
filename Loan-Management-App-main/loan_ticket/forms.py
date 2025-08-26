
from django import forms
from loan_ticket.models import LoanTicket



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