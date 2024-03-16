from django.urls import path 
from . import views

urlpatterns = [
    path('movies/', views.movies, name='movies'),
    path('home/', views.home, name='home'),
    path('showtime/', views.showtime, name='showtime'),
    path('tickets/', views.tickets, name='tickets'),
    path('contact/', views.contact, name='contact')
]