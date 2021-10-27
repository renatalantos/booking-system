from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.core.exceptions import *




def view_home(request):
    return render(request, 'restaurant/index.html')

def view_menu(request):
    return render(request, 'restaurant/menu.html')

def add_booking(request):
   
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_booking')            

    form=BookingForm()    
    context= {
        'form': form
        }    
    return render(request, 'restaurant/add_booking.html', context)

def view_booking(request):
    
    bookings = Booking.objects.all()
    context= {
        'bookings': bookings
    }
    return render(request, 'restaurant/view_booking.html', context)




def edit_booking(request, booking_id):
    book = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('view_booking')
    
    form = BookingForm(instance=book)
    context = {
        'form': form
    }
    return render(request, 'restaurant/edit_booking.html', context)

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if booking.delete():
            return redirect('view_booking')
    
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'restaurant/delete_booking.html', context)    


def contact(request):
    return render(request, 'restaurant/contact.html')
