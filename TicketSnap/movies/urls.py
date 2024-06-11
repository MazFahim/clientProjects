from django.urls import path 
from . import views

urlpatterns = [
    path('movies/<int:id>/<slug:date>/<slug:slotChoice>/', views.tickets, name='movies'),
    path('', views.home, name='home'),
    path('showtime/', views.showtime, name='showtime'),
    path('contact/', views.contact, name='contact'),
    path('showtimemapper/', views.showtimeMapper, name='showtimemapper'),
    path('book_seats/', views.book_seats, name='book_seats'),
    path('checkout/', views.checkout, name='checkout'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:movie_id>/add_review/', views.add_review, name='add_review'),
    path('cart/', views.cart, name='cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkCoupon/', views.checkCoupon, name='checkCoupon')
]