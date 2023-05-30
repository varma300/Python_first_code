from django.contrib import admin
from.models import Product, offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','stock', 'image')
  
class OfferAdmin(admin.ModelAdmin):
    list_display=('code','discount')
    
# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(offer, OfferAdmin)