from django.shortcuts import render,redirect
from django.views.generic import View
from django.views.generic.detail import DetailView
from .forms import RegisterForm,LoginForm,cleanerRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import messages
from .models import User,Cleaner
from django.http import JsonResponse

# Create your views here.

class RegisterView(View):
    def get(self,request):
        r_form = RegisterForm()
        return render(request,'accounts/register.html',{'form':r_form})
    
    def post(self,request):
        r_form = RegisterForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            return redirect('login')
        return render(request,'accounts/register.html',{'form':r_form})

def validate_phone(request):
    phone = request.GET.get('phone',None)
    data = {
        'is_taken': User.objects.filter(phone__iexact=phone).exists()
    }
    return JsonResponse(data)

class Profile(DetailView):
    model = User
    template_name = "accounts/profile.html"
    extra_context = {'form':cleanerRegisterForm()}

    

class CleanerView(View):
    def get(self,request):
        c_form = cleanerRegisterForm()
        return render(request,'accounts/cleaner.html',{'form':c_form})
 
    def post(self,request):
        c_form = cleanerRegisterForm(request.POST)
        if c_form.is_valid():
            obj=c_form.save(commit=False)
            obj.user = request.user
            request.user.is_cleaner = True
            request.user.save()
            obj.save()
            return redirect("profile",pk=request.user.pk)
        # return render(request,"accounts/cleaner.html",{'form':c_form})

class LoginView(View):
    def get(self,request):
        l_form = LoginForm()
        return render(request,'accounts/login.html',{'form':l_form})
    
    def post(self,request):
        form1 = LoginForm(data=request.POST)
        print (form1.is_valid())
        if form1.is_valid():
            phone = form1.cleaned_data.get('phone')
            password = form1.cleaned_data.get('password')
            user = authenticate(phone=phone,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'User Does Not Exists Please Enter Valid Data'+str(form1.errors))
        return render(request,'accounts/login.html',{'form':form1})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')

def home(request):
    return render(request,'accounts/home.html')
