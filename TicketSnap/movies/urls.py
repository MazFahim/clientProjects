from django.urls import path 
from . import views

urlpatterns = [
    path('movies/<int:id>/', views.movies, name='movies'),
    path('', views.home, name='home'),
    path('showtime/', views.showtime, name='showtime'),
    path('tickets/<int:id>/', views.tickets, name='tickets'),
    path('contact/', views.contact, name='contact'),
    path('showtimemapper/', views.showtimeMapper, name='showtimemapper'),
]