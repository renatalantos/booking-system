"""reservesmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restaurant.views import get_booking_form, add_booking, view_booking, edit_booking, delete_booking
from restaurant import views


APP_NAME = "restaurant"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_booking_form, name='book'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('view_booking/', views.view_booking, name='view_booking'),
    path('edit/<restaurant_id>', views.edit_booking, name='edit'),
    path('delete_booking/', views.delete_booking, name='delete_booking'),
]
