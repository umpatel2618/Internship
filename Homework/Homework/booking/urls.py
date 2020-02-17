from django.urls import path
from .views import BookingView,BookingSave,BookingList,DeleteBooking,BookingDetail,Dutydetail
from . import views

urlpatterns = [
    path('booking/',BookingView.as_view() ,name='booking'),
    path('booking_detail/<int:pk>/',BookingDetail.as_view(),name='bookinglist'),    
    path('booking_save/',BookingSave.as_view() ,name='booking_save'),
    path('booking_list/',BookingList.as_view() ,name='mybooking_list'),
    path('booking_delete/<int:pk>/',DeleteBooking.as_view(),name='booking_delete'),
    path('dutydetail/<int:pk>/',Dutydetail.as_view(),name='dutydetail'),

]
