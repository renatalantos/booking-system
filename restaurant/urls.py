from django.urls import path
from .views import BookingListView, BookingFormView
from . import views

app_name = 'restaurant'

urlpatterns = [
    
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('book/', BookingFormView.as_view(), name='booking_view'),
 
]
