from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    artist = models.CharField(max_length=255)
    album_title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(upload_to='album/%Y/%m/%d')

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + '-' + self.artist
        

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': album_id})

    def __str__(self):
        return self.song_title
