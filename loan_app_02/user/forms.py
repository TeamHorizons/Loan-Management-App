from django import forms
from user.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# Working with crispy form
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

"""
This is a registration form extended with django UserCreationForm
which provides password confirming and hashing.
"""
class RegForm(UserCreationForm):
    email = forms.EmailField(max_length=150,
                            required=True,
                            help_text='example@gmail.com',
                            widget=forms.EmailInput(attrs={'placeholder':'Enter Email'}))
    
    phone_number = forms.CharField(max_length=11,
                                help_text='e.g. 08012345678')
    

    class Meta:
        model = UserProfile
        fields = ['email','phone_number', 'password1', 'password2']

    # checking if email already exists in the database
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserProfile.objects.filter(email__iexact=email).exists():
            raise ValidationError(message='Email already exists')
        return email
    
    # Crispy helper controls the form rendering
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "" #current URL
        self.helper.form_id = "signup-form"
        self.helper.label_class = "form-label"
        self.helper.field_class = "mb-3"

        # Buttons
        self.helper.add_input(Submit(name='submit', value='Create Account'))
        



class LoginForm(forms.Form):
    email = forms.EmailField(max_length=150,
                            required=True, 
                            help_text='example@gmail.com',
                            widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    
    password = forms.CharField(required=True, 
                            widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_action = "" #current url
        self.helper.form_id = "login-form"
        self.helper.label_class = "form-helper"
        self.helper.field_class = 'mb-3'

        # Buttons

        self.helper.add_input(Submit(name='submit', value='Login'))
