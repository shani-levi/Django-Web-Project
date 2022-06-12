from django.db import models

# Create your models here.
class Movie(models.Model):
    picture = models.ImageField(default='default.png', blank=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    plot = models.TextField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    actors = models.TextField()
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.title