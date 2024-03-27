from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.home, name='home'),
    path('summerwear/', views.summerwear, name='summerwear'),
    path('winterwear/', views.winterwear, name='winterwear'),
]