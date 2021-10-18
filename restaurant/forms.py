from django import forms



class BookingForm(forms.Form):
      
    user = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    start_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    end_date = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    number_of_customers = forms.IntegerField(required=True)
    
    MENU_CATEGORY = [
        ('A la carte', 'A la carte'),
        ('House special', 'Special'),
        ('Vegetarian', 'Vegetarian'),
        ('Vegan', 'Vegan'),
    ]
    
    menu = forms.ChoiceField(choices=MENU_CATEGORY)


    
