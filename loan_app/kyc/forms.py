
from django import forms
from kyc.models import  KYC


# KYC Form
class KYCForm(forms.ModelForm):
    class Meta:
        model = KYC
        fields = ['status','BVN_number', 'TIN_number','documents', 'remark']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'BVN_number': forms.TextInput(attrs={'class': 'form-control'}),
            'TIN_number': forms.TextInput(attrs={'class': 'form-control'}),
            'documents': forms.SelectMultiple(attrs={'class': 'form-control'}), # For ManyToMany
            'completion_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }



class KYCSubmit(forms.ModelForm):
    class Meta:
        model = KYC
        fields = [
            'BVN_number',
            'TIN_number',
            'documents',
            'remark',
        ]
        widgets = {
            'BVN_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your BVN Number',
                'maxlength': '12'
            }),
            'TIN_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your TIN Number',
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
        self.fields['BVN_number'].required = True
        self.fields['TIN_number'].required = True
        self.fields['documents'].required = True
