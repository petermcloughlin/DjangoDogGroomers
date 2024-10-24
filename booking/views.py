from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm
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
    # bookings = get_list_or_404(Booking, created_by=request.user)  
    bookings = list(Booking.objects.filter(created_by=request.user))
    if not bookings:       
        return render(
            request,
            "booking/profile-no-booking.html"
            )
    else:
        return render(
            request,
            "booking/profile.html", 
            {"bookings": bookings}
            )
    

def booking_page(request):
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.created_by = request.user
            booking.save()
            return render(
                request,
                "booking/index.html"
                )
            # messages.add_message(
            #     request, messages.SUCCESS,
            #     'Thanks you. We look forward to seeing you.'
            # )

    booking_form = BookingForm()

    return render(
        request,
        "booking/booking.html",
        {
            "booking_form": booking_form,
        },
    )




    

    



