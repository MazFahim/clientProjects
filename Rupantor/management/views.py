from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

def test(request):
    return HttpResponse('Rupantor')


def home(request):
    featured = Featured.objects.all().values()
    offers = Offer.objects.all().values()
    products = Wears.objects.all().values()

    context = {
        'featured' : featured,
        'offers' : offers,
        'products' : products
    }

    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))


def summerwear(request):
    template = loader.get_template('summerwear.html')
    return HttpResponse(template.render())


def winterwear(request):
    template = loader.get_template('winterwear.html')
    return HttpResponse(template.render())


def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())