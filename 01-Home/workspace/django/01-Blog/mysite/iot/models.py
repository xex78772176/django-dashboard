from django.db import models
import datetime
# Create your models here.
class Event(models.Model):
    #Fields
    create_time = models.DateTimeField(auto_now_add=True)
    node_id = models.CharField(max_length=2)
    loc = models.CharField(max_length=10)
    temp = models.DecimalField(max_digits=5, decimal_places=2)
    hum = models.DecimalField(max_digits=5, decimal_places=2)
    light = models.DecimalField(max_digits=5, decimal_places=2)
    snd = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return 'Event #{}'.format(self.node_id)
class Venue_Event(models.Model):
    
    Venue = models.CharField(max_length = 10)
    Date = models.DateField()
    Timestart = models.TimeField()
    Timeend = models.TimeField()
    Event = models.CharField(max_length = 10)
    Instructor = models.CharField(max_length = 20)
    temp= models.DecimalField(decimal_places=2, max_digits=5)
    hum = models.DecimalField(decimal_places=2, max_digits=5)
    light= models.DecimalField(decimal_places=2, max_digits=5)
    snd=models.DecimalField(decimal_places=2, max_digits=5)


    def __str__(self):
        return 'Venue Event #{}'.format(self.id)


# Create your models here.
