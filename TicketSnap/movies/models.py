from django.db import models
from django.conf import settings

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


class Seat(models.Model):    
    row = models.IntegerField()
    number = models.IntegerField()
    # is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('row', 'number')

    def __str__(self):
        return f"Row {self.row} Seat {self.number}"

class ShowtimeMapper(models.Model):
    SLOT_CHOICES = [
        ('Slot1', 'Slot 1'),
        ('Slot2', 'Slot 2'),
    ]

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    slotChoice = models.CharField(max_length=20, choices=SLOT_CHOICES, default='slot not chosen')

    def __str__(self):
        return f"{self.date} - {self.slotChoice} - {self.movie}"

class Booking(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, null=True)
    bookingTime = models.ForeignKey(ShowtimeMapper, on_delete=models.CASCADE, null=True)
    is_booked = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart',
        null=True
    )
    class Meta:
        unique_together = ('seat', 'bookingTime')

    def __str__(self):
        return f"Booking for {self.bookingTime}-{self.user}"
