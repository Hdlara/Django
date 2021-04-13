from django.urls import path

from.views import index, contato, product

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato),
    path('product/<int:id>', product, name='product'),
]