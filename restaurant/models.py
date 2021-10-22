from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone



class Booking(models.Model):
    
    user = models.CharField(max_length=15)
    customer_name = models.CharField(max_length=15, default=1)
    reservation_date = models.DateTimeField()
    def validate_date(reservation_date):
        if reservation_date < timezone.now():
            print('Date cannot be in the past!')
            raise ValidationError("Date cannot be in the past") # from Stack Overflow  
    reservation_date = models.DateTimeField(null=True, blank=True, validators=[validate_date])
    number_of_customers = models.IntegerField(default=1)
    phone_number = models.CharField(max_length=15)
    
    MENU_CATEGORY = [
        ('A la carte', 'A la carte'),
        ('House special', 'Special'),
        ('Vegetarian', 'Vegetarian'),
        ('Vegan', 'Vegan'),
    ]
    menu = models.CharField(max_length=13, choices=MENU_CATEGORY)
    # class Meta:
    #     unique_together = ("user", "customer_name", "reservation_date", "number_of_customers", "menu")


    def __str__(self):
        return f' Customer {self.customer} has made a booking for {self.number_of_customers} customers between {self.start_date} with menu {self.menu}'

