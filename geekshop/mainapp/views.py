from django.shortcuts import render
from .models import Product, Contact, ProductCategory, ContactCountry

# Create your views here.
def main(request):
    title = "Home"
    excl = Product.objects.all()[12:]
    content = {"title": title, "excl": excl}
    return render(request, 'mainapp/index.html', content)


def products(request):
    title = "Products"
    excl = Product.objects.all()[12:]
    products = Product.objects.all()[:12]
    categories = ProductCategory.objects.all()[:5]
    content = {"title": title, "excl": excl, "categories": categories, "products": products}
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = "Contact"
    contacts = Contact.objects.all()[:]
    content = {"title": title, "contacts": contacts}
    return render(request, 'mainapp/contact.html', content)


def all(request):
    return render(request, 'mainapp/products.html')


def home(request):
    return render(request, 'mainapp/products.html')


def office(request):
    return render(request, 'mainapp/products.html')


def furniture(request):
    return render(request, 'mainapp/products.html')


def modern(request):
    return render(request, 'mainapp/products.html')


def exclusive(request):
    return render(request, 'mainapp/products.html')
