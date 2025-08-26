from django import forms
from emi.models import EMI



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