from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

def test(request):
    cart = Cart.objects.all().values()
    template = loader.get_template('test.html')
    context = {
        'cart' : cart
    }
    # return HttpResponse(template.render(context, request))
    return HttpResponse('Hello')


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
    wears = Wears.objects.all().values()

    context = {
        'wears' : wears
    }
    template = loader.get_template('summerwear.html')
    return HttpResponse(template.render(context, request))


def winterwear(request):
    wears = Wears.objects.all().values()

    context = {
        'wears' : wears
    }
    template = loader.get_template('winterwear.html')
    return HttpResponse(template.render(context, request))


def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())