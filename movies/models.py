from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return self.title