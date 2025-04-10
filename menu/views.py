# views.py
from django.shortcuts import render
from .models import Cake, Coffee, Drink

def menu_view(request):
    return render(request, 'menu.html')

def cake_list(request):
    cakes = Cake.objects.all()
    return render(request, 'cake_list.html', {'cakes': cakes})

def coffee_list(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffee_list.html', {'coffees': coffees})

def drink_list(request):
    drinks = Drink.objects.all()
    return render(request, 'drink_list.html', {'drinks': drinks})

from django.shortcuts import render

def menu_view(request):
    return render(request, 'menu.html')  # Бул жерде menu.html деген шаблонду колдоносуңар

# menu/views.py файлын ачып, муну кошуңуз:
from django.shortcuts import render # Бул сап эң башында болушу керек

# ...башка view функцияларыңыз...

def contact_view(request):
    # Бул жөн гана contact.html шаблонун көрсөтөт
    # Азырынча контексттин кереги жок
    context = {
        'page_title': "Байланыш"
    }
    return render(request, 'contact.html', context)