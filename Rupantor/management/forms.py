from django import forms
from .models import CustomerMessage

class CustomerMessageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    msg = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    class Meta:
        model = CustomerMessage
        fields = ['name', 'email', 'subject', 'msg']