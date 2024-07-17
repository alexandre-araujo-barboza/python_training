from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class OrderPayment(View):

    def get(self, *args, **kargs):
        return HttpResponse('pagamento')

class OrderClose(View):

    def get(self, *args, **kargs):
        return HttpResponse('fechar')

class OrderDetails(View):

    def get(self, *args, **kargs):
        return HttpResponse('detalhes')
