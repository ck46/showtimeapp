from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from movieapp import views as movie_views
from movieapp import views
from .views import *

urlpatterns = [
    # Movie
    url(r'^HomePayPal/$', views.HomePayPal, name='HomePayPal'),
    url(r'^$', views.dashboardMoviePage, name='dashboardMoviePage'),
    url(r'^List/$', views.moviesList, name='moviesList'),
    url(r'^movie/(?P<pk>\d+)/$', views.moviesDetail, name='moviesDetail'),
    url(r'^movie/new/$', views.newMovies, name='newMovies'),
    url(r'^movie/(?P<pk>\d+)/edit/$', views.moviesEdit, name='moviesEdit'),
    url(r'^movie/(?P<pk>\d+)/remove/$', views.moviesRemove, name='moviesRemove'),
    url(r'^genre/(?P<gn>[-\w]+)/$',
        views.genreMoviePage, name='genreMoviePage'),

    # Genres
    url(r'^genresMoviesList/$', views.genresMoviesList, name='genreMoviesList'),
    url(r'^/(?P<pk>\d+)/$', views.genresMoviesDetail, name='genresMoviesDetail'),
    url(r'^genre/new/$', views.newMovieGenres, name='newMovieGenres'),
    url(r'^genre/(?P<pk>\d+)/edit/$', views.genresEdit, name='genreEdit'),
    url(r'^/(?P<pk>\d+)/remove/$', views.genresRemove, name='genreRemove'),



]
