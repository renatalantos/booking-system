from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    TABLE_CATEGORY = [
        ('Inside', 'Inside'),
        ('Outside', 'Outside'),
    ]
    category = models.CharField(max_length=7, choices=TABLE_CATEGORY)
    table_number = models.IntegerField()
    seats = models.IntegerField()

    def __str__(self):
        return f' Table number {self.table_number} {self.category} with {self.seats} seats'
        

