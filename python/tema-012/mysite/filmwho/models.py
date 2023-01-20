from django.db import models

# Create your models here.
class Director(models.Model):
    director_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=50)
    movie = models.ManyToManyField('Movie', related_name='directors', null=True, blank=True)
    picture = models.ImageField(upload_to='images/directors', null=True, blank=True)

    def __str__(self):
        return self.name

    def directed_movies(self):
        return self.movie.all()

    def movie_count(self):
        return self.movie.count()

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=280)
    run_time = models.IntegerField()
    director = models.ManyToManyField(Director, related_name='movies', null=True, blank=True)
    poster = models.ImageField(upload_to='images/posters/', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_directors(self):
        return  self.directors.all()

    def directors_count(self):
        return  self.directors.count()
