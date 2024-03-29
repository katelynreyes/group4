# from .models import Pet, PetInstance
from django.shortcuts import render


def index(request):
    """View function for home page of site."""
    context={'test':'Testing'}
    return render(request, 'index.html', context=context)

from django.shortcuts import render


