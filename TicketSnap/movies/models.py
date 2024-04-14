from django.db import models

class Movie(models.Model):
    movieId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    duration = models.CharField(max_length=50)
    actors = models.CharField(max_length=255)
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    release_date = models.DateField()
    status = models.CharField(max_length=20)
    trailer_url = models.URLField()
    poster = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.genre} - {self.status}"

class Showtime(models.Model):
    Day_Choices = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    dayofweek = models.CharField(max_length=20, choices=Day_Choices)
    date = models.DateField()
    slot1 = models.ForeignKey(Movie, related_name='slot1', limit_choices_to={'status': 'Now Playing'}, on_delete=models.CASCADE)
    slot2 = models.ForeignKey(Movie, related_name='slot2', limit_choices_to={'status': 'Now Playing'}, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['dayofweek', 'date']

    def __str__(self):
        return f"{self.dayofweek} {self.date}"

class CustomerMessage(models.Model):
    msgID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    msg = models.TextField()