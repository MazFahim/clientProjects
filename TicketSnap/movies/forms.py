from django import forms
from .models import CustomerMessage

class CustomerMessageForm(forms.ModelForm):
    name = forms.TextInput()
    email = forms.TextInput()
    subject = forms.TextInput()
    msg = forms.TextInput()
    class Meta:
        model = CustomerMessage
        fields = ['name', 'email', 'subject', 'msg']