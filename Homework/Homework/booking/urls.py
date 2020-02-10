from django.urls import path
from .views import BookingView,BookingSave,BookingList
from . import views

urlpatterns = [
    path('booking/',BookingView.as_view() ,name='booking'),
    path('booking_save/',BookingSave.as_view() ,name='booking_save'),
    path('booking_list/<int:pk>/',BookingList.as_view() ,name='booking_list'),
]
