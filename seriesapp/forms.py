from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = [ 'title', 'publishedDate', 'genreImages']

class SeriesForm(forms.ModelForm):

    class Meta:
        model = Series
        fields = ['title', 'description', 'genres', 'publishedDate', 'seriesImages', 'seriesVideo']
        





