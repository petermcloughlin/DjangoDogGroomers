from . import views
from django.urls import path

urlpatterns = [   
    path('', views.home, name='home') ,     
    path('profile', views.profile, name='profile'),
    path('profile', views.profile, name='profile_booking'),
    path('booking/', views.booking_page, name='booking_page'),  
    path('booking/<int:bk_id>/update', views.update_view, name='update_url'),
    path('booking/<int:bk_id>/delete', views.delete_view, name='delete_url'),      
]