from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    bio = models.TextField()
    image = models.ImageField(upload_to ='images/', null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist,related_name="albums", on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    cover = models.ImageField(upload_to ='images/')
    year = models.DateField()

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    title = models.CharField(max_length=80)

    def __str__(self):
        return self.title
    




    