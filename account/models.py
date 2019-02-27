# from django.contrib.auth.models import AbstractUser
from django.db import models 
from django.contrib.auth.models import AbstractUser




class CustomUser(AbstractUser):
    phonenumber = models.CharField(max_length=100, blank=False, null=True)
    decodertype = models.CharField(max_length=100, blank=False, null=True)
    iucnumber = models.CharField(max_length=100 , blank=False, null=True)
    profileImages = models.FileField(upload_to='Profile/ProfileImage/', blank=False, null=True)


    def __str__(self):
        return self.iucnumber