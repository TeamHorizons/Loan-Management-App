
from django import forms
from kyc.models import  KYC



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