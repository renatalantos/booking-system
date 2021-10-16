from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Table, Booking, Menu
from .forms import BookingForm
from restaurant.reservation_functions.availablity import check_availability
# Create your views here.

class TableList(ListView):
    model = Table


class BookingList(ListView):
    model = Booking


class MenuList(ListView):
    model = Menu

class BookingView(FormView):
    form_class = BookingForm
    template_name = 'booking_form.html'

 
    def form_valid(self, form):
        data =form.cleaned_data
        table_list = Table.objects.filter(category=data['table_category'])
        available_tables =[]
        for table in table_list:
            if check_availability(table, data['start_date'], data['end_date']):
                available_tables.append(table)

        if len(available_tables)>0:        
            table = available_tables[0]
            booking=Booking.objects.create(
                customer=request.customer,
                table=table,
                start_date=data['start_date'],
                end_date=data['end_date'],
                
                number_of_customers=number_of_customers,
                number_of_tables=number_of_tables,

            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All these tables are booked out!')        



