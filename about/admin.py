from django.contrib import admin
from .models import About, JobStatus, Stylist, HairRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('updated_on',)
    search_fields = ['updated_on']
    list_filter = ('updated_on',)
    summernote_fields = ('content',)


@admin.register(JobStatus)
class JobStatusAdmin(SummernoteModelAdmin):
    list_display = ('title', 'qualif_level',)
    search_fields = ['title']
    list_filter = ('title',)


@admin.register(Stylist)
class StylistAdmin(SummernoteModelAdmin):
    list_display = ('stylist_id', 'first_name', 'last_name', 'job_title',)
    search_fields = ['stylist_id', 'first_name', 'last_name', 'job_title']
    list_filter = ('job_title',)


@admin.register(HairRequest)
class HairRequestAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_on', 'read',)
    search_fields = ['name', 'email', 'subject', 'created_on']
    list_filter = ('read', 'created_on',)
    summernote_fields = ('message',)

# Register your models here.

