from django.urls import path
from .views import BookingList, BookingView
from . import views

app_name = 'restaurant'

urlpatterns = [
    
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='booking_view'),
 

]
