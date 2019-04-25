from .models import *
from django import forms
import django_filters

class SeriesFilters(django_filters.FilterSet):
        class Meta :
            model = Series
            fields = ['title', 'description', 'genres', 'publishedDate']
