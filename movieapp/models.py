from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.db import models
# Create your models here.


# Movie  
class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    publishedDate = models.DateTimeField(
        blank=True, null=True
    )
    movieImages = models.FileField(upload_to='Movie/MovieImage/', blank=False, null=True)
    movieVideo = models.FileField(upload_to='Movie/MovieVide/', blank=False, null=True)

    def __unicode__(self):
        title = str(self.title)
        return title 


# Genre
class Genre(models.Model):
    
    movies = models.ForeignKey(Movie)
    title = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    publishedDate = models.DateTimeField(
        blank=True, null=True
    )
    genreImages = models.FileField(upload_to='Movie/GenreImage/', blank=False, null=True)

    def __unicode__(self):
        title = str(self.title)
        return title 
