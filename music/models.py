from django.db import models


class Album(models.Model):

    album_title = models.CharField(max_length=500),
    genre = models.CharField(max_length=250),
    album_logo = models.CharField(max_length=500)


class Song(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE),
    song_title = models.CharField(max_length=500),
    file_type = models.CharField(max_length=10)






