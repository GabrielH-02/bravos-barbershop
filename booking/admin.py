from django.contrib import admin
from .models import Service, AppointmentTime, Appointment

# Register your models here.
admin.site.register(Service)


admin.site.register(AppointmentTime)


admin.site.register(Appointment)