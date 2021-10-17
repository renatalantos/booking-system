from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse

from django.views.generic import ListView, FormView
from .models import Booking
from .forms import BookingForm
from restaurant.reservation_functions.availablity import check_availability
# Create your views here.




class BookingList(ListView):
    model = Booking



class BookingView(FormView):
    form_class = BookingForm
    template_name = 'booking_form.html'

 
    def form_valid(self, form):
        data =form.cleaned_data
        table_list = Booking.objects.filter()
        available_tables =[]
        for table in table_list:
            if check_availability(data['start_date'], data['end_date']):
                available_tables.append(table)

        if len(available_tables)>0:        
            table = available_tables[0]
            booking = Booking.objects.create(
                user=self.request.user,
                phone_number=data['phone_number'],
                start_date=data['start_date'],
                end_date=data['end_date'],
                number_of_customers=data['number_of_customers'],
                menu=data['menu'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All these tables are booked out!')        



