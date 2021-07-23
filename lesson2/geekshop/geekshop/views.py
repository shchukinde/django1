from django.shortcuts import render
from datetime import date

def index(request):
    context = {
        'slogan':'Супер предложения',
        'time' : date.today()
    }
    return render(request, 'geekshop/index.html', context)

def contacts(request):
    return render(request, 'geekshop/contact.html')