
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



class KYCSubmit(forms.ModelForm):
    class Meta:
        model = KYC
        fields = [
            'aadhar_number',
            'pan_number',
            'documents',
            'remark',
        ]
        widgets = {
            'aadhar_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your Aadhar Number',
                'maxlength': '12'
            }),
            'pan_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your PAN Number',
                'maxlength': '10'
            }),
            'documents': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),

            'remark': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Add any additional remarks (optional)',
                'rows': 3
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['aadhar_number'].required = True
        self.fields['pan_number'].required = True
        self.fields['documents'].required = True
