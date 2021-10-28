from django.urls import path
from restaurant import views


urlpatterns = [
    path('', views.view_home, name='home'),
    path('menu/', views.view_menu, name='menu'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('view_booking/', views.view_booking, name='view_booking'),
    path('edit/<booking_id>', views.edit_booking, name='edit_booking'),
    path('delete/<booking_id>', views.delete_booking, name='delete_booking'),
    path('booking_deleted/', views.no_booking_after_delete, name='no_booking_after_delete'),
    path('contact', views.contact, name='contact'),
]
