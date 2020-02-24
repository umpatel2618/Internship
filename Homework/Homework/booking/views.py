from django.shortcuts import render, redirect
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import Cleaner,City
from .forms import BookingForm,BookingDetailForm,SLOT_CHOICE
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from Homework.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.urls import reverse_lazy
import datetime

# Create your views here.


class BookingView(View):
    def get(self, request):
        form = BookingForm()
        return render(request, "booking/booking.html", {'form': form})

    def post(self, request):
        form = BookingForm(data=request.POST)
        if form.is_valid():
            city = form.cleaned_data.get('city')
            slot = form.cleaned_data.get('slot')
            date = form.cleaned_data.get('date')
            
            

            book = Booking.objects.filter(
                                city__city=city,slot=slot, date=date)
            cleaner = Cleaner.objects.filter(city__city=city).exclude(
                                user__in=[x.cleaner.user for x in book]).exclude(user=request.user)
            print(cleaner, city, date, slot)

            


            return render(request, 'booking/booking.html', {'star_counter':range(5),'cleaner': cleaner, 'city': city, 'slot': slot, 'date': date,'form':form})

class BookingSave(View):
    @method_decorator(login_required,name='dispatch')
    def post(self,request):
        data = request.POST.copy()
        city = City.objects.get(pk=data['city'])
        cleaner = Cleaner.objects.get(pk=data['cleaner'])
        o=Booking.objects.create(user=request.user,city=city,date=data['date'],cleaner=cleaner,slot=data['slot'])
        # message = '----Booking Detail----\n Customer Name:' + cleaner.user.first_name +  '\n Date:' + str(data['date'])+ '\n City: '+ city.city + '\n Time:' + str(data['slot']) +'' 
        # print(message)
        # recepient= cleaner.user.email
        # print(recepient)
        # data=Booking.objects.filter(user=request.user)
        # subject = "One New Booking"
        # send_mail(subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False) 
        return redirect('bookinglist',pk=o.id)    
         
class BookingList(ListView):
    template_name = 'booking/booking_list.html'
    

    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-date')
        
        

class DeleteBooking(DeleteView):
    model=Booking
    # template_name = 'booking/bookingmodel_confirm_delete.html'
    success_url = reverse_lazy('mybooking_list')
    

class BookingDetail(DetailView):
    model=Booking
    template_name = 'booking/booking_detail.html'

    extra_context = {'form':BookingDetailForm()}

class Dutydetail(ListView):
    template_name = 'booking/duty.html'

    def get_queryset(self):
        return Booking.objects.filter(cleaner__user=self.request.user).order_by('date')