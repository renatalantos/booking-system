from django.contrib import admin
from .models import Table, Booking, Menu, AvailableTable
# Register your models here.


admin.site.register(Table)
admin.site.register(Booking)
admin.site.register(Menu)
admin.site.register(AvailableTable)
