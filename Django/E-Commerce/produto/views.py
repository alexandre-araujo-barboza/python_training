from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
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
            variacao_estoque = 0
            variacao_nome = ''
            produto_estoque = produto.estoque 
            preco_unitario = produto.preco_marketing
            preco_unitario_promocional = produto.preco_marketing_promocional
        else:
            variacao = get_object_or_404(models.Variacao, id = variacao_id)
            variacao_estoque = variacao.estoque
            variacao_nome = variacao.nome
            produto_estoque = 0
            preco_unitario = variacao.preco
            preco_unitario_promocional = variacao.preco_promocional
            produto = variacao.produto
        produto_nome = produto.nome
        slug = produto.slug
        if produto.imagem:
            imagem = produto.imagem.url
        else:
            imagem = ''
        
        if variacao_id and variacao.estoque < 1:
            messages.warning (
                self.request,
                'Não temos produto com esse tipo no estoque'
            )
            return redirect(http_referer)
        elif not variacao_id and produto.estoque < 1:
            messages.warning (
                self.request,
                'Não temos esse produto no estoque'
            )
            return redirect(http_referer)
        
        dicionario = {
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

        if not self.request.session.get('carrinho'):
            self.request.session['carrinho'] = {}
            self.request.session.save()
        carrinho = self.request.session['carrinho']
        flag_limit_in_stock = False
        if variacao_id: 
            if variacao_id in carrinho:
                # variação existe no carrinho
                quantidade_atual = carrinho[variacao_id]['quantidade']
                quantidade_atual += 1
                if variacao_estoque < quantidade_atual:
                    messages.info (
                        self.request,
                        f'Não temos {quantidade_atual} desse tipo de produto no estoque,'
                        f' foram adicionadas {variacao_estoque} unidades.'
                    )
                    quantidade_atual = variacao_estoque
                    flag_limit_in_stock = True 
                carrinho[variacao_id]['quantidade'] = quantidade_atual
                carrinho[variacao_id]['preco_quantitativo'] = preco_unitario * quantidade_atual
                carrinho[variacao_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * quantidade_atual     
            else:
                # variação não existe no carrinho
                carrinho[variacao_id] = dicionario
        else: 
            if produto_id in carrinho:
                # produto existe no carrinho
                quantidade_atual = carrinho[produto_id]['quantidade']
                quantidade_atual += 1
                if produto_estoque < quantidade_atual:
                    messages.info (
                        self.request,
                        f'Não temos {quantidade_atual} desse produto no estoque,'
                        f' foram adicionadas {produto_estoque} unidades.'
                    )
                    quantidade_atual = variacao_estoque
                    flag_limit_in_stock = True 
                carrinho[produto_id]['quantidade'] = quantidade_atual
                carrinho[produto_id]['preco_quantitativo'] = preco_unitario * quantidade_atual
                carrinho[produto_id]['preco_quantitativo_promocional'] = preco_unitario_promocional * quantidade_atual     
            else:
                # produto não existe no carrinho
                carrinho[produto_id] = dicionario
        
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
