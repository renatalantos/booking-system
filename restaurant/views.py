
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView, FormView, View
from .models import Booking
from .forms import BookingForm
from restaurant.reservation_functions.availablity import check_availability
# Create your views here.




class BookingListView(ListView):
    model = Booking
    template = "booking_list.html"

    def get_queryset(self, *args, **kwargs):
        booking_list = Booking.objects.filter(user = self.request.user)
        return booking_list

  
class BookingFormView(View):
    def get(self, request, *args, **kwargs):
        if 'start_date' in request.session:
            s = request.session
            form_data = {
                "user": s['user'],
                "phone_number": s['phone_number'],
                "start_date": s['start_date'],
                "end_date": s['end_date'],
                "number_of_customers": s['number_of_customers'],
                "menu": s['menu'],    

            }
            #booking_form_data = self.request.session['booking_form_data']
            form = BookingForm(request.POST or None, initial=form_data)
        else:
            form = BookingForm() 

        return render(request, 'booking_form.html', {'form': form})   
    
    
    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            data =form.cleaned_data
        
            request.session['user'] = data['user']
            request.session['start_date'] = data['start_date'].strftime("%Y-%m-%dT%H:%M")
            request.session['end_date'] = data['end_date'].strftime("%Y-%m-%dT%H:%M")
            request.session['number_of_customers'] = data['number_of_customers']
            request.session['menu'] = data['menu']
            request.session['phone_number'] = data['phone_number']

            return redirect('restaurant:BookingListView')
        else:
            return HttpResponse('form not valid', form.errors)    



