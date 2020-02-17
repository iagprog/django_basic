from django.shortcuts import render
from .models import Product, Contact, ProductCategory, ContactCountry

# Create your views here.
def main(request):
    title = "Home"
    excl = Product.objects.all()[12:]
    content = {"title": title, "excl": excl}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = "Products"
    excl = Product.objects.all()[12:]
    products = Product.objects.all()[:12]
    categories = ProductCategory.objects.all()[:]
    content = {"title": title, "excl": excl, "categories": categories, "products": products, "pk":pk}
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = "Contact"
    contacts = Contact.objects.all()[:]
    content = {"title": title, "contacts": contacts}
    return render(request, 'mainapp/contact.html', content)
