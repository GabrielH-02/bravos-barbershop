from django.shortcuts import render
from django.views import generic
from .models import Service


class ServiceList(generic.ListView):
    queryset = Service.objects.all().order_by('popular')
    template_name = "booking/services.html"