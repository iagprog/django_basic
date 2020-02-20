from django.shortcuts import render
from .models import Product, Contact, ProductCategory, ContactCountry

# Create your views here.
def main(request):
    title = "Home"
    excl = Product.objects.filter(category__name = 'exclusive')
    content = {"title": title, "excl": excl}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = "Products"
    excl = Product.objects.filter(category__name = 'exclusive')
    if pk == 1 or pk is None:  # category = 'all'
        products = Product.objects.exclude(category__name = 'exclusive')
    else:
        products = Product.objects.filter(category__pk = pk)
    categories = ProductCategory.objects.exclude(name = 'exclusive')
    content = {"title": title, "excl": excl, "categories": categories, "products": products, "pk":pk}
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = "Contact"
    contacts = Contact.objects.all()[:]
    content = {"title": title, "contacts": contacts}
    return render(request, 'mainapp/contact.html', content)
