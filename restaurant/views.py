"""
Views to create application logic.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


def handler404(request, *args, **argv):
    """
    Function to enable customizing 404 error
    page in production environment if booking is not found.
    """
    form = BookingForm()
    context = {
        'form': form
        }
    response = render(request, 'restaurant/not_found.html', context)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    """
    Function to enable customizing 404 error page
    in production environment if booking is duplicate.
    """
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    response = render(request, 'restaurant/duplicate_booking.html', context)
    response.status_code = 500
    return response


def view_home(request):
    """
    Function enables user to view the home page.
    """
    return render(request, 'restaurant/index.html')


def view_menu(request):
    """
    Function enables user to view the menu page.
    """
    return render(request, 'restaurant/menu.html')


def contact(request):
    """
    Function enables user to view the menu page.
    """
    return render(request, 'restaurant/contact.html')


def add_booking(request):
    """
    Function enables user to make a booking
    and add it to the database.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking successful.')
            return redirect('view_booking')
    form = BookingForm()
    context = {
        'form': form
        }
    return render(request, 'restaurant/add_booking.html', context)


def view_booking(request):
    """
    Function enables user to view a booking after
    it has been made and added to the database.
    """
    bookings = Booking.objects.all()[:1]
    context = {
        'bookings': bookings
    }
    return render(request, 'restaurant/view_booking.html', context)


def edit_booking(request, booking_id):
    """
    Function enables user to edit a booking after
    it has been made and added to the database.
    """
    book = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking has been updated.')
        return redirect('view_booking')
    form = BookingForm(instance=book)
    context = {
        'form': form
    }
    return render(request, 'restaurant/edit_booking.html', context)


def delete_booking(request, booking_id):
    """
    Function enables user to delete a booking after
    it has been made and added to the database.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if booking.delete():
            messages.success(request, 'Your booking has been deleted.')
            return redirect('no_booking_after_delete')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'restaurant/delete_booking.html', context)


def no_booking_after_delete(request):
    """
    Function ensures user is redirected to
    empty booking table after deletion.
    """
    bookings = Booking.objects.all()[:0]
    context = {
        'bookings': bookings
    }
    return render(request, 'restaurant/no_booking.html', context)
