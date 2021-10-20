from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking



from .forms import BookingForm


def get_booking_form(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'restaurant/booking_form.html', context)



def add_booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request, "Success")
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
    return render (request, 'restaurant/view_booking.html', context)

def edit_booking(request, restaurant_id):
    booking = get_object_or_404(Booking, id = restaurant_id)
    if request.method=='POST':
        form=BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            #messages.success(request, "Success")
            return redirect('view_booking')
    form=BookingForm(instance=booking)    
    context= {
        'form': form
        }  
    return render (request, 'restaurant/edit_booking.html', context)

def delete_booking(request):
    return render (request, 'restaurant/delete_booking.html')  
