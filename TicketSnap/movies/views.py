from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def movies(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def showtime(request):
    template = loader.get_template('showtime.html')
    return HttpResponse(template.render())

def tickets(request):
    template = loader.get_template('tickets.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())