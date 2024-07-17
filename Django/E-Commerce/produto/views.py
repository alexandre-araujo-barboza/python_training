from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

class ProductsList(ListView):
    pass

class ProductDetails(View):
    pass

class ProductAddToCart(View):
    pass

class ProductRemoveFromCart(View):
    pass

class ProductCart(View):
    pass

class ProductFinish(View):
    pass
