from django import forms
from .models import User,City,Cleaner
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator

contact = RegexValidator(regex='[0-9]{10}$',message="Enter Valid 10 Digit Mobile Number")

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('phone','first_name','last_name','email','password1','password2')

class LoginForm(forms.Form):
    phone = forms.CharField(max_length=10,validators = [contact], label='Enter Contact Number')
    password = forms.CharField(max_length=20,label='Enter Password',widget=forms.PasswordInput())

class cleanerRegisterForm(forms.ModelForm):
    city = forms.ModelChoiceField(queryset=City.objects.all(),label="Select City:")
    class Meta:
        model = Cleaner
        fields = ['city'] 