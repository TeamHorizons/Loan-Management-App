from django import forms
from borrower.models import Borrower
from crispy_forms.helper import FormHelper # helper class
from crispy_forms.layout import Submit# for button rendering
# Borrower Form
class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['user_profile','first_name', 'last_name', 'mobile',
                'alternate_mobile', 'state',  'district',
                'address','bank_name','branch_name'] # Include all fields from the model
        widgets = {
            'user_profile':forms.SelectMultiple(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'alternate_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'account_number': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_name': forms.Select(attrs={'class': 'form-control'}),
            'branch_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BorrowerSubmit(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = [
            'first_name',
            'last_name',
            'mobile',
            'alternate_mobile',
            'state',
            'district',
            'address',
            'account_number',
            'bank_name',
            'branch_name',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Last Name'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Mobile Number'
            }),
            'alternate_mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Alternate Mobile (optional)'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter State'
            }),
            'district': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter District'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Full Address',
                'rows': 3
            }),
            'account_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Bank Account Number'
            }),
            'bank_name': forms.ChoiceField(attrs={
                'class': 'form-control',
                'placeholder': 'Select a Bank'
            }),
            'branch_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Branch Name'
            }),
        }

