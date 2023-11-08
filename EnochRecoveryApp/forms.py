from django import forms
from phone_field import PhoneField
from .models import Customer


class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone = PhoneField(blank=True, help_text="Contact phone number")
    date = forms.DateField()
    time = forms.TimeField()
    location = forms.CharField(max_length=100)
