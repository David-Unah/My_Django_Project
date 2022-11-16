from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
class Song(models.Model):
    title = models.CharField(max_length=40)
    date_released = models.DateField()
    artiste_id = models.IntegerField()
class Lyrics(models.Model):
    content = models.CharField(max_length=400)
    song_id = models.IntegerField()
