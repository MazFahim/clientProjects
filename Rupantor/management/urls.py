from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.home, name='home'),
    path('summerwear/', views.summerwear, name='summerwear'),
    path('winterwear/', views.winterwear, name='winterwear'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('individual/', views.testProduct, name='testProduct'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]