from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='Enter Email!')
    class Meta:
        model = User
        fields = ('username','email','password1','password2')