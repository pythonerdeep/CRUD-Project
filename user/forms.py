from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Registration
        fields='__all__'

class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())