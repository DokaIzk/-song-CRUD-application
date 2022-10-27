from unittest.util import _MAX_LENGTH
from django.db import models


class Artiste(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField


class Song(models.Model):
    title = models.CharField(max_length=40)
    released_date = models.DateTimeField()
    likes = models.IntegerField()
    artiste_id = models.IntegerField()
    artistes = models.ForeignKey('Artiste', on_delete=models.CASCADE)


class Lyric(models.Model):
    content = models.CharField(max_length=2000)
    song_id = models.IntegerField()
    songs = models.OneToOneField('Song', on_delete=models.CASCADE)
