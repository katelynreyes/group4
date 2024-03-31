from django.shortcuts import render


# Existing import statements...
# from .models import Pet, PetInstance

def index(request):
    """View function for home page of site."""
    context = {'test': 'Testing'}
    return render(request, 'catalog/index.html', context=context)


def home(request):
    """View function for home page of site."""
    # Context can contain any data you want to pass to the template
    return render(request, 'catalog/base.html', {})  # Changed 'home.html' to 'base.html'


def volunteer(request):  # Renamed from volunteer_info to volunteer
    """View function for the volunteer page."""
    return render(request, 'catalog/volunteer.html', {})  # The context is empty for now


def volunteer(request):
    # Render the volunteer_info.html template
    return render(request, 'catalog/volunteer_info.html')
