from django.shortcuts import render
from django.views import generic
from .models import Booking
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('Welcome to the home page.')
def home(request):
    return render(request, "booking/index.html")


class BookingList(generic.ListView):
    # model = Booking
    queryset = Booking.objects.all()
    template_name = "booking_list.html"



