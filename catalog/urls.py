from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), #the main page
    path('pet_list/', views.PetListView.as_view(), name='pet_list'), # Pet list page
    path('pet_detail/<int:pk>', views.PetDetailView.as_view(), name='pet_detail'),
    path('volunteer/', views.volunteer, name='volunteer'),  # Volunteer information page
]
