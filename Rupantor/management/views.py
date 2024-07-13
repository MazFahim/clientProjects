from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .forms import CustomerMessageForm
from .models import *
from django.contrib import messages
from django.utils import timezone


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
    reviews = UserReview.objects.filter(wear=product)

    context = {
        'product': product,
        'reviews': reviews
    }

    template = loader.get_template('product_detail.html')
    return HttpResponse(template.render(context, request))



def testProduct(request):
    #product = get_object_or_404(Wears, productId=product_id)
    template = loader.get_template('product_detail.html')
    return HttpResponse(template.render())



# for this action, login was required
def add_to_cart(request, product_id):
    product = get_object_or_404(Wears, productId=product_id)
    quantity = int(request.POST.get('quantity', 1))

    if request.user.is_authenticated:
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=product
            )
            
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart_item, created = Cart.objects.get_or_create(
            session_key=session_key,
            product=product
        )
        # defaults={'quantity': quantity}
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()
    return redirect('cart')



def cart(request):
    template = loader.get_template('cart.html')

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        shipped_items = Shipping.objects.filter(user=request.user)
    else:
        session_key = request.session.session_key
        cart_items = Cart.objects.filter(session_key=session_key)
        shipped_items = Shipping.objects.filter(session_key=session_key)


    for item in cart_items:
        item.subtotal = item.quantity * item.product.productPrice
    context = {
        'cart_items': cart_items,
        'shipped_items': shipped_items
    }
    return HttpResponse(template.render(context, request))



# for this action, login was required
def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, id=item_id, user=request.user)  
    else:
        session_key = request.session.session_key
        cart_item = get_object_or_404(Cart, id=item_id, session_key=session_key)  

    if request.method == 'POST':
        cart_item.delete()
    return redirect('cart')



def contact(request):
    if request.POST:
        form = CustomerMessageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'contact.html', {'form':CustomerMessageForm})
    


# for this action, login was required
def confirm_shipment(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            cart_items = Cart.objects.filter(user=request.user)
        else:
            session_key = request.session.session_key
            cart_items = Cart.objects.filter(session_key=session_key)

        payment_method = request.POST.get('payment_method')
        delivery_time_from = request.POST.get('delivery_time_from')
        delivery_time_to = request.POST.get('delivery_time_to')

        customer_name = request.POST.get('customer_name')
        customer_address = request.POST.get('customer_address')
        customer_phone = request.POST.get('customer_phone')
        customer_email = request.POST.get('customer_email')
        couponCode = request.POST.get('couponCode')

        coupons = CouponCode.objects.all()

        totalPayableAmount = 0
        total_price = 0

        if request.user.is_authenticated:
            for item in cart_items:
                Shipping.objects.create(
                    user=request.user,
                    product=item.product,
                    quantity=item.quantity,
                    payment_method=payment_method,
                    delivery_time_from=delivery_time_from,
                    delivery_time_to=delivery_time_to,
                    customer_name=customer_name,
                    customer_address=customer_address,
                    customer_phone=customer_phone,
                    customer_email=customer_email
                )
                item.subtotal = item.quantity * item.product.productPrice
                totalPayableAmount = totalPayableAmount + item.subtotal
        else:
            session_key = request.session.session_key
            for item in cart_items:
                Shipping.objects.create(
                    session_key=session_key,
                    product=item.product,
                    quantity=item.quantity,
                    payment_method=payment_method,
                    delivery_time_from=delivery_time_from,
                    delivery_time_to=delivery_time_to,
                    customer_name=customer_name,
                    customer_address=customer_address,
                    customer_phone=customer_phone,
                    customer_email=customer_email
                )
                item.subtotal = item.quantity * item.product.productPrice
                totalPayableAmount = totalPayableAmount + item.subtotal

        for coupon in coupons:
            if coupon.code == couponCode:
                if coupon.discountAmount!=None and coupon.discountPercent == None:
                    total_price = totalPayableAmount - coupon.discountAmount
                elif coupon.discountPercent!=None and coupon.discountAmount == None:
                    total_price = totalPayableAmount - (totalPayableAmount*coupon.discountPercent/100)

        # Clear the Cart after transferring to Shipping
        cart_items.delete()

        template = loader.get_template('orderConfirmed.html')

        context = {
            'TotalPayableAmount':totalPayableAmount,
            'total_price': total_price
        }

        return HttpResponse(template.render(context, request))
    else:
        return redirect('cart')
    


def search(request):

    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            search_result = Wears.objects.filter(productName__icontains=query)
        else:
            search_result = None
        return render(request, 'search_results.html', {'search_results': search_result})
    return render(request, 'search_results.html', {'search_results': None})


# for this action, login was required
def add_review(request, product_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key

        rating = request.POST.get('rating')
        message = request.POST.get('message')
        product = get_object_or_404(Wears, productId=product_id)

        if request.user.is_authenticated:
            review = UserReview.objects.create(
                user=user,
                wear=product,
                message=message,
                rating=rating
            )
        else:
            review = UserReview.objects.create(
                session_key=session_key,
                wear=product,
                message=message,
                rating=rating
            )
        return redirect('product_detail', product_id=product_id)
    
    return HttpResponse("Method Not Allowed", status=405)


def filtered_elements(request):
    template = loader.get_template('filtered_elements.html')

    if request.method == 'GET':
        categories = request.GET.getlist('categories')
        min_price = request.GET.get('min-price')
        max_price = request.GET.get('max-price')

        wears = Wears.objects.all()
        categorized = Wears.objects.all()
        
        if min_price:
            wears = wears.filter(productPrice__gte=float(min_price))
        if max_price:
            wears = wears.filter(productPrice__lte=float(max_price))

        if categories:
            categorized = wears.filter(categories__categoryName__in=categories).distinct()

        context = {
            'items': wears,
            'categorized': categorized
        }
        return HttpResponse(template.render(context, request))
    

def received_shipment(request, item_id):
    try:
        if request.user.is_authenticated:
            shipped_item = get_object_or_404(Shipping, id=item_id, user=request.user)
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            shipped_item = get_object_or_404(Shipping, id=item_id, session_key=session_key)

        # Create a ShippedItems entry
        if request.user.is_authenticated:
            shipped_item_obj = ShippedItems.objects.create(
                user=request.user,
                product = shipped_item.product.productName,
                quantity = shipped_item.quantity,
                customerName = shipped_item.customer_name,
                customerPhone = shipped_item.customer_phone,
                customerEmail = shipped_item.customer_email,
                receivedDate = date.today()
            )
        else:
            shipped_item_obj = ShippedItems.objects.create(
                session_key=session_key,
                product = shipped_item.product.productName,
                quantity = shipped_item.quantity,
                customerName = shipped_item.customer_name,
                customerPhone = shipped_item.customer_phone,
                customerEmail = shipped_item.customer_email,
                receivedDate = date.today()
            )

        if shipped_item_obj: 
            shipped_item.delete()
            messages.success(request, 'Item marked as received and moved to shipped items.')
        else:
            messages.error(request, 'Failed to mark item as received.')

    except Exception as e:
        print(f"Error: {e}")
        messages.error(request, 'An error occurred while processing your request.')
    return redirect('cart')


def purchase_history(request):
    purchaseHistory = ShippedItems.objects.all()
    today = timezone.now().date()
    context = {
        'purchaseHistory': purchaseHistory,
        'today' : today
    }
    template = loader.get_template('purchaseHistory.html')
    return HttpResponse(template.render(context, request))


def return_item(request, item_id):
    if request.user.is_authenticated:
        returned_item = get_object_or_404(ShippedItems, id=item_id, user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        returned_item = get_object_or_404(ShippedItems, id=item_id, session_key=session_key)

    returned_item.delete()
    return redirect('cart')


def about_us(request):
    template = loader.get_template('about_us.html')

    return HttpResponse(template.render())