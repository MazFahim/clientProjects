from django.db import models

class CardData(models.Model):
    movieName = models.CharField(max_length=100)
    # poster = models.ImageField(upload_to=<>)
    releaseDate = models.DateField()
