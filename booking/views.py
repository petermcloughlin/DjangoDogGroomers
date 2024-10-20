from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Booking
from django.contrib.auth.models import User
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('Welcome to the home page.')
def home(request):
    return render(request, "booking/index.html")
    

def profile(request):
    '''
    Display the user's list of bookings when logged in. 
    Welcome {{ user }} displays this when clicked.
    '''    
    # Get the list of bookings where created_by is the current user
    bookings = get_list_or_404(Booking, created_by=request.user)  
    
    return render(
        request,
        "booking/profile.html", 
        {"bookings": bookings}
        )
    
    

    



