from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Createing a user model using django built in AbstractUser 
"""
# Abstract user model comes with username, first_name, last-name, email, password, 
# is-staff, is_active, date_joined by default, it can be extended with other fields.
# Using email and password from AbstractUser and extending it with phonenumber 
"""

# Using regular expression (regex) validation
"""
# To check if a user phone number is of 12-digits if not raise a warning message
during registration.This makes sure any phone number being registered is officaily
of lenght 12 which is a standard for a NG phone number.
"""

def phone_number_validator():
    return RegexValidator(regex=r'^(?:070|080|081|090|091)\d{8}$', #checks for known nigerian phone number prefix
        message='Enter a valid Nigerian phone number (e.g. 08012345678).')

# Create your models here.

<<<<<<< HEAD:loan_app_02/user/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
=======
class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, 
                                    unique=True, 
                                    blank=False, 
                                    null=False, 
                                    validators=[phone_number_validator()]
                                    ) 
    
    USERNAME_FIELD = "email"       # this tells Django to use email for login
    REQUIRED_FIELDS = ['username']  # Don’t force phone_number when creating superuser
>>>>>>> 8e0c905415d69bf70ef1a3d4667d0ba1cf1625c3:user/models.py

def phone_number_validator():
    return RegexValidator(r'^\d{11}$', 'Enter a valid 11-digit phone number.')

class UserProfile(AbstractUser):
    username = models.CharField(max_length=50, unique=True)  # unique username
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        blank=False,
        null=False,
        validators=[phone_number_validator()]
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']  # required for superuser

    def __str__(self):
        return f"User-{self.username} | User Email:{self.email}"
