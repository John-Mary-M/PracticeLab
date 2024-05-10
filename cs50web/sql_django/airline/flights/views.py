from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger
# Create your views here.
def index(request):
    '''returns a list of all flights'''
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })

def flight(request, flight_id):
    '''takes fligt_id and returns flight details'''
    # get flight_id
    flight = Flight.objects.get(id=flight_id)
    return render(request,  'flights/flight.html', {
        'flight': flight,
        'passengers': flight.passengers.all(),
        # get passengers who are not on the flight
        'non_passengers': Passenger.objects.exclude(flights = flight).all()
    })

def book(request, flight_id):
    '''takes a flight_id,
    and books a flight.
    '''
    if request.method == 'POST':
        # get flight who's primary key (pk) is flight_id
        flight = Flight.objects.get(pk=flight_id)
        # get passenger information from the form they submit where passenger is the name of the input field pk here is the primary id of the passenger thus using int()
        passenger = Passenger.objects.get(pk= int(request.POST['passenger']))

        # access passenger flights and add flight
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight', args=(flight_id,)))
