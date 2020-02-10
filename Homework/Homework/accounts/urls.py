from django.urls import path
from .views import RegisterView,LoginView,LogoutView,CleanerView,Profile,validate_phone
from . import views
from django.conf.urls import url
urlpatterns = [
    path('',views.home, name='home'),
    path('register/',RegisterView.as_view() ,name='register'),
    url(r'^ajax/validate_phone/$', views.validate_phone, name='validate_phone'),
    path('profile/<int:pk>',Profile.as_view() ,name='profile'),
    path('login/',LoginView.as_view() ,name='login'),
    path('logout/',LogoutView.as_view() ,name='logout'),
    path('cleaner/',CleanerView.as_view() ,name='cleaner'),
]

