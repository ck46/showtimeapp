from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class MoviesForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['title', 'genre', 'description', 'publishedDate', 'movieImages', 'movieVideo']
        


class GenresForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = ['title', 'publishedDate', 'genreImages']


