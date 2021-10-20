from django import forms
from .models import Booking



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'phone_number', 'start_date', 'end_date', 'number_of_customers', 'menu']
      
    
    
