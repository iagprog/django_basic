from django.contrib import admin
from .models import ProductCategory, Product, ContactCountry, Contact

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ContactCountry)
admin.site.register(Contact)