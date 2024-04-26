from django.shortcuts import render
from django.contrib import messages
from .models import About, Stylist
from .forms import HairRequestForm


# CREATE + READ: About view for displaying barbershop details and creation of hair request
def about_me(request):
    """
    Renders the 'About' page.

    Renders the About page, allowing users to view information about the barbershop,
    the stylists, and create and submit a personalized hair request.

    If the request method is POST, processes the hair request form submitted by the user.
    If the form is valid, saves the hair request and displays a success message.
    
    **Context**

    ``about``
        The latest About instance, containing information about the salon.
    ``stylists``
        Queryset of all stylists.
    ``hairrequest_form``
        Form object for submitting hair requests.

    **Template:**

    :template:`about/about.html`

    """
    if request.method == "POST":
        hairrequest_form = HairRequestForm(data=request.POST)
        if hairrequest_form.is_valid():
            hairrequest_form.save()
            messages.add_message(request, messages.SUCCESS, "You're Hair request has been received! We will contact you shortly ...")

    about = About.objects.all().order_by('-updated_on').first()
    stylists = Stylist.objects.all()
    hairrequest_form = HairRequestForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "stylists": stylists,
            "hairrequest_form": hairrequest_form

        },
    )