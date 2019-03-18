from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = [ 'title', 'publishedDate', 'genreImages']


class EpisodesForm(forms.ModelForm):
    
    class Meta:
        model = Episodes
        fields = ['genres'  ,'title', 'description', 'publishedDate']

class SeriesForm(forms.ModelForm):

    class Meta:
        model = Series
        fields = ['genres', 'title', 'description', 'genres', 'publishedDate', 'seriesImages','episodes']
        





