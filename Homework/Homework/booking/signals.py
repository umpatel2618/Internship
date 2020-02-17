from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking
from .forms import SLOT_CHOICE
from Homework.settings import EMAIL_HOST_USER
from django.core.mail import send_mass_mail

@receiver(post_save,sender=Booking)
def email_send(sender,instance,created,**kwargs):
    if created:
        cleaner_msg = "Welcome To Homewrok The Home Cleaning Services.\n You have been Booked for a Date:" + str(instance.date) + " for cleaning service at " + instance.city.city + "\nCustomer name : " + instance.user.first_name + "\nTime : " + SLOT_CHOICE[int(instance.slot)][1] + "\nSee Your Orders List :127.0.0.1:8000/booking_list/'"
        print(cleaner_msg)
        customer_msg = "Welcome To Homewrok The Home Cleaning Services.\n Congratulations!You have successfully booked a cleaner for date :" + str(instance.date) + " cleaning service at " + instance.city.city + "\nCleaner name : " + instance.cleaner.user.first_name + "\nTime : " + SLOT_CHOICE[int(instance.slot)][1] + "\nSee Your Orders List :127.0.0.1:8000/booking_list/'"
        print(customer_msg)
        print(SLOT_CHOICE[int(instance.slot)][1])
        
        cleaner_mail = ('Hey Cleaner, You Have Been Booked', cleaner_msg, EMAIL_HOST_USER, [instance.cleaner.user.email])
        customer_mail = ('Welcome To Homework Your Booking Apppoinment', customer_msg, EMAIL_HOST_USER, [instance.user.email])

        res = send_mass_mail((cleaner_mail, customer_mail), fail_silently=False)

        print(res) # return render(request,'booking/postbooking.html')
    else:
        raise('Not Booked!!!')