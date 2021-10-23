from django.contrib import admin
from .models import Booking
from django.contrib.admin import ModelAdmin
# Register your models here.



@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    list_display = ('user', 'customer_name', 'reservation_date_and_time', 'phone_number', 'number_of_customers')
    search_fields = ('customer_name', 'reservation_date_and_time', 'phone_number')
    list_filter = ('customer_name', 'reservation_date_and_time', 'phone_number')


