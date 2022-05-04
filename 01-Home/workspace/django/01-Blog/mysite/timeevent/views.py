from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from iot.models import Venue_Event,Event
from django.db import models

# Create your views here.
def index(request):
    iotevents = Event.objects.all()
    events = Venue_Event.objects.all() # date_created descending order
    venues = Venue_Event.objects.order_by().values('Venue').distinct()
    
    timestarts = Venue_Event.objects.order_by().values('Timestart').distinct()
    timeends= Venue_Event.objects.order_by().values('Timeend').distinct()
    dates = Venue_Event.objects.order_by().values('Date').distinct()

    


    context = {'events' : events,
    'venues': venues,
    'timestarts': timestarts,
    'timeends': timeends,
    'dates': dates,
    'iotevents' : iotevents,
    }
    
    return render(request, 'timeevent/index.html', context) # Pass the context to HTML template


