from django.db import models

# Create your models here.
class inventory(models.Model):
    inventory_no = models.TextField()
    Location = models.TextField()
    end_user = models.TextField()
    description = models.TextField()
    brand = models.TextField()
    unit_price = models.FloatField()
    date_purchase = models.DateTimeField()


def __str__(self):
    return 'inventory #{}'.format(self.id)