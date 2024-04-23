from .models import Appointment
from django import forms


class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False

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
