from .models import HairRequest
from django import forms

class HairRequestForm(forms.ModelForm):
    class Meta:
        model = HairRequest
        fields = ('name', 'email', 'phone_number', 'subject', 'message')