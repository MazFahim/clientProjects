from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import CustomerMessageForm
from django.db import transaction
from django.http import JsonResponse



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



#login was required here
def tickets(request, id, date, slotChoice):
    movie = Movie.objects.get(pk=id)
    seats = Seat.objects.all()
    showtime_mapper = ShowtimeMapper.objects.get(pk=id)
    booked_seats = Booking.objects.filter(bookingTime=showtime_mapper).values_list('seat__id', flat=True)

    template = loader.get_template('tickets.html')
    context = {
        'showtime_mapper_id' : id,
        'movie' : movie,
        'rows': 'ABCDE',
        'seats' : seats,
        'date' : date,
        'slotchoice' : slotChoice,
        'booked_seats': booked_seats
    }
    return HttpResponse(template.render(context, request))



#login was required here
def book_seats(request):
    if request.method == 'POST':
        seat_ids = request.POST.getlist('seats')
        showtime_mapper_id = request.POST.get('showtime_mapper_id')
        showtime_mapper = ShowtimeMapper.objects.get(id=showtime_mapper_id)
        request.session['booked_seats'] = seat_ids

        with transaction.atomic():
            if Booking.objects.filter(bookingTime=showtime_mapper, seat__in=seat_ids).exists():
                return HttpResponse("One or more seats are already booked.", status=400)
            
            if request.user.is_authenticated:    
                for seat_id in seat_ids:
                    seat = Seat.objects.get(id=seat_id)
                    Booking.objects.create(
                        seat=seat,
                        bookingTime=showtime_mapper,
                        user=request.user,
                        is_booked=True
                    )
            else:
                session_key = request.session.session_key
                for seat_id in seat_ids:
                    seat = Seat.objects.get(id=seat_id)
                    Booking.objects.create(
                        seat=seat,
                        bookingTime=showtime_mapper,
                        session_key=session_key,
                        is_booked=True
                    )


        request.session['showtime_mapper_id'] = showtime_mapper_id
        return redirect('checkout')
    


def checkout(request):
    seat_ids = request.session.get('booked_seats', [])
    showtime_mapper_id = request.session.get('showtime_mapper_id')
    seats = Seat.objects.filter(id__in=seat_ids)
    coupons = CouponCode.objects.all()
    total_price = sum(250 for seat in seats)
    
    if request.method == 'POST':
        request.session.pop('booked_seats', None)
        request.session.pop('showtime_mapper_id', None)

        couponCode = request.POST.get('couponCode')

        for coupon in coupons:
            if coupon.code == couponCode:
                if coupon.discountAmount!=None and coupon.discountPercent == None:
                    total_price = total_price - coupon.discountAmount
                elif coupon.discountPercent!=None and coupon.discountAmount == None:
                    total_price = total_price - (total_price*coupon.discountPercent/100)
        return render(request, 'confirmation.html', {'seats': seats, 'total_price': total_price})

    return render(request, 'checkout.html', {'seats': seats, 'total_price': total_price, 'coupons': coupons})



def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, movieId=movie_id)
    reviews = UserReview.objects.filter(movie=movie)

    context = {
        'movie' : movie,
        'reviews' : reviews
    }
    
    template = loader.get_template('movieDetails.html')
    return HttpResponse(template.render(context, request))



def add_review(request, movie_id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        message = request.POST.get('message')
        if request.user.is_authenticated:
            user = request.user
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
        product = get_object_or_404(Movie, movieId=movie_id)

        if request.user.is_authenticated:
            review = UserReview.objects.create(
                user=user,
                movie=product,
                message=message,
                rating=rating
            )
        else:
            review = UserReview.objects.create(
                session_key=session_key,
                movie=product,
                message=message,
                rating=rating
            )

        return redirect('movie_detail', movie_id=movie_id)
    
    return HttpResponse("Method Not Allowed", status=405)


def cart(request):
    template = loader.get_template('cart.html')

    if request.user.is_authenticated:
        bookedTickets = Booking.objects.filter(user=request.user)
    else:
        session_key = request.session.session_key
        bookedTickets = Booking.objects.filter(session_key=session_key)

    context = {
        'bookedTickets' : bookedTickets
    }
    return HttpResponse(template.render(context, request))


def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        booked_seat = get_object_or_404(Booking, id=item_id, user=request.user)
    else:
        session_key = request.session.session_key
        booked_seat = get_object_or_404(Booking, id=item_id, session_key=session_key)  
    
    if request.method == 'POST':
        booked_seat.delete()
    return redirect('cart')


def about_us(request):
    template = loader.get_template('about_us.html')

    return HttpResponse(template.render())