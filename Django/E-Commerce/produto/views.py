from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core import serializers
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.forms.models import model_to_dict
from pprint import pprint
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
        variacao_estoque = variacao.estoque
        produto = variacao.produto
        produto_id = produto.id
        produto_nome = produto.nome
        variacao_nome = variacao.nome or ''
        variacao_id = variacao.id
        preco_unitario = variacao.preco
        preco_unitario_promocional = variacao.preco_promocional
        slug = produto.slug 
        if produto.imagem:
            imagem = produto.imagem.url
        else:
            imagem = '' 
        if variacao.estoque < 1:
            messages.warning (
                self.request,
                'Não temos esse produto no estoque'
            )
            return redirect(http_referer)
        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()
        carrinho = self.request.session['carrinho']
        if variacao_id in carrinho:
            # existe no carrinho
            quantidade_atual = carrinho[variacao_id]['quantidade']
            quantidade_atual += 1
            if variacao_estoque < quantidade_atual:
                messages.info (
                    self.request,
                    f'Não temos {quantidade_atual} desse produto no estoque,'
                    f' foram adicionadas {variacao_estoque} unidades.'
                 )
                quantidade_atual = variacao_estoque 
            carrinho[variacao_id]['quantidade'] = quantidade_atual
            carrinho[variacao_id]['preco_quantitativo'] = preco_unitario * quantidade_atual
            carrinho[variacao_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * quantidade_atual     
        else:
            # não existe no carrinho
            carrinho[variacao_id] = {
                'produto_id' : produto_id,
                'produto_nome' : produto_nome,
                'variacao_nome' : variacao_nome,
                'variacao_id': variacao_id,
                'preco_unitario' : preco_unitario,
                'preco_unitario_promocional' : preco_unitario_promocional,
                'preco_quantitativo' : preco_unitario,
                'preco_quantitativo_promocional' : preco_unitario_promocional,
                'quantidade' : 1,
                'slug' : slug, 
                'imagem' : imagem,
            }
            
        self.request.session.save()
        pprint(carrinho)
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
