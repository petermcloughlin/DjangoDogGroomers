from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('service', 'staff', 'appointmentDay',)
        


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime'
    
        
 