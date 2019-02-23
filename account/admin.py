# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm , SignUpForm
from .models import CustomUser

# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserCreationForm
#     model = CustomUser
#     list_display = ['username', 'email']

# admin.site.register(CustomUser, CustomUserAdmin)