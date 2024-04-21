from django.contrib import admin
from .models import Service, AppointmentTime, Appointment
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):
    list_display = ('title', 'price', 'level', 'popular',)
    search_fields = ['title', 'level']
    list_filter = ('level',)



@admin.register(AppointmentTime)
class AppointmentTimeAdmin(SummernoteModelAdmin):
    list_display = ('title',)
    search_fields = ['title']
    list_filter = ('title',)



@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):
    list_display = ('author', 'stylist', 'title', 'date_appo', 'time_appo',)
    search_fields = ['author', 'stylist', 'title', 'date_appo']
    list_filter = ('date_appo',)

