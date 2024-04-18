from django.contrib import admin
<<<<<<< HEAD
from catalog.models import Pet, Appointment  # Assuming PetInstance is not needed, or is imported if it is
from django.utils import timezone
from datetime import timedelta
from datetime import date


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


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'date_of_birth', 'available_for_adoption')
    list_filter = ('available_for_adoption', 'breed')
    search_fields = ('name', 'breed')

    def get_age(self, obj):
        if obj.date_of_birth:
            return date.today().year - obj.date_of_birth.year
        else:
            return 'Unknown'

    get_age.short_description = 'Age'  # Provides header for the column


# Register the admin class with the associated model
admin.site.register(Appointment, AppointmentAdmin)

# If PetInstance needs to be registered, and you have a PetInstanceAdmin defined, use a similar approach:
# admin.site.register(PetInstance, PetInstanceAdmin)
=======
from catalog.models import Pet, PetInstance

# Register your models here.
admin.site.register(Pet)
admin.site.register(PetInstance)

>>>>>>> 33e8028c489bc62bb065715056b7905dbaaacb83
