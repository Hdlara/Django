from django.shortcuts import render

from .models import Product

def index(request):
    products = Product.objects.all()

    context = {
        'curso': 'Programação web com Django Framework',
        'outros': 'Jango é massa',
        'products': products
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')

def product(request, id):
    prod = Product.objects.get(id=id)
    context = {
        'product': prod
    }
    return render(request, 'product.html', context)