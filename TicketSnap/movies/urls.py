from django.urls import path 
from . import views

urlpatterns = [
    path('movies/', views.movies, name='movies'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact')
]