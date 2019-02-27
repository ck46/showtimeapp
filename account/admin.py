# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import *
from account.models import CustomUser

admin.site.register(User)

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name','profileImages', 'phonenumber' , 'iucnumber' ,'decodertype','email']

admin.site.register(CustomUser, CustomUserAdmin)