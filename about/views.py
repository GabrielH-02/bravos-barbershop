from django.shortcuts import render
from .models import About
from django.contrib import messages
from .forms import HairRequestForm

def about_me(request):
    """
    Renders the About page
    """
    if request.method == "POST":
        hairrequest_form = HairRequestForm(data=request.POST)
        if hairrequest_form.is_valid():
            hairrequest_form.save()
            messages.add_message(request, messages.SUCCESS, "You're Hair request has been received! We will contact you shortly ...")

    about = About.objects.all().order_by('-updated_on').first()
    hairrequest_form = HairRequestForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "hairrequest_form": hairrequest_form

        },
    )