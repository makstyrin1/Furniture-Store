from math import fabs
from django.shortcuts import render, get_object_or_404

from goods.models import Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }
    return render(request, "goods/product.html", context=context)
