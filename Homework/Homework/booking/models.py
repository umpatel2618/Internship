from django.db import models
from accounts.models import User,Cleaner,City
from django.urls import reverse
# Create your models here.



class Booking(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    city = models.ForeignKey(City,null=True,on_delete=models.SET_NULL)
    cleaner = models.ForeignKey(Cleaner,null=True,on_delete=models.SET_NULL)
    date = models.DateField()
    slot = models.IntegerField(null=True)
    


    def __str__(self):
        return str(self.id) + " " + self.cleaner.user.first_name + ' , ' + self.city.city

    def get_absolute_url(self):
        return reverse("booking_list", kwargs={"pk": self.pk})
     