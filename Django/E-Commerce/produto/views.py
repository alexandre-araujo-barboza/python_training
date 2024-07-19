from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import SuspiciousOperation
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
        produto_id  = self.request.GET.get('produto')
        variacao_id = self.request.GET.get('vid')
        if not variacao_id:
            produto = get_object_or_404(models.Produto, id = produto_id)
            estoque = produto.estoque
            variacao_id   = 0
            produto_id = 's' + str(produto_id)
            variacao_nome = ''
            preco_unitario = produto.preco_marketing
            preco_unitario_promocional = produto.preco_marketing_promocional
        else:
            variacao = get_object_or_404(models.Variacao, id = variacao_id)
            estoque = variacao.estoque
            produto_id = 0
            variacao_id = 'v' + str(variacao_id)
            variacao_nome = variacao.nome
            preco_unitario = variacao.preco
            preco_unitario_promocional = variacao.preco_promocional
            produto = variacao.produto
        produto_nome = produto.nome
        produto_tipo = produto.tipo
        produto_slug = produto.slug
        if produto.imagem:
            imagem = produto.imagem.url
        else:
            imagem = ''
        
        if variacao_id:
            message = 'Não temos produto com esse tipo no estoque'
        else:
            message = 'Não temos esse produto no estoque'
        
        if estoque < 1:
            messages.warning (
                self.request,
                message
            )
            return redirect(http_referer)
        
        dicionario = {
            'produto_id' : produto_id,
            'variacao_id' : variacao_id,
            'produto_nome' : produto_nome,
            'variacao_nome' : variacao_nome,
            'preco_unitario' : preco_unitario,
            'preco_unitario_promocional' : preco_unitario_promocional,
            'preco_quantitativo' : preco_unitario,
            'preco_quantitativo_promocional' : preco_unitario_promocional,
            'quantidade' : 1,
            'tipo': produto_tipo,
            'slug' : produto_slug, 
            'imagem' : imagem,
        }

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()
        carrinho = self.request.session['carrinho']
        flag_limit_in_stock = False
        
        if variacao_id in carrinho and carrinho[variacao_id]['tipo'] == 'V':
            quantidade_atual = carrinho[variacao_id]['quantidade']
        elif produto_id in carrinho and carrinho[produto_id]['tipo'] == 'S':
            quantidade_atual = carrinho[produto_id]['quantidade']
        else:
            quantidade_atual = 0
        
        if variacao_id in carrinho and variacao_id and carrinho[variacao_id]['tipo'] == 'V': 
            message = f'Não temos {quantidade_atual +1} desse tipo de produto no estoque, já foram adicionadas {quantidade_atual} unidades.'
        elif produto_id in carrinho and produto_id and carrinho[produto_id]['tipo'] == 'S': 
            message = f'Não temos {quantidade_atual +1} desse produto no estoque, já foram adicionadas {quantidade_atual} unidades.'
        else:
            if quantidade_atual != 0:
                raise SuspiciousOperation("Algo não está correto com a sua sessão")
        
        if variacao_id in carrinho and carrinho[variacao_id]['tipo'] == 'V':
            # variacao existe no carrinho
            quantidade_atual += 1
            if estoque < quantidade_atual:
                messages.info (
                    self.request,
                    message,
                )
                flag_limit_in_stock = True
            else:     
                carrinho[variacao_id]['quantidade'] = quantidade_atual
                carrinho[variacao_id]['preco_quantitativo'] = preco_unitario * quantidade_atual
                carrinho[variacao_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * quantidade_atual

        elif produto_id in carrinho and carrinho[produto_id]['tipo'] == 'S':
            # produto existe no carrinho
            quantidade_atual += 1
            if estoque < quantidade_atual:
                messages.info (
                    self.request,
                    message,
                )
                flag_limit_in_stock = True
            else:     
                carrinho[produto_id]['quantidade'] = quantidade_atual
                carrinho[produto_id]['preco_quantitativo'] = preco_unitario * quantidade_atual
                carrinho[produto_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * quantidade_atual
        else:
            # não existe no carrinho
            if (variacao_id):
                carrinho[variacao_id] = dicionario
            else:
                carrinho[produto_id]  = dicionario 
        
        if not flag_limit_in_stock:
            if variacao_id:
                message = f'Adicionamos no seu carrinho o produto {produto_nome} do tipo {variacao_nome}.'
            else:
                message = f'Adicionamos no seu carrinho o produto {produto_nome}.'     
            messages.success (
                self.request,
                message
            )
        
        self.request.session.save()
        return redirect(http_referer)      
        
class ProductRemoveFromCart(View):

    def get(self, *args, **kargs):
        return HttpResponse('remover')

class ProductCart(View):

    def get(self, *args, **kargs):
        return render(self.request, 'produto/carrinho.html')

class ProductFinish(View):

    def get(self, *args, **kargs):
        return HttpResponse('finalizar')
