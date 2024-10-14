from django.shortcuts import render
from django.views import generic
from .models import Booking
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('Welcome to the home page.')
class BookingList(generic.ListView):
    model = Booking
