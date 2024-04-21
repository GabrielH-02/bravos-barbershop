from django.db import models
from django.contrib.auth.models import User
from about.models import JobStatus, Stylist


class Service(models.Model):
    popular = models.IntegerField()
    title = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.ForeignKey(
        JobStatus, on_delete=models.CASCADE, to_field='qualif_level'
    )

    class Meta:
        ordering = ['popular']

    def __str__(self):
        return f"Service: {self.title} at the price of {self.price}, only a barber with qualifcations of {self.level} can do it"


class AppointmentTime(models.Model):
    title = models.TimeField(unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"Appointment time: {self.title}"


class Appointment(models.Model):
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
        return f"Appointment: {self.author} with {self.stylist} on {self.date_appo} at {self.time_appo}"
