from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import *
from .forms import *
from django.utils import timezone
import time


@login_required
def HomePayPal(request):
    return render(request, 'website/paypalpayment.html', {})

# Dashboard Product
@login_required
def dashboardMoviePage(request):
    movies= Movie.objects.all().order_by('publishedDate')
    genres = Genre.objects.all().order_by('publishedDate')
    return render(request, 'website/dashboardMoviePage.html', {'newMovies' : movies, 'newMovieGenres' : genres})


#  Movie List
@login_required
def moviesList(request):
    movieslist = Movie.objects.all().order_by('publishedDate')
    return render(request, 'website/moviesList.html', {'newMovies' : movieslist})

#  Genre Product List
@login_required
def genresMoviesList(request):
    genreslists = Genre.objects.all().order_by('publishedDate')
    return render(request, 'website/genreList.html', {'newMovieGenres' : genreslists})

# Details of Series
@login_required
def moviesDetail(request, pk):
    moviesdetails  = get_object_or_404(Movie, pk=pk)
    return render(request, 'website/movieDetails.html', {'newMovies': moviesdetails})

# Details of Genres
@login_required
def genresMoviesDetail(request, pk):
    genresdetails  = get_object_or_404(Genre, pk=pk)
    return render(request, 'website/genresDetails.html', {'newMovieGenres':genresdetails})



# New Store Product
@login_required
def newMovies(request):
    if request.method == "POST":
        form = MoviesForm(request.POST, request.FILES)
        if form.is_valid():
            newMovies = form.save()
            newMovies.user = request.user
            newMovies.publishedDate = timezone.now()
            newMovies.save()
            # return redirect('dashboard',)productList
            # return redirect('productDetail', pk=newProduct.pk)
            return redirect('moviesList', pk=newMovies.pk)
    else:
        form = MoviesForm()
        # form = PostForm(request.POST, instance=new_post)
    return render(request, 'website/newMovies.html', {'form' : form})


# Edit old  Store Product
@login_required
def moviesEdit(request, pk):
    newMovies= get_object_or_404(Movie, pk=pk)
    if request.method == "POST" :
        form = MoviesForm(request.POST,request.FILES, instance=newMovies)
        if form.is_valid():
            newMovies = form.save()
            newMovies.user = request.user
            newMovies.publishedDate = timezone.now()
            newMovies.save()
            return redirect('moviesDetail', pk=newMovies.pk)
    else:
        form = MoviesForm(instance=newMovies)
    return render(request, 'website/moviesEdit.html', {'form': form})


# Delete Series
@login_required
def moviesRemove(request, pk):
    newMovies = get_object_or_404(Movie, pk=pk)
    newMovies.delete()
    return redirect('moviesList')



# New Genres
@login_required
def newMovieGenres(request):
    if request.method == "POST":
        form = GenresForm(request.POST, request.FILES)
        if form.is_valid():
            newMovieGenres = form.save()
            newMovieGenres.user = request.user
            newMovieGenres.publishedDate = timezone.now()
            newMovieGenres.save()
            # return redirect('dashboard',)
            return redirect('genresDetail', pk=newMovieGenres.pk)
    else:
        form = GenresForm()
        # form = PostForm(request.POST, instance=new_post)
    return render(request, 'website/newMovieGenres.html', {'form' : form})


# Edit old Store
@login_required
def genresEdit(request, pk):
    newMovieGenres = get_object_or_404(Genre, pk=pk)
    if request.method == "POST" :
        form = displayProductForm(request.POST,request.FILES, instance=newStore)
        if form.is_valid():
            newMovieGenres = form.save()
            newMovieGenres.user = request.user
            newMovieGenres.publishedDate = timezone.now()
            newMovieGenres.save()
            return redirect('genresDetail', pk=newMovieGenres.pk)
    else:
        form = GenresForm(instance=newMovieGenres)
    return render(request, 'website/genresEdit.html', {'form': form})


# Delete Store
@login_required
def genresRemove(request, pk):
    newMovieGenres = get_object_or_404(newMovieGenres, pk=pk)
    newMovieGenres.delete()
    return redirect('genresList')
