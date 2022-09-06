from django.contrib import admin
from .models import User,Place,Date,Flight,Ticket,Passenger

admin.site.register(User)
admin.site.register(Place)
admin.site.register(Date)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Passenger)
