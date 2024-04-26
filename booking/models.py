from django.db import models
from django.contrib.auth.models import User
from about.models import JobStatus, Stylist


class Service(models.Model):
    """
    Model to store information about services provided by the barber shop.
    
    **Fields**

        popular (IntegerField): The popularity score of the service.
        title (CharField): The title of the service.
        price (DecimalField): The price of the service.
        level (ForeignKey): The qualification level required for the service, linked to the JobStatus model.

    """

    popular = models.IntegerField()
    title = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.ForeignKey(
        JobStatus, on_delete=models.CASCADE, to_field='qualif_level'
    )

    class Meta:
        ordering = ['popular']

    def __str__(self):
        return self.title


class AppointmentTime(models.Model):
    """
    Model to store appointment times.
    
    **Fields**
    
        title (TimeField): The time of the appointment.

    """
    title = models.TimeField(unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title.strftime('%H:%M')


class Appointment(models.Model):
    """
    Model to store information about appointments.
    
    **Fields**
    
        author (ForeignKey): The user who made the appointment, linked to the User model.
        title (ForeignKey): The type of service for the appointment, linked to the Service model.
        stylist (ForeignKey): The stylist assigned to the appointment, linked to the Stylist model.
        date_appo (DateField): The date of the appointment.
        time_appo (ForeignKey): The time of the appointment, linked to the AppointmentTime model.

    """

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="client"
    )
    title = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='servicetype'
    )
    stylist = models.ForeignKey(
        Stylist, on_delete= models.CASCADE, to_field='stylist_id'
    )
    date_appo = models.DateField()
    time_appo = models.ForeignKey(
        AppointmentTime, on_delete=models.CASCADE, related_name='appointmenttime'
    )

    class Meta:
        ordering = ['date_appo', 'time_appo']

    def __str__(self):
        return f"{self.title} for {self.author} with {self.stylist} on {self.date_appo} at {self.time_appo}"