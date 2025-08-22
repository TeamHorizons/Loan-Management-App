
from django import forms
from penalty.models import Penalty

# Penalty Form
class PenaltyForm(forms.ModelForm):
    class Meta:
        model = Penalty
        fields = '__all__'
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'emi': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment': forms.Select(attrs={'class': 'form-control'}), # Can be null
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }