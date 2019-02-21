from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from movieapp import views as movie_views
from movieapp import views
from .views import *

urlpatterns = [
    # Movie
    url(r'^$', views.dashboardPage, name='dashboardPage'),
    url(r'^List/$', views.moviesList, name='moviesList'),
    url(r'^movie/(?P<pk>\d+)/$', views.moviesDetail, name='moviesDetail'),
    url(r'^movie/new/$', views.newMovies, name='newMovies'),
    url(r'^movie/(?P<pk>\d+)/edit/$', views.moviesEdit, name='moviesEdit'),
    url(r'^movie/(?P<pk>\d+)/remove/$', views.moviesRemove, name='moviesRemove'),

    # Genres
    url(r'^genreList/$', views.genresList, name='genreProductList'),
    url(r'^/(?P<pk>\d+)/$', views.genresDetail, name='genresDetail'),
    url(r'^genre/new/$', views.newGenres, name='newGenres'),
    url(r'^genre/(?P<pk>\d+)/edit/$', views.genresEdit, name='genreEdit'),
    url(r'^/(?P<pk>\d+)/remove/$', views.genresRemove, name='genreRemove'),



]