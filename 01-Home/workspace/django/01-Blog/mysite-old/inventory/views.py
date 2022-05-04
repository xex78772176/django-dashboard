from django.shortcuts import render
from .models import inventory
from django.db.models import Count

def index(request):
    inventories = inventory.objects.all()
    context = {'inventories' : inventories}
    return render(request, 'inventory/index.html',context)



# Create your views here.
def price(request):
    inventories = inventory.objects.filter(unit_price__gte = 10000.0)
    context = {'inventories' : inventories} # Store the data in "context" dictionaries
    return render(request, 'inventory/price.html', context)

def user(request):
    inventories = inventory.objects.values('end_user').annotate(total=Count('end_user')).order_by('end_user')
    locations = inventory.objects.values('Location').annotate(total=Count('Location')).order_by('Location')
    context = {'inventories' : inventories, 'locations':locations} # Store the data in "context" dictionaries
    return render(request, 'inventory/user.html', context)

def year(request):
    inventories = inventory.objects.filter(date_purchase__year__lte = (2021-5))
    context = {'inventories' : inventories} # Store the data in "context" dictionaries
    return render(request, 'inventory/year.html', context)

