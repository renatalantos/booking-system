from django import forms
from .models import Booking
from django.forms import ModelForm
from django.forms import DateTimeInput
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class BookingForm(forms.ModelForm): #changed from forms.ModelForm

    class Meta:
        model = Booking
        
        fields = ('customer_name', 'phone_number', 'reservation_date_and_time', 'number_of_customers')


    def __init__(self, *args, **kwargs):

        
            super().__init__(*args, **kwargs)
            self.fields['reservation_date_and_time'].widget.attrs['class'] = 'form-control datetimepicker-input'
            self.fields['reservation_date_and_time'].widget = DateTimePicker()
            
            
