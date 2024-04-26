from .models import Appointment
from django import forms


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('title', 'stylist', 'date_appo', 'time_appo')
        widgets = {
            'date_appo': forms.DateInput(attrs={'class': 'form-control datepicker'})
        }
        labels = {
            'title': 'Service',
            'stylist': 'Stylist',
            'date_appo': 'Appointment Date',
            'time_appo': 'Appointment Time',
        }
        for field_name in fields:
            field = {field_name: forms.CharField(required=True)}