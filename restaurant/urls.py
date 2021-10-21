from . import views
from django.urls import path
from restaurant import views


urlpatterns=[
    path('', views.add_booking, name='home'),
    path('view_booking/', views.view_booking, name='view_booking'),
    path('edit/<booking_id>', views.edit_booking, name='edit'),
    path('delete/<booking_id>', views.delete_booking, name='delete_booking'),
   
]