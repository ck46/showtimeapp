# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)