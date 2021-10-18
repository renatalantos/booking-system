from django.db import models
from django.contrib.auth.models import User



class Booking(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    number_of_customers = models.IntegerField(default=1)
    phone_number = models.CharField(max_length=15)
    
    MENU_CATEGORY = [
        ('A la carte', 'A la carte'),
        ('House special', 'Special'),
        ('Vegetarian', 'Vegetarian'),
        ('Vegan', 'Vegan'),
    ]
    menu = models.CharField(max_length=13, choices=MENU_CATEGORY)


    def __str__(self):
        return f' Customer {self.user} has made a booking for {self.number_of_customers} customers between {self.start_date} and {self.end_date} with menu {self.menu}'

