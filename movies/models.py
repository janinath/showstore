from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.TextField(max_length=100,null=True)
    description = models.TextField(max_length=600,null=True)

    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.TextField(max_length=100,null=True)
    image = models.ImageField(upload_to='actors/',null=True)
    bio = models.TextField(max_length=600,null=True)
    
    def __str__(self):
        return self.name
class Director(models.Model):
    name = models.TextField(max_length=100,null=True)
    bio = models.TextField(max_length=600,null=True)
    image = models.ImageField(upload_to='directors/',null=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.TextField(max_length=100,null=True)
    description = models.TextField(max_length=900,null=True)
    release_date = models.DateField(null=True)
    duration = models.DurationField(null=True)
    rating = models.FloatField(null=True)
    poster_image = models.ImageField(upload_to='posters/',null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,null=True)
    actors = models.ManyToManyField(Actor,null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title