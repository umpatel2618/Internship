from django.shortcuts import render, redirect
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import Cleaner,City
from .forms import BookingForm,BookingDetailForm,SLOT_CHOICE
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


class BookingView(View):
    def get(self, request):
        form = BookingForm()
        return render(request, "booking/booking.html", {'form': form})

    def post(self, request):
        print('knlsdhsad')
        form = BookingForm(data=request.POST)
        print("dsfjndskjnslk")
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

# class BookingList(ListView):
#     template_name = 'booking/booking_list.html'
#     queryset = Booking.objects.all()



class BookingSave(View):
    @method_decorator(login_required,name='dispatch')
    def post(self,request):
        data = request.POST.copy()
        city = City.objects.get(pk=data['city'])
        cleaner = Cleaner.objects.get(pk=data['cleaner'])
        o=Booking.objects.create(user=request.user,city=city,date=data['date'],cleaner=cleaner,slot=data['slot'])
        data=Booking.objects.filter(user=request.user)
        return redirect('booking_list',pk=o.id)    
         
class BookingList(ListView):
    template_name = 'booking/booking_list.html'
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-date')
        
