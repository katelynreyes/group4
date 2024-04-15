from django.contrib import admin
from catalog.models import Pet, PetInstance
from .models import Appointment
from django.utils import timezone
from datetime import timedelta


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_date', 'client_name', 'appointment_type')

    # Function to filter upcoming appointments within, say, the next 30 days
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Get current date and date for 30 days in the future
        now = timezone.now()
        upcoming = now + timedelta(days=30)
        # Filter appointments between now and the upcoming date
        return qs.filter(appointment_date__range=(now, upcoming))


# Register the admin class with the associated model
admin.site.register(Appointment, AppointmentAdmin)

admin.site.register(Pet)
admin.site.register(PetInstance)
