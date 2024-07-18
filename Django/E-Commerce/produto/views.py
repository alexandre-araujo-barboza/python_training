from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from . import models

class ProductsList(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10
    
class ProductDetails(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'
class ProductAddToCart(View):
    
    def get(self, *args, **kargs):
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )
        variacao_id = self.request.GET.get('vid')
        if not variacao_id:
            messages.error(
                self.request,
                'Produto não existe'
            )
            return redirect(http_referer)
        variacao = get_object_or_404(models.Variacao, id = variacao_id)
        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {

            }
            self.request.session.save()

        carrinho = self.request.session['carrinho']
        if variacao_id in carrinho:
            # variação existe no carrinho
            pass
        else:
            # variação não existe no carrinho
            pass
            
        return HttpResponse(f'{variacao.produto} {variacao.nome}')
class ProductRemoveFromCart(View):

    def get(self, *args, **kargs):
        return HttpResponse('remover')

class ProductCart(View):

    def get(self, *args, **kargs):
        return HttpResponse('carrinho')

class ProductFinish(View):

    def get(self, *args, **kargs):
        return HttpResponse('finalizar')
