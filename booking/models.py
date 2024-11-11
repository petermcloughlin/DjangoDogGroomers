from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

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
        (4, 'Flea Treatment and Worming'),
        (5, 'Paw Ear and Skin Treatment'),
        (6, 'Therapy Bath')
    ]

    service = models.IntegerField(choices=SERVICES, default=0)
    staff = models.IntegerField(choices=STAFF, default=0)
    appointment = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(
                    User,
                    on_delete=models.CASCADE,
                    related_name='booking_booking'
                    )

    class Meta:
        ordering = ["appointment"]

    def __str__(self):
        return f"Booking for {self.created_by} | {self.appointment.strftime('%B %d, %Y at %I:%M %p')}"
        
