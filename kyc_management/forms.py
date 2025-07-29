from django import forms
from kyc_management.models import KYC, Documents

class KYCForm(forms.ModelForm):
    documents = forms.ModelMultipleChoiceField(queryset=Documents.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = KYC
        fields = [
            'status',
            'borrower',
            'aadhar_number',
            'pan_number',
            'documents',
            'remark'
        ]