from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class GenresForm(forms.ModelForm):
    
    class Meta:
        model = Genre
        fields = ['title', 'publishedDate', 'genreImages']


class DirectorForm(forms.ModelForm):
    
    class Meta:
        model = Director
        fields = ['directorName', 'directorImages']


class ActorForm(forms.ModelForm):
    
    class Meta:
        model = Actor
        fields = ['description', 'mainActorImages','actorOne', 'secondActorImages','actorTwo', 'thirdActorImages','actorThree', 'fourthActorImages', 'actorFour']


class MoviesForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['title', 'genre', 'description','directors', 'actors', 'publishedDate', 'movieImages', 'movieVideo']
        





