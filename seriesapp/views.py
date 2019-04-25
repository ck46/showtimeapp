# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import *
from .forms import *
from .filters import *
from django.utils import timezone
from django.db.models import Q
import time




# Dashboard Product
@login_required
def dashboardPage(request):
    series= Series.objects.all().order_by('publishedDate')
    genres = Genre.objects.all().order_by('publishedDate')
    # series_filter = SeriesFilters(request.GET, queryset=series)
    query = request.GET.get("searchs")
    if query:
        series = series.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)|
            Q(publishedDate__icontains=query)|
            Q(genres__title__icontains=query)
        ).distinct()
    return render(request, 'website/dashboardPages.html', {'newGenres' : genres, 'series': series})

#  Series List
@login_required
def seriesList(request):
    serieslist = Series.objects.all().order_by('publishedDate')
    return render(request, 'website/seriesList.html', {'newSeries' : serieslist})

#  Genre Product List
@login_required
def genresList(request):
    genreslists = Genre.objects.all().order_by('publishedDate')
    return render(request, 'website/genreList.html', {'newGenres' : genreslists})



# Details of Series
@login_required
def seriesDetail(request, pk):
    seriesdetails  = get_object_or_404(Series, pk=pk)
    return render(request, 'website/serieDetails.html', {'newSeries': seriesdetails})

# Details of Genres
@login_required
def genresDetail(request, pk):
    genresdetails  = get_object_or_404(Genre, pk=pk)
    return render(request, 'website/genresDetails.html', {'newGenres':genresdetails})



# New Store Product
@login_required
@login_required
def newSeries(request):
    if request.method == "POST":
        form = SeriesForm(request.POST, request.FILES)
        if form.is_valid():
            newSeries = form.save()
            newSeries.user = request.user
            newSeries.publishedDate = timezone.now()
            newSeries.save()
            # return redirect('dashboard',)productList
            # return redirect('productDetail', pk=newProduct.pk)
            return redirect('seriesList', pk=newSeries.pk)
    else:
        form = SeriesForm()
        # form = PostForm(request.POST, instance=new_post)
    return render(request, 'website/newSeries.html', {'form' : form})


# Edit old  Store Product
@login_required
def seriesEdit(request, pk):
    newSeries= get_object_or_404(Series, pk=pk)
    if request.method == "POST" :
        form = ProductForm(request.POST,request.FILES, instance=newSeries)
        if form.is_valid():
            newSeries = form.save()
            newSeries.user = request.user
            newSeries.publishedDate = timezone.now()
            newSeries.save()
            return redirect('seriesDetail', pk=newSeries.pk)
    else:
        form = SeriesForm(instance=newSeries)
    return render(request, 'website/seriesEdit.html', {'form': form})


# Delete Series
@login_required
def seriesRemove(request, pk):
    newSeries = get_object_or_404(Series, pk=pk)
    newSeries.delete()
    return redirect('seriesList')



# New Genres
@login_required
def newGenres(request):
    if request.method == "POST":
        form = GenresForm(request.POST, request.FILES)
        if form.is_valid():
            newGenres = form.save()
            newGenres.user = request.user
            newGenres.publishedDate = timezone.now()
            newGenres.save()
            # return redirect('dashboard',)
            return redirect('genresDetail', pk=newGenres.pk)
    else:
        form = GenresForm()
        # form = PostForm(request.POST, instance=new_post)
    return render(request, 'website/newGenres.html', {'form' : form})


# Edit old Store
@login_required
def genresEdit(request, pk):
    newGenres = get_object_or_404(Genre, pk=pk)
    if request.method == "POST" :
        form = displayProductForm(request.POST,request.FILES, instance=newStore)
        if form.is_valid():
            newGenres = form.save()
            newGenres.user = request.user
            newGenres.publishedDate = timezone.now()
            newGenres.save()
            return redirect('genresDetail', pk=newGenres.pk)
    else:
        form = GenresForm(instance=newGenres)
    return render(request, 'website/genresEdit.html', {'form': form})


# Delete Store
@login_required
def genresRemove(request, pk):
    newGenres = get_object_or_404(newGenres, pk=pk)
    newGenres.delete()
    return redirect('genresList')


