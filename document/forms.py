
from django import forms
from document.models import Document


# Document Form
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        widgets = {
            'document_name': forms.TextInput(attrs={'class': 'form-control'}),
            'document_folder': forms.TextInput(attrs={'class': 'form-control'}),
        }