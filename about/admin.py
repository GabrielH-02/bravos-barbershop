from django.contrib import admin
from .models import About, JobStatus, Stylist, HairRequest

# Register your models here.
admin.site.register(About)


admin.site.register(JobStatus)


admin.site.register(Stylist)


admin.site.register(HairRequest)
