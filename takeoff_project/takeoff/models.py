from django.db import models
from datetime import datetime

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
class Place(models.Model):
    city = models.CharField(max_length=20)
    airport = models.CharField(max_length=30)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.city
class Date(models.Model):
    month = models.CharField(max_length=15)
    day = models.IntegerField()
    year = models.IntegerField(default = 2022)

    def __str__(self):
        return self.day
class Flight(models.Model):
    origin = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="arrivals")
    departDay = models.ManyToManyField(Date, related_name="flight")
    departTime = models.TimeField(auto_now=False, auto_now_add=False)
    arrivalTime = models.TimeField(auto_now=False, auto_now_add=False)
    airline = models.CharField(max_length=20)
    duration = models.DurationField(null=True)

    def __str__(self):
        return self.airline
class Ticket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bookings", blank=True, null=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets", blank=True, null=True)
    flightDepartDate = models.DateField(blank=True, null=True)
    flightArrivalDate = models.DateField(blank=True, null=True)
    bookingDate = models.DateTimeField(default=datetime.now)
    email = models.EmailField(max_length=30, blank=True)
    phone = models.CharField(max_length=13,blank=True)
    flightFare = models.FloatField(blank=True,null=True)
    refNumber = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.refNumber
class Passenger(models.Model):
    firstName = models.CharField(max_length=20, blank=True)
    lastName = models.CharField(max_length=20, blank=True)
    passenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flights")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="passengers")

    def __str__(self):
        return self.firstName
