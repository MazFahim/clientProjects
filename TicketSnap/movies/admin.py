from django.contrib import admin
from .models import *

admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(ShowtimeMapper)
admin.site.register(CustomerMessage)
admin.site.register(Seat)
admin.site.register(Booking)
admin.site.register(CouponCode)