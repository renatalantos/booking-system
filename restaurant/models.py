from django.db import models
from django.contrib.auth.models import User

class AvailableTable(models.Model):
    available_tables = models.IntegerField(default=1)
    def __str__(self):
        return f'{self.available_tables}'

class Table(models.Model):
    
    TABLE_CATEGORY = [
        ('For 2', 'Couple'),
        ('For 4', 'Party of 4'),
        
    ]
    category = models.CharField(max_length=7, choices=TABLE_CATEGORY)
    tables_available = models.ForeignKey(AvailableTable, on_delete=models.CASCADE, related_name='tables_available')
    table_number = models.IntegerField()
 


    def __str__(self):
        return f' Table number {self.table_number} for a {self.category} tables available {self.tables_available}'

class Menu(models.Model):
    MENU_CATEGORY = [
        ('A la carte', 'A la carte'),
        ('House special', 'Special'),
        ('Vegetarian', 'Vegetarian'),
        ('Vegan', 'Vegan'),
    ]
    menu_category = models.CharField(max_length=13, choices=MENU_CATEGORY)
    def __str__(self):
        return f' {self.menu_category}'

class Booking(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reserved_table')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    number_of_customers = models.IntegerField()
    number_of_tables = models.IntegerField()

    def __str__(self):
        return f' Customer {self.customer} has booked{self.table} {self.number_of_tables} tables for {self.number_of_customers} customers between {self.start_date} and {self.end_date} with menu {self.menu}'
