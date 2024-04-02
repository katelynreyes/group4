from .models import Pet, PetInstance
from django.shortcuts import render
from django.views import generic
# Existing import statements...


def index(request):
    """View function for home page of site."""
    num_pets = Pet.objects.all().count()
    num_instances = PetInstance.objects.all().count()

    # Available pets (status = 'a')
    num_instances_available = PetInstance.objects.filter(status__exact='a').count()

    #
    context = {
        'num_pets': num_pets,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


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


class PetDetailView(generic.DetailView):
    model = Pet

class PetListView(generic.ListView):
    model = Pet
    
