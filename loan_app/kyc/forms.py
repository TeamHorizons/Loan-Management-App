
from django import forms
from kyc.models import  KYC


# KYC Form
class KYCForm(forms.ModelForm):
    class Meta:
        model = KYC
        fields = ['status','bvn_number', 'tin_number','documents', 'remark']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'bvn_number': forms.TextInput(attrs={'class': 'form-control'}),
            'tin_number': forms.TextInput(attrs={'class': 'form-control'}), # For ManyToMany
            'completion_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }



class KYCSubmit(forms.ModelForm):
    class Meta:
        model = KYC
        fields = [
            'bvn_number',
            'tin_number',
        ]
        widgets = {
            'bvn_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your BVN Number',
                'maxlength': '12'
            }),
            'tin_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your TIN Number',
                'maxlength': '10'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bvn_number'].required = True
        self.fields['tin_number'].required = True
