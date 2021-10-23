from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone



class Booking(models.Model):
    
    user = models.CharField(max_length=15)
    customer_name = models.CharField(max_length=15, null=True)
    reservation_date_and_time = models.DateTimeField()
    def validate_date(reservation_date_and_time):
        if reservation_date_and_time < timezone.now():
            print('Date cannot be in the past!')
            raise ValidationError("Date cannot be in the past") # from Stack Overflow  
    reservation_date_and_time = models.DateTimeField(null=True, blank=True, validators=[validate_date])
    number_of_customers = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=15)
    
    
    class Meta:
        unique_together = ("user", "customer_name", "reservation_date_and_time", "number_of_customers")


    def __str__(self):
        return f' Customer {self.customer_name} has made a booking for {self.number_of_customers} customers for {self.reservation_date_and_time}.'

