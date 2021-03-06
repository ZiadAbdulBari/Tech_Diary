from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2') 
