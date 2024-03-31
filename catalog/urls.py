from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.home, name='home'),  # The main page
    path('volunteer/', views.volunteer, name='volunteer'),  # Volunteer information page
]
