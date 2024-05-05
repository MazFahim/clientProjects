from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
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


def product_detail(request, product_id):
    product = get_object_or_404(Wears, productId=product_id)
    return render(request, 'product_detail.html', {'product': product})


def testProduct(request):
    #product = get_object_or_404(Wears, productId=product_id)
    template = loader.get_template('product_detail.html')
    return HttpResponse(template.render())

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Wears, productId=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': quantity}
    )
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    return redirect('cart')

def cart(request):
    template = loader.get_template('cart.html')
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        item.subtotal = item.quantity * item.product.productPrice
    context = {
        'cart_items': cart_items
    }
    return HttpResponse(template.render(context, request))


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)  # Ensures the item belongs to the user
    if request.method == 'POST':
        cart_item.delete()
    return redirect('cart')

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())