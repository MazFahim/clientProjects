from django.db import models

class CardData(models.Model):
    movieName = models.CharField(max_length=100)
    # poster = models.ImageField(upload_to=<>)
    releaseDate = models.DateField()

class Movie(models.Model):
    movieId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    actors = models.CharField(max_length=255)
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    release_date = models.DateField()
    status = models.CharField(max_length=20)
    trailer_url = models.URLField()

class Showtime(models.Model):
    Day_Choices = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    
    dayofweek = models.CharField(max_length=20, choices=Day_Choices)
    date = models.DateField()
    slot1 = models.TimeField()
    slot2 = models.TimeField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title} - {self.day_of_week} {self.date}"

class CustomerMessage(models.Model):
    msgID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=20)
    msg = models.TextField()