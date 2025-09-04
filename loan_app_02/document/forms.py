
from django import forms
from document.models import Document


# Document Form
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        widgets = {
            'document_category': forms.Select(attrs={'class': 'form-control'}),
            'document_type': forms.Select(attrs={'class': 'form-control'}),
        }


class DocumentSubmit(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document_category', 'document_type']
        widgets = {
            'document_category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Document Category (e.g. Identity)'
            }),
            'document_type': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select Document Type'
            }),
        }
