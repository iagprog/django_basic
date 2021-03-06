from django.db import models
from django.conf import settings

from mainapp.models import Product

# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE, related_name = 'basket')
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity',default = 0)
    add_datetime = models.DateTimeField(verbose_name='add_datetime',auto_now_add=True)
