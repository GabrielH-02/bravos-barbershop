from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Model to store information about the salon.
    
    **Fields**

        profile_image (CloudinaryField): The image associated with the salon profile.
        updated_on (DateTimeField): The date and time when the about section was last updated.
        content (TextField): The text content of the about section.

    """
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return f"This about us section was created on {self.updated_on}"


class JobStatus(models.Model):
    """
    Model to store information about job titles and qualification levels.
    
    **Fields**

        title (CharField): The title of the job.
        qualif_level (IntegerField): The qualification level associated with the job title.
    
    """
    title = models.CharField(max_length=25, unique=True)
    qualif_level = models.IntegerField(unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Stylist(models.Model):
    """
    Model to store information about stylists.
    
    **Fields**

        stylist_id (CharField): The unique identifier for the stylist.
        first_name (CharField): The first name of the stylist.
        last_name (CharField): The last name of the stylist.
        stylist_image (CloudinaryField): The image associated with the stylist.
        job_title (ForeignKey): The job title of the stylist, linked to the JobStatus model.

    """
    stylist_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    stylist_image = CloudinaryField('image', default='placeholder')
    job_title = models.ForeignKey(
        JobStatus, on_delete=models.CASCADE, to_field='title'
    )

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.stylist_id


class HairRequest(models.Model):
    """
    Model to store information about hair requests.
    
    **Fields**
    
        created_on (DateTimeField): The date and time when the hair request was created.
        name (CharField): The name of the person making the hair request.
        email (EmailField): The email address of the person making the hair request.
        phone_number (CharField): The phone number of the person making the hair request.
        subject (CharField): The subject of the hair request.
        message (TextField): The message content of the hair request.
        read (BooleanField): Indicates whether the hair request has been read.

    """
    created_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Hair Request from {self.name}"