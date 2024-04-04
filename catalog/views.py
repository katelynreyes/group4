from .models import Pet, PetInstance
from django.shortcuts import render
from django.views import generic
# Existing import statements...

def index(request):
    """View function for home page of site."""
    context = {'test': 'Testing'}
    return render(request, 'catalog/index.html', context=context)

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
    
