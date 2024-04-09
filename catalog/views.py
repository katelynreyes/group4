from django.shortcuts import render
from django.views import generic
from .models import Pet
#from django.contrib.auth.mixins import LoginRequiredMixin


# Existing import statements...

def index(request):
    """View function for home page of site."""
    context = {'test': 'Testing'}
    return render(request, 'catalog/index.html', context=context)


def volunteer_view(request):
    return render(request, 'catalog/volunteer.html')


def volunteer(request):
    return render(request, 'catalog/volunteer.html')


class PetDetailView(generic.DetailView):
    model = Pet


class PetListView(generic.ListView):
    model = Pet

