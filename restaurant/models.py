from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    
    TABLE_CATEGORY = [
        ('Inside', 'Inside'),
        ('Outside', 'Outside'),
    ]
    category = models.CharField(max_length=7, choices=TABLE_CATEGORY)
    table_number = models.IntegerField()
    seats = models.IntegerField(default=2)
    


    def __str__(self):
        return f' Table number {self.table_number} {self.category} with {self.seats} seats'
        

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reserved_table')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    number_of_customers = models.IntegerField()
    number_of_tables = models.IntegerField()

    def __str__(self):
        return f' Customer {self.customer} has booked{self.table} {self.number_of_tables} tables for {self.number_of_customers} customers between {self.start_date} and {self.end_date}'
