from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.db import models
# Create your models here.

# Genre
class Genre(models.Model):
    title = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    publishedDate = models.DateTimeField(
        blank=True, null=True
    )
    genreImages = models.FileField(upload_to='Series/GenreImage/', blank=False, null=True)

    def __unicode__(self):
        title = str(self.title)
        return title 


# Series 
class Series(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=200)
    genres = models.ForeignKey(Genre)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    publishedDate = models.IntegerField(
        blank=True, null=True
    )
    seriesImages = models.FileField(upload_to='Series/SeriesImage/', blank=False, null=True)
    seriesVideo = models.FileField(upload_to='Series/SerieVideo/', blank=False, null=True)

    def __unicode__(self):
        title = str(self.title)
        return title 


# Episodes 
class Episodes(models.Model):
    series = models.ForeignKey(Series)
    title = models.CharField(max_length=200)
    publishedDate = models.IntegerField(
        blank=True, null=True
    )
    episodesImages = models.FileField(upload_to='Series/SeriesImage/', blank=False, null=True)
    episodesVideo = models.FileField(upload_to='Series/SerieVideo/', blank=False, null=True)

    def __unicode__(self):
        title = str(self.title)
        return title 


