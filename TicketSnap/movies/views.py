from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import CustomerMessageForm
from django.db import transaction

def movies(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

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
def tickets(request):
    if request.method == 'POST':
        showtime_mapper_id = request.POST.get('showtime_mapper')
        seat_ids = request.POST.getlist('seats')
        showtime_mapper = ShowtimeMapper.objects.get(id=showtime_mapper_id)

        with transaction.atomic():
            if Booking.objects.filter(bookingTime=showtime_mapper, seat__in=seat_ids, is_booked=True).exists():
                return HttpResponse("One or more seats are already booked.", status=400)

            # Check if this user has already booked any of these seats for this showtime
            if Booking.objects.filter(bookingTime=showtime_mapper, seat__in=seat_ids, user=request.user).exists():
                return HttpResponse("You have already booked one or more of the selected seats for this showtime.", status=400)

            # Create bookings for the selected seats
            for seat_id in seat_ids:
                seat = Seat.objects.get(id=seat_id)
                Booking.objects.create(
                    seat=seat,
                    bookingTime=showtime_mapper,
                    user=request.user,
                    is_booked=True
                )
        return redirect('/')  # Assuming you want to redirect to the home page on success
    showtimes = ShowtimeMapper.objects.all().select_related('movie')
    seats = Seat.objects.all()  # You might want to filter this if your seat list is too long
    context = {
        'showtimes': showtimes,
        'seats': seats,
        'rows': 'ABCDE',
        'numbers': range(1, 9)
    }
    return render(request, 'tickets.html', context)


# @login_required
# def tickets(request):
#     # Pre-fetch all showtimes and their related movies
#     showtimes = ShowtimeMapper.objects.all().select_related('movie')
    
#     # Pre-fetch all seats and order them by row and number for display
#     seats = Seat.objects.all().order_by('row', 'number')

#     # Organize seats by rows
#     seats_by_row = {row: [] for row in 'ABCDE'}  # Assuming rows are labeled from 'A' to 'E'
#     for seat in seats:
#         seats_by_row[seat.row].append(seat)

#     if request.method == 'POST':
#         # Extract the selected showtime and seats from the POST request
#         showtime_mapper_id = request.POST.get('showtime_mapper')
#         seat_ids = request.POST.getlist('seats')
#         showtime_mapper = ShowtimeMapper.objects.get(id=showtime_mapper_id)
        
#         with transaction.atomic():
#             # Check for already booked seats
#             if Booking.objects.filter(bookingTime=showtime_mapper, seat_id__in=seat_ids, is_booked=True).exists():
#                 return HttpResponse("One or more seats are already booked.", status=400)

#             # Check if the user has already booked any of these seats for this showtime
#             if Booking.objects.filter(bookingTime=showtime_mapper, seat_id__in=seat_ids, user=request.user).exists():
#                 return HttpResponse("You have already booked one or more of the selected seats for this showtime.", status=400)

#             # Proceed to create bookings for each selected seat
#             for seat_id in seat_ids:
#                 seat = Seat.objects.get(id=seat_id)
#                 Booking.objects.create(
#                     seat=seat,
#                     bookingTime=showtime_mapper,
#                     user=request.user,
#                     is_booked=True
#                 )
        
#         # Redirect to a success or home page upon successful booking
#         return redirect('/')

#     # For GET requests or initial page load, prepare the context data for the template
#     context = {
#         'showtimes': showtimes,
#         'seats_by_row': seats_by_row,
#     }
#     return render(request, 'tickets.html', context)


def contact(request):
    if request.POST:
        form = CustomerMessageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'contact.html', {'form':CustomerMessageForm})