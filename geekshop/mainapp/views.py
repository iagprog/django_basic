from django.shortcuts import render

# Create your views here.
def main(request):
    title = "Home"
    excl_main = [
        {
        "name": "Fishnet Chair1",
        "descr": "Seat and back with upholstery made of cold cure foam. Steel frame, available in matt",
        "img_src": "exclusive-img1.jpg",
        "img_ref": "#",
        "alt": "exclusive-img1.jpg"
        },
        {
        "name": "Fishnet Chair2",
        "descr": "Seat and back with upholstery made of cold cure foam. Steel frame, available in matt",
        "img_src": "exclusive-img2.jpg",
        "img_ref": "#",
        "alt": "exclusive-img2.jpg"
        }
    ]
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
    products = [
        {
        "name": "chair",
        "type": "office-chair",
        "img_src": "product1.jpg",
        "img_ref": "/products/1",
        "alt": "product1"
        },
        {
        "name": "chair",
        "type": "modern-chair",
        "img_src": "product2.jpg",
        "img_ref": "/products/2",
        "alt": "product2",
        },
        {
        "name": "chair",
        "type": "cool-chair",
        "img_src": "product3.jpg",
        "img_ref": "/products/3",
        "alt": "product3"
        }
    ]
    excl_products = [
        {
        "name": "Fishnet Chair1",
        "descr": "Seat and back with upholstery made of cold cure foam. Steel frame, available in matt",
        "img_src": "exclusive-img1.jpg",
        "img_ref": "#",
        "alt": "exclusive-img1.jpg"
        },
        {
        "name": "Fishnet Chair2",
        "descr": "Seat and back with upholstery made of cold cure foam. Steel frame, available in matt",
        "img_src": "exclusive-img2.jpg",
        "img_ref": "#",
        "alt": "exclusive-img2.jpg"
        }
    ]
    content = {"title": title, "links_menu": links_menu, "products": products, "excl_products": excl_products}
    return render(request, 'mainapp/products.html', content)

def contact(request):
    title = "Contact"
    contacts = [
        {           
            "country": "Thailand",
            "phone": "9999 - 1234 -5678",
            "email": "thailand@interior.com",
            "address": "9999 W 1st St, 90001 Thailand",
            "img_src": "location-image.jpg",
            "alt": "location-image.jpg"
        },
        {           
            "country": "Vietnam",
            "phone": "8888 - 1234 -5678",
            "email": "vietnam@interior.com",
            "address": "8888 W 1st St, 90001 Vietnam",
            "img_src": "location-image.jpg",
            "alt": "location-image.jpg"
        },
        {           
            "country": "Costa-Rica",
            "phone": "7777 - 1234 -5678",
            "email": "costa-rica@interior.com",
            "address": "7777 W 1st St, 90001 Costa-Rica",
            "img_src": "location-image.jpg",
            "alt": "location-image.jpg"
        }
    ]
    content = {"title": title, "contacts": contacts}
    return render(request, 'mainapp/products.html', content)

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

def products_modern(request):
    return render(request, 'mainapp/products.html')

