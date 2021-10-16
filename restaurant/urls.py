from django.urls import path
from .views import MenuList, TableList, BookingList
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('table_list/', TableList.as_view(), name='TableList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('menu_list/', MenuList.as_view(), name='MenuList'),
  

]
