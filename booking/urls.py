from . import views
from django.urls import path

urlpatterns = [
    path('', views.ServiceList.as_view(), name='home'),
]