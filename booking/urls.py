from . import views
from django.urls import path

urlpatterns = [   
    path('', views.home, name='home') ,     
    path('profile', views.profile, name='profile'),
    path('profile', views.profile, name='profile_booking'),
    path('profile', views.booking_page, name='booking_make'),      
]