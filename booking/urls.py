from django.urls import path
from . import views


urlpatterns = [
    path('our-services/', views.ServiceList.as_view(), name='services'),
    path('my-appointments/', views.my_appointments, name='appointments'),
    path('edit_appointment/<int:appointment_id>/', views.appointment_edit, name='appointment_edit'),
    path('delete_appointment/<int:appointment_id>/', views.appointment_delete, name='appointment_delete'),
]
