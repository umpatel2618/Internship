from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Userparent(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
#     f_name = models.CharField(max_length=50)
#     l_name = models.CharField(max_length=50)

# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     pub_date = models.DateField()
#     reporter = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reporter')

#     def __str__(self):
#         return self.headline
#     class Meta:
#         ordering = ('headline',)
        
class Program(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Price(models.Model):
    program = models.ForeignKey(Program,on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return str(self.program) + " " + str(self.from_date) + " " + str(self.to_date)

class Order(models.Model):
    stats = models.CharField(max_length=20)
    items = models.ManyToManyField(Price)

    def __str__(self):
        return str(self.stats) + " " + str(self.items) 


class Movie(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Charecter(models.Model):
    name = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name
