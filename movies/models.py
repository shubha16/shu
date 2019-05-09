from django.db import models

class movie1(models.Model):
    actor = models.CharField(max_length=30)
    actor_movie = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    movie_logo = models.CharField(max_length=100)

    def __str__(self):
         return self.actor + '---' + self.actor_movie
class Song (models.Model):
        movie = models.ForeignKey(movie1, on_delete=models.CASCADE)
        file_type = models.CharField(max_length=50)
        song_name = models.CharField(max_length=100)

