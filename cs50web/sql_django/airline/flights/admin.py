from django.contrib import admin

from .models import Flight, Airport, Passenger



'''Customizing the django admin interface to show more information about flights and passengers after which I register the new custom functions along with the models. 

Notice that filter_horizontal takes a tuple or list hence living a comma after the flights
'''
class FlightAdmin(admin.ModelAdmin):
    '''Shows more information about a flight'''
    list_display = ('id', 'origin', 'destination', 'duration')

class PassengerAdmin(admin.ModelAdmin):
    '''Edits passengers information '''
    filter_horizontal = ('flights',)

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)