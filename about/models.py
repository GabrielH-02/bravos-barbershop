from django.db import models

# Create your models here.


class About(models.Model):
    """
    Stores a single about me text field.
    """
    profile_image = models.CharField(max_length=25) #CloudinaryField
    updated_on = models.DateField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.updated_on

class JobStatus(models.Model):
    """
    Stores a single job title field.
    """
    title = models.CharField(max_length=25, unique=True)
    qualif_level = models.IntegerField(unique=True)


class Stylist(models.Model):
    """
    Stores a single profile of a stylist
    """
    stylist_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    stylist_image = models.CharField(max_length=25) #CloudinaryField
    job_title = models.ForeignKey(
        JobStatus, on_delete=models.CASCADE, to_field='title'
    )

    def __str__(self):
        return f"{self.stylist_id} is a {self.job_title}"

class HairRequest(models.Model):
    """
    Stores a single hair request message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Hair Request from {self.name}"