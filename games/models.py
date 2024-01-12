from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    platform = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    comments = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='game_covers/', blank=True, null=True)

    def __str__(self):
        return self.title
