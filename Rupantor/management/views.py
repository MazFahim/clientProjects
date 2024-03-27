from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def test(request):
    return HttpResponse('Rupantor')

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def summerwear(request):
    template = loader.get_template('summerwear.html')
    return HttpResponse(template.render())

def winterwear(request):
    template = loader.get_template('winterwear.html')
    return HttpResponse(template.render())

def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render())