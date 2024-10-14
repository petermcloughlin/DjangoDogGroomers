from django.urls import path
from . import views
from .views import (
    BookingList
)

urlpatterns = [        
    path('booking/',BookingList.as_view(), name='booking-list'),
    path('', views.home, name='doggroomers-home') 
]