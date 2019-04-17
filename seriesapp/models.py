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



# Episodes 
class Episodes(models.Model):
    genres = models.ForeignKey(Genre)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    publishedDate = models.IntegerField(
        blank=True, null=True
    )
    episodes1 = models.CharField(max_length=200)
    episodesVideo1 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes2 = models.CharField(max_length=200)
    episodesVideo2 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes3 = models.CharField(max_length=200)
    episodesVideo3 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes4 = models.CharField(max_length=200)
    episodesVideo4 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes5 = models.CharField(max_length=200)
    episodesVideo5 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes6 = models.CharField(max_length=200)
    episodesVideo6 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes7 = models.CharField(max_length=200)
    episodesVideo7 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes8 = models.CharField(max_length=200)
    episodesVideo8 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes9 = models.CharField(max_length=200)
    episodesVideo9 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes10 = models.CharField(max_length=200)
    episodesVideo10 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes11 = models.CharField(max_length=200)
    episodesVideo11 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes12 = models.CharField(max_length=200)
    episodesVideo12 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes13 = models.CharField(max_length=200)
    episodesVideo13 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes14 = models.CharField(max_length=200)
    episodesVideo14 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes15 = models.CharField(max_length=200)
    episodesVideo15 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes16 = models.CharField(max_length=200)
    episodesVideo16 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes17 = models.CharField(max_length=200)
    episodesVideo17 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes18 = models.CharField(max_length=200)
    episodesVideo18 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes19 = models.CharField(max_length=200)
    episodesVideo19 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes20 = models.CharField(max_length=200)
    episodesVideo20 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes21 = models.CharField(max_length=200)
    episodesVideo21 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes22 = models.CharField(max_length=200)
    episodesVideo22 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes23 = models.CharField(max_length=200)
    episodesVideo23 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    episodes24 = models.CharField(max_length=200)
    episodesVideo24 = models.FileField(upload_to='Series/EpisodesVideo/', blank=False, null=True)
    

    def __unicode__(self):
        title = str(self.title)
        return title 


# Season
class Seasons(models.Model):
    genres = models.ForeignKey(Genre)
    episodes = models.ForeignKey(Episodes)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=200)
    genres = models.ForeignKey(Genre)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    publishedDate = models.IntegerField(
        blank=True, null=True
    )
    seriesImages = models.FileField(upload_to='Series/SeriesImage/', blank=False, null=True)
    

    def __unicode__(self):
        title = str(self.title)
        return title 

# Series 
class Series(models.Model):
    genres = models.ForeignKey(Genre)
    episodes = models.ForeignKey(Episodes)
    seasons = models.ForeignKey(Seasons)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    publishedDate = models.IntegerField(
        blank=True, null=True
    )
    seriesImages = models.FileField(upload_to='Series/SeriesImage/', blank=False, null=True)
    

    def __unicode__(self):
        title = str(self.title)
        return title 





