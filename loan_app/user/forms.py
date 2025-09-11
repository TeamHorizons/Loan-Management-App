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
from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import UserProfile
from django.core.exceptions import ValidationError

class RegForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Enter Username'})
    )
    email = forms.EmailField(
        max_length=150,
        required=True,
        help_text='example@gmail.com',
        widget=forms.EmailInput(attrs={'placeholder':'Enter Email'})
    )
    phone_number = forms.CharField(
        max_length=11,
        required=True,
        help_text='e.g. 08012345678',
        widget=forms.TextInput(attrs={'placeholder':'Enter Phone Number'})
    )

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if UserProfile.objects.filter(username__iexact=username).exists():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserProfile.objects.filter(email__iexact=email).exists():
            raise ValidationError("Email already exists")
        return email

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if UserProfile.objects.filter(phone_number=phone).exists():
            raise ValidationError("Phone number already exists")
        return phone

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = ""  # current URL
        self.helper.form_id = "signup-form"
        self.helper.label_class = "form-label"
        self.helper.field_class = "mb-3"
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
