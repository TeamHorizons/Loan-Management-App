from django import forms
from payment.models import Payment



# Payment Form
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields =  ['amount', 'payment_mode', 'email']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_mode': forms.Select(attrs={'class': 'form-control'}),
            'emi': forms.Select(attrs={'class': 'form-control'}), # Can be null
            'bank_reference_id': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }