from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='name', max_length=64, unique=True)
    description = models.TextField(verbose_name='description', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='product name', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name='short products description',max_length=64,blank=True)
    description = models.TextField(verbose_name='description', blank=True)
    price = models.DecimalField(verbose_name='product price', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='store quantity')

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class ContactCountry(models.Model):
    name = models.CharField(verbose_name='country', max_length=64, unique=True)
    info = models.TextField(verbose_name='info', blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    country = models.ForeignKey(ContactCountry, on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='phone', max_length=64,blank=True)
    email = models.CharField(verbose_name='email', max_length=64,blank=True)
    address = models.CharField(verbose_name='address', max_length=128)
    image = models.ImageField(upload_to='contact_images', blank=True)
    short_desc = models.CharField(verbose_name='short location description', max_length=64, blank=True)

    def __str__(self):
        return self.country.name
