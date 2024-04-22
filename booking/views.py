from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service, Appointment


class ServiceList(LoginRequiredMixin, generic.ListView):
    queryset = Service.objects.all().order_by('popular')
    template_name = "booking/services.html"


class AppointmentList(LoginRequiredMixin, generic.ListView):
    queryset = Appointment.objects.all().order_by('date_appo')
    template_name = "booking/my-appointments.html"
