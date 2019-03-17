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
    genreImages = models.FileField(upload_to='Movie/GenreImage/', blank=False, null=True)

    def __unicode__(self):
        title = str(self.title)
        return title 


# Director
class Director(models.Model):
    directorName  = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    publishedDate = models.IntegerField(
        blank=True, null=True
    )
    directorImages = models.FileField(upload_to='Movie/DirectorImage/', blank=False, null=True)

    def __unicode__(self):
        directorName = str(self.directorName)
        return directorName 


# Actors 
class Actor(models.Model):
    description = models.CharField(max_length=200)
    publishedDate = models.IntegerField(
        blank=True, null=True
    )
    mainActorImages = models.FileField(upload_to='Movie/ActorsImage/', blank=False, null=True)
    actorOne = models.CharField(max_length=200)
    secondActorImages = models.FileField(upload_to='Movie/ActorsImage/', blank=False, null=True)
    actorTwo = models.CharField(max_length=200)
    thirdActorImages = models.FileField(upload_to='Movie/ActorsImage/', blank=False, null=True)
    actorThree = models.CharField(max_length=200)
    fourthActorImages = models.FileField(upload_to='Movie/ActorsImage/', blank=False, null=True)
    actorFour = models.CharField(max_length=200)

    def __unicode__(self):
        description = str(self.description)
        return description


# Movie  
class Movie(models.Model):
    directors = models.ForeignKey(Director)
    actors = models.ForeignKey(Actor)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    genre = models.ForeignKey(Genre)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    publishedDate = models.IntegerField(
        blank=True, null=True
    )
    movieImages = models.FileField(upload_to='Movie/MovieImage/', blank=False, null=True)
    movieVideo = models.FileField(upload_to='Movie/MovieVide/', blank=False, null=True)

    def __unicode__(self):
        title = str(self.title)
        return title 





