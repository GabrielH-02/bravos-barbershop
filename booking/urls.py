from . import views
from django.urls import path


urlpatterns = [
    path('our-services/', views.ServiceList.as_view(), name='services'),
    path('my-appointments/', views.my_appointments, name='appointments'),
    
]