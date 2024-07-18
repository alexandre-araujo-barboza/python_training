from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models

class ProductsList(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10
    
class ProductDetails(View):

    def get(self, *args, **kargs):
        return HttpResponse('detalhes')

class ProductAddToCart(View):

    def get(self, *args, **kargs):
        return HttpResponse('adicionar')

class ProductRemoveFromCart(View):

    def get(self, *args, **kargs):
        return HttpResponse('remover')

class ProductCart(View):

    def get(self, *args, **kargs):
        return HttpResponse('carrinho')

class ProductFinish(View):

    def get(self, *args, **kargs):
        return HttpResponse('finalizar')
