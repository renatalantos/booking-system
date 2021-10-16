from django import forms


class BookingForm(forms.Form):
    TABLE_CATEGORY = [
        ('For 2', 'Couple'),
        ('For 4', 'Party of 4'),    
    ]
    table_category = forms.ChoiceField(required=True, choices=TABLE_CATEGORY)
    start_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    end_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    number_of_customers = forms.IntegerField(required=True)
    number_of_tables = forms.IntegerField(required=True)
    menu = forms.ChoiceField(required=True, choices=MENU_CATEGORY)


    
