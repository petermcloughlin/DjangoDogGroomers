from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    STAFF = [
        (0, 'Sean'),
        (1, 'Grace'),
        (2, 'Roberta')
    ]

    SERVICES = [
        (0, 'Wash and Blow-Dry'),
        (1, 'Claw Clipping'),
        (2, 'Coat Trim'),
        (3, 'Teeth Clean'),
        (4 ,'Flea Treatment and Worming'),
        (5, 'Paw Ear and Skin Treatment'),
        (6 , 'Therapy Bath')
    ]

    service = models.CharField(choices=SERVICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_booking')
    appointmentDay = models.DateTimeField()

    

    
