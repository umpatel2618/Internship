from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=20,unique=False)
    phone = models.CharField(max_length=10,unique=True)
    first_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    is_cleaner = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS =   ['username']

    def __str__(self):
        return self.first_name

class City(models.Model):
    city = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.city

class Cleaner(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    quality_score = models.FloatField(default=0.00)
    city = models.ForeignKey(City,null=True,on_delete=models.CASCADE)
     
    def __str__(self):
        return str(self.user) + ' ,' +str(self.quality_score) + ',' + str(self.city)
    