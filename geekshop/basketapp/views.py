from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.conf import settings

from mainapp.models import Product
from basketapp.models import Basket

# Create your views here.
  
def basket(request):
    title = "basket"
    basket_items = Basket.objects.filter(user=request.user).order_by("product__category")
    content = {"title": title, "basket_items": basket_items, "media_url": settings.MEDIA_URL}
    return render(request, "basketapp/basket.html", content)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
