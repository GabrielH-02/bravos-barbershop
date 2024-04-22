from django.shortcuts import render
from django.views import generic
from .models import Service, Appointment


class ServiceList(generic.ListView):
    queryset = Service.objects.all().order_by('popular')
    template_name = "booking/services.html"


class AppointmentList(generic.ListView):
    queryset = Appointment.objects.all().order_by('date_appo')
    template_name = "booking/my-appointments.html"