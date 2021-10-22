from django import forms
from .models import Booking



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'phone_number', 'reservation_date','number_of_customers', 'menu']
      
    
    
