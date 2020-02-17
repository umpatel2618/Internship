from .models import Booking
from django import forms
from accounts.models import City,Cleaner
from django.db.models import Q
from django.utils import timezone
from .models import User

SLOT_CHOICE = (
    (0,"---------------"),
    (1,"10 A.M To 12 P.M"),
    (2,"12 P.M To 2 P.M"),
    (3," 2 P.M To 4 P.M"),
    (4," 4 P.M To 6 P.M"),
    (5," 6 P.M To 8 P.M"),
)   


class BookingForm(forms.Form):
    city = forms.ModelChoiceField(label="Select Your Prefered City:",queryset=City.objects.all())
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control datetimepicker-input','type':'date'}))
    slot = forms.IntegerField(widget=forms.Select(choices=SLOT_CHOICE))
    date.widget.attrs['min'] = timezone.now().date()
    email = forms.EmailField().hidden_widget

class BookingDetailForm(forms.Form):
    class Meta:
        model = Booking
        fields = '__all__' 






