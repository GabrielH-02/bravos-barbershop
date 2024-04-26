from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Service, Appointment


# Service list view to display the service's the barber provides
class ServiceList(LoginRequiredMixin, generic.ListView):
    """
    Display the list of services provided by the barber.
    
    Requires login.

    **Context**

    ``queryset``
        Queryset of all services ordered by popularity.
    
    **Template:**

    :template:`booking/services.html`

    """
    queryset = Service.objects.all().order_by('popular')
    template_name = "booking/services.html"


# CREATE + READ: Appointment view for creation and read of appointments
@login_required
def my_appointments(request):
    """
    Renders the 'My Appointments' page.
    
    Allows users to view their appointments and create new appointments.

    Requires login.

    **Context**

    ``appointments``
        Queryset of appointments belonging to the current user.
    ``appointment_form``
        Form object for creating new appointments.

    **Template:**

    :template:`booking/my-appointments.html`

    """
    if request.method == "POST":
        appointment_form = AppointmentForm(data=request.POST)
        if appointment_form.is_valid():
            appointment = appointment_form.save(commit=False)
            appointment.author = request.user
            appointment.save()
            messages.success(request, "You have made your appointment! We look forward to seeing you.")
            return redirect("appointments")

    appointments = Appointment.objects.filter(author=request.user).order_by('date_appo')
    appointment_form = AppointmentForm()

    return render(
        request,
        "booking/my-appointments.html",
        {
            "appointments": appointments,
            "appointment_form": appointment_form
        },
    )


# UPDATE: Appointment view for editing of appointments
@login_required
def appointment_edit(request, appointment_id):
    """
    Edit an appointment.

    Requires login.

    **Context**

    ``appointment``
        The appointment instance to be edited.
    ``appointment_form``
        Form object for editing the appointment.

    """
    if request.method == "POST":

        appointment = get_object_or_404(Appointment, pk=appointment_id)
        appointment_form = AppointmentForm(data=request.POST, instance=appointment)
        
        if appointment_form.is_valid() and appointment.author == request.user:
            appointment = appointment_form.save(commit=False)
            appointment.save()
            messages.add_message(request, messages.SUCCESS, 'Appointment Updated!')
        else:
                messages.add_message(request, messages.ERROR, 'Error updating appointment')
        
    return HttpResponseRedirect(reverse('appointments'))


# DELETE: Appointment view for deletion of appointments
@login_required
def appointment_delete(request, appointment_id):
    """
    Delete an appointment.

    Requires login.

    **Context**

    ``appointment``
        The appointment instance to be deleted.

    """
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    if appointment.author == request.user:
        appointment.delete()
        messages.add_message(request, messages.SUCCESS, 'Appointment deleted!')
    else:
        messages.add_message(request, messages.ERROR,'You can only delete your own appointments!')

    return HttpResponseRedirect(reverse('appointments'))