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
            message = f'Não temos {quantidade_atual +1} desse tipo de produto no estoque, já foram adicionadas {quantidade_atual} unidades.'
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
            quantidade_atual = carrinho[produto_id]['quantidade']
            message = f'Não temos {quantidade_atual +1} desse produto no estoque, já foram adicionadas {quantidade_atual} unidades.'
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
            quantidade_atual = 0
            # não existe variação/produto no carrinho
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
        http_referer = self.request.META.get(
            'HTTP_REFERER',
            reverse('produto:lista')
        )
        if not self.request.session.get('carrinho'):
            return redirect(http_referer)
        
        produto_id  = self.request.GET.get('id')
        variacao_id = self.request.GET.get('vid')
        carrinho = self.request.session['carrinho']
        
        if variacao_id != '0':
            if variacao_id not in carrinho:
                return redirect(http_referer)
            
            produto_nome  = carrinho[variacao_id]['produto_nome']
            variacao_nome = carrinho[variacao_id]['variacao_nome']
            message = f'Produto {produto_nome} do tipo {variacao_nome} foi removido do carrinho'
        elif produto_id != '0':
            if produto_id not in carrinho:
                return redirect(http_referer)
            
            produto_nome  = carrinho[produto_id]['produto_nome']
            message = f'Produto {produto_nome} foi removido do carrinho'
        else:        
            return redirect(http_referer)

        messages.success (
            self.request,
            message
        )
        if variacao_id != '0':
            if carrinho[variacao_id]['quantidade'] == 1:
                del self.request.session['carrinho'][variacao_id]
            else:
                carrinho[variacao_id]['quantidade'] -= 1     
        else:
            if carrinho[produto_id]['quantidade'] == 1:
                del self.request.session['carrinho'][produto_id]
            else:
                carrinho[produto_id]['quantidade'] -= 1
        
        self.request.session.save()
        return redirect(http_referer)

class ProductCart(View):
    def get(self, *args, **kargs):
        return render(self.request, 'produto/carrinho.html')

class ProductFinish(View):
    def get(self, *args, **kargs):
        return HttpResponse('finalizar')
