from django import forms
from .models import *



class LoginForm(forms.Form):
   email = forms.CharField(max_length = 100,)
   password = forms.CharField(widget=forms.PasswordInput())

