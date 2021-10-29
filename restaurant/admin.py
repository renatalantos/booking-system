"""
Representation of the booking model in the admin interface.
"""
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    """
    Class registered to represent model in admin database.
    """
    list_display = ('user', 'customer_name',
                    'reservation_date_and_time',
                    'phone_number',
                    'number_of_customers')
    search_fields = ('customer_name',
                     'reservation_date_and_time',
                     'phone_number')
    list_filter = ('customer_name',
                   'reservation_date_and_time',
                   'phone_number')
