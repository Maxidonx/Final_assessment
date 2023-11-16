from django.db import models
from django.utils import timezone


# Create your models here.

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    BookingDate = models.DateTimeField(default=timezone.now)
    no_of_guest = models.IntegerField(null=True)

    def __str__(self): 
        return self.first_name

class Menu(models.Model):
    name = models.CharField(max_length=200) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    menu_item_description = models.TextField(max_length=1000, default='') 
    inventory = models.IntegerField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'