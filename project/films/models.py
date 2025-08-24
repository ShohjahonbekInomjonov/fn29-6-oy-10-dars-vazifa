from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name="Janr Nomi")

    class Meta:
        ordering = ['name']
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        db_table = 'genres'

    def __str__(self) -> str:
        return f"{self.name}"
    

class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kino Nomi")
    year = models.IntegerField(verbose_name="Kino chiqarilgan yili")
    description = models.TextField(null=True, blank=True, verbose_name="Matni")
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    photo = models.ImageField(upload_to='images', null=True, blank=True, verbose_name="Rasmi")
    video = models.FileField(upload_to='videos', null=True, blank=True, verbose_name="Videosi")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="movies", verbose_name="Janr")

    class Meta:
        ordering = ['title']
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        db_table = 'movies'
    
    def __str__(self) -> str:
        return f"{self.title}"
    

class Comment(models.Model):
    text = models.CharField(max_length=500, verbose_name="Izoh")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Kino")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'
        ordering = ['-created']
        