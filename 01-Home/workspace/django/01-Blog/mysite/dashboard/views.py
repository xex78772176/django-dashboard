from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from iot.models import Event,Venue_Event
#import pandas as pd
# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def temp_data(request):
    events = Event.objects.all()
    data = serializers.serialize('json', events)
   #Translating Django models into JSON formats
    return JsonResponse(data, safe=False)
