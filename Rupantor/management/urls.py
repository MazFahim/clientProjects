from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.home, name='home'),
    path('summerwear/', views.summerwear, name='summerwear'),
    path('winterwear/', views.winterwear, name='winterwear'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('received_shipment/<int:item_id>/', views.received_shipment, name='received_shipment'),
    # Confirming shipment
    path('confirm_shipment/', views.confirm_shipment, name='confirm_shipment'),
    path('search/', views.search, name='search'),
    path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
    #for filtering
    path('filtered_elements/', views.filtered_elements, name='filtered_elements'),
    #for purchase history
    path('purchase_history/', views.purchase_history, name='purchase_history'),
    #for returning product
    path('return_item/<int:item_id>/', views.return_item, name='return_item'),
    #for about us
    path('about_us/', views.about_us, name='about_us'),
    #for cancelling shipment
    path('cancel_shipment/<int:item_id>/', views.cancel_shipment, name='cancel_shipment'),
]