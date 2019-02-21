from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from showtimeapp import views as showtime_view
from showtimeapp import views
from .views import *

urlpatterns = [
    # Home Page
    url(r'^$', views.Home, name='Home'),

]