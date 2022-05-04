from django.shortcuts import render
#from . import iot_mqtt
from .models import Event
from . import iot_mqtt
# Create your views here.
def index(request):
    events = Event.objects.all() # date_created descending order
    items2 = Event.objects.filter(loc ='W311-Z2')
    context = {'events' : events} # Store the data in "context" dictionaries
    return render(request, 'iot/index.html', context) # Pass the context to HTML template
def W311H1(request):
    items1 = Event.objects.filter(loc ='W311-H1')
    context = {'items1' : items1} # Store the data in "context" dictionaries
    return render(request, 'iot/w311H1.html', context) # Pass the context to HTML template

def W311H3(request):
    items = Event.objects.filter(loc ='W311-H3')
    context = {'items' : items} # Store the data in "context" dictionaries
    return render(request, 'iot/w311-H3.html', context) # Pass the context to HTML template
def W311a(request):
    items2 = Event.objects.filter(loc ='W311A')
    context = {'items2' : items2} # Store the data in "context" dictionaries
    return render(request, 'iot/W311a.html', context) # Pass the context to HTML template
def W311b(request):
    items3 = Event.objects.filter(loc ='W311B')
    context = {'items3' : items3} # Store the data in "context" dictionaries
    return render(request, 'iot/W311-b.html', context) # Pass the context to HTML template
def W311H2(request):
    items3 = Event.objects.filter(loc ='W311-H2')
    context = {'items3' : items3} # Store the data in "context" dictionaries
    return render(request, 'iot/W311-H2.html', context) # Pass the context to HTML template
def W311DZ1(request):
    items4 = Event.objects.filter(loc ='W311D-Z1')
    context = {'items4' : items4} # Store the data in "context" dictionaries
    return render(request, 'iot/W311D-Z1.html', context) # Pass the context to HTML template    
def W311Z2(request):
    items5 = Event.objects.filter(loc ='W311D-Z2')
    context = {'items5' : items5} # Store the data in "context" dictionaries
    return render(request, 'iot/W311D-Z2.html', context) # Pass the context to HTML template    
