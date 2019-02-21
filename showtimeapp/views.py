# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


# Home Page
def Home(request):
    return render(request, 'website/index.html', {})