# myapp/forms.py
from django import forms

class PhoneNumberForm(forms.Form):
    phone_no = forms.CharField(max_length=10, min_length=10, label="Phone Number")
