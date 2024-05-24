from django.contrib import admin
from .models import *

# admin.site.register(Wears)
admin.site.register(Cart)
admin.site.register(CustomerMessage)
admin.site.register(Featured)
admin.site.register(Offer)
admin.site.register(Shipping)
admin.site.register(Category)

@admin.register(Wears)
class WearAdmin(admin.ModelAdmin):
    list_display = ['productName', 'summerOrWinter']
    filter_horizontal = ['categories']