from django.shortcuts import render
import json

def index(request):
    title = 'каталог'

    with open('mainapp/templates/mainapp/links_menu.json') as f:
        links_menu = json.load(f)

    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)