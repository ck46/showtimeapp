# from django.contrib.auth.models import AbstractUser
from django.db import models 
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phonenumber = models.CharField(max_length=100)
    iucnumber = models.CharField(max_length=100)


    def __str__(self):
        return self.iucnumber