from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import CustomerMessageForm

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
    movieSchedules = Showtime.objects.all().values()
    template = loader.get_template('showtime.html')
    context = {
        'movieSchedules' : movieSchedules
    }
    return HttpResponse(template.render(context, request))

def tickets(request):
    template = loader.get_template('tickets.html')
    return HttpResponse(template.render())

def contact(request):
    if request.POST:
        form = CustomerMessageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'contact.html', {'form':CustomerMessageForm})