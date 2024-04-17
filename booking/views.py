from django.shortcuts import render
from django.views import generic
from .models import Service

# Create your views here.
class ServiceList(generic.ListView):
    queryset = Service.objects.all()
    template_name = "service_list.html"