from .models import Booking
from django import forms
from django.forms import widgets, DateTimeField, DateTimeInput


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('service', 'staff', 'appointment',)
        widgets = {
            'appointment': forms.widgets.DateTimeInput(
                attrs={
                        'type': 'datetime-local',
                        'required': 'required'
                    }
                )
        }


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'
