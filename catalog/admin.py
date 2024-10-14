from django.contrib import admin
from .models import Product, ProductType, Storage, Manufacturer

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Storage)
admin.site.register(Manufacturer)
