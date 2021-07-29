from django.shortcuts import render
import json

from mainapp.models import Product

from mainapp.models import ProductCategory


def index(request):
    title = 'каталог'

    # with open('mainapp/templates/mainapp/links_menu.json') as f:
    #     links_menu = json.load(f)
    links_menu = ProductCategory.objects.all()

    products = Product.objects.all()[0:3]

    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': products
    }
    return render(request, 'mainapp/products.html', context)