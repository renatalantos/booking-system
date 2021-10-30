"""
Form elements that will appear on booking form.
Based on the Booking model.
"""
from tempus_dominus.widgets import DateTimePicker
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Class to construct booking form from the model.
    """
    class Meta:
        """
        Add form inputs from the model items as form fields.
        """
        model = Booking
        fields = ('customer_name', 'phone_number',
                  'reservation_date_and_time', 'number_of_customers')

    def __init__(self, *args, **kwargs):
        """
        Add class, required field and DateTime picker
        to third field.
        """
        super().__init__(*args, **kwargs)
        self.fields['reservation_date_and_time'].widget.attrs['class'] = 'form-control datetimepicker-input'
        self.fields['reservation_date_and_time'].widget = DateTimePicker()
        self.fields['reservation_date_and_time'].widget.attrs['required'] = 'required'
        self.fields['phone_number'].widget.attrs['required'] = 'required'
