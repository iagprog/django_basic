from django.shortcuts import render
from .models import Product, Contact, ProductCategory, ContactCountry

# Create your views here.
def main(request):
    title = "Home"
    excl_main = Product.objects.all()[:2]
    content = {"title": title, "excl_main": excl_main}
    return render(request, 'mainapp/index.html', content)


def products(request):
    title = "Products"
    links_menu = [
        {
            "href": "products_all",
            "name": "all"
        },
        {
            "href": "products_home",
            "name": "home"
        },
        {
            "href": "products_office",
            "name": "office"
        },
        {
            "href": "products_furniture",
            "name": "furniture"
        },
        {
            "href": "products_modern",
            "name": "modern"
        },
        {
            "href": "products_classic",
            "name": "classic"
        }
    ]
    excl_products = Product.objects.all()[:2]
    products = Product.objects.all()[2:]
    content = {"title": title, "links_menu": links_menu, "products": products, "excl_products": excl_products}
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = "Contact"
    contacts = Contact.objects.all()[:]
    content = {"title": title, "contacts": contacts}
    return render(request, 'mainapp/contact.html', content)


def products_all(request):
    return render(request, 'mainapp/products.html')


def products_home(request):
    return render(request, 'mainapp/products.html')


def products_office(request):
    return render(request, 'mainapp/products.html')


def products_furniture(request):
    return render(request, 'mainapp/products.html')


def products_modern(request):
    return render(request, 'mainapp/products.html')
