from .models import *
from django import forms
import django_filters

class MoviesFilters(django_filters.FilterSet):
    class Meta :
        model = Movie
        fields = ['title', 'description', 'genre']

