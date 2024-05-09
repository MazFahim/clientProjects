from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import CustomerMessageForm
from django.db import transaction
from django.contrib import messages

def movies(request, id):
    template = loader.get_template('first.html')
    context = {
        'movie' : movie
    }
    return HttpResponse(template.render(context, request))

def home(request):
    movies = Movie.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'movies' : movies
    }
    return HttpResponse(template.render(context, request))
    

def showtime(request):
    movieSchedules = Showtime.objects.order_by('-date')[:6].values()
    movies = Movie.objects.all().values()

    template = loader.get_template('showtime.html')
    context = {
        'movieSchedules' : movieSchedules,
        'movies' : movies
    }
    return HttpResponse(template.render(context, request))


@login_required
def tickets(request, id):
    movie = Movie.objects.get(pk=id)
    if request.method == 'POST':
        showtime_mapper_id = request.POST.get('showtime_mapper')
        seat_ids = request.POST.getlist('seats')
        showtime_mapper = ShowtimeMapper.objects.get(id=showtime_mapper_id)

        with transaction.atomic():
            if Booking.objects.filter(bookingTime=showtime_mapper, seat__in=seat_ids, is_booked=True).exists():
                return HttpResponse("One or more seats are already booked.", status=400)

            if Booking.objects.filter(bookingTime=showtime_mapper, seat__in=seat_ids, user=request.user).exists():
                return HttpResponse("You have already booked one or more of the selected seats for this showtime.", status=400)

            booked_seats = []
            for seat_id in seat_ids:
                seat = Seat.objects.get(id=seat_id)
                Booking.objects.create(
                    seat=seat,
                    bookingTime=showtime_mapper,
                    user=request.user,
                    is_booked=True
                )
                booked_seats.append(seat_id)

            return redirect('/') 
    showtimes = ShowtimeMapper.objects.all().select_related('movie')
    seats = Seat.objects.all()  
    context = {
        'movie': movie,
        'showtimes': showtimes,
        'seats': seats,
        'rows': 'ABCDE',
        'numbers': range(1, 9)
    }
    return render(request, 'tickets.html', context)

def showtimeMapper(request):
    showtimes = ShowtimeMapper.objects.all().values()
    movies = Movie.objects.all().values()
    template = loader.get_template('showtimemapper.html')
    context = {
        'showtimes' : showtimes,
        'movies' : movies
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    if request.POST:
        form = CustomerMessageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'contact.html', {'form':CustomerMessageForm})