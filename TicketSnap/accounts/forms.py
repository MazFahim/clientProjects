from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordResetForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': ''}  # Customize or remove the message
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': ''} 
    )


class CustomPasswordResetForm(PasswordResetForm):
    pass