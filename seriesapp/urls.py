from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from seriesapp import views as series_views
from seriesapp import views
from .views import *

urlpatterns = [
    # Series 
    url(r'^$', views.dashboardPage, name='dashboardPage'),
    url(r'^seriesList/$', views.seriesList, name='seriesList'),
    url(r'^series/(?P<pk>\d+)/$', views.seriesDetail, name='seriesDetail'),
    url(r'^series/new/$', views.newSeries, name='newSeries'),
    url(r'^series/(?P<pk>\d+)/edit/$', views.seriesEdit, name='seriesEdit'),
    url(r'^series/(?P<pk>\d+)/remove/$', views.seriesRemove, name='seriesRemove'),

    # Genres
    url(r'^genreList/$', views.genresList, name='genreProductList'),
    url(r'^/(?P<pk>\d+)/$', views.genresDetail, name='genresDetail'),
    url(r'^genre/new/$', views.newGenres, name='newGenres'),
    url(r'^genre/(?P<pk>\d+)/edit/$', views.genresEdit, name='genreEdit'),
    url(r'^/(?P<pk>\d+)/remove/$', views.genresRemove, name='genreRemove'),


]