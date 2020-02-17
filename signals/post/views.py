from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_finished
from django.dispatch import receiver,Signal
from .models import Post
# Create your views here.


request_counter_signal = Signal(providing_args=['timestamp'])

def home(request):
    request_counter_signal.send(sender=Post,timestamp='2020-2-13')
    return HttpResponse("Here Is The Response")

@receiver(request_finished)
def post_request_receiver(sender, **kwargs):
    print("Request Finished..")

@receiver(request_counter_signal)
def post_counter_request_receiver(sender, **kwargs):
    print(kwargs)



