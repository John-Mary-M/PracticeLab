from django.db import models

# Create your models here.
class Airport(models.Model):
    '''represents airports in the different cities'''
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        '''returns string rep of the Airport model'''
        return f'{self.city} ({self.code})'

class Flight(models.Model):
    '''table that represents flights'''
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField()

    def __str__(self):
        '''returns string representation of the model'''
        return f'{self.origin} to {self.destination} duration: {self.duration}'
    
class Passenger(models.Model):
    '''represents passengers on the flight'''
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')

    def __str__(self):
        '''returns string representation of passenger'''
        return f'{self.first} {self.last}'