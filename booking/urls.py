from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # path('', views.ServiceList.as_view(), name='home'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

]