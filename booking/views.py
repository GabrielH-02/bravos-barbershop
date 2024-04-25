from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Service, Appointment



class ServiceList(LoginRequiredMixin, generic.ListView):
    queryset = Service.objects.all().order_by('popular')
    template_name = "booking/services.html"


@login_required
def my_appointments(request):
    """
    Renders the My appointments page
    """
    if request.method == "POST":
        appointment_form = AppointmentForm(data=request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.author = request.user
            appointment.save()
            messages.success(request, "You have made your appointment! We look forward to seeing you.")
            return redirect("appointments")

    appointments = Appointment.objects.all().order_by('date_appo')
    appointment_form = AppointmentForm()

    return render(
        request,
        "booking/my-appointments.html",
        {
            "appointments": appointments,
            "appointment_form": appointment_form
        },
    )

@login_required
def appointment_delete(request, appointment_id):
    """
    view to delete appointment 
    """
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    if appointment.author == request.user:
        appointment.delete()
        messages.add_message(request, messages.SUCCESS, 'Appointment deleted!')
    else:
        messages.add_message(request, messages.ERROR,'You can only delete your own appointments!')

    return HttpResponseRedirect(reverse('appointments'))