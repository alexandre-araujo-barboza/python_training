from django.shortcuts import redirect, reverse, render
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib import messages
from produto.models import Variacao, Produto
from .models import Pedido, ItemPedido
from utils.onfilters import quantity_total, product_sum 

class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:criar')

        return super().dispatch(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs
    
class OrderPayment(DispatchLoginRequiredMixin, DetailView):
    template_name = 'pedido/pagamento.html'
    model = Pedido
    pk_url_kwarg = 'pk'
    context_object_name = 'pedido'

class OrderSave(View):
    template_name = 'pedido/pagamento.html'
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.info(
                self.request,
                'Você precisa fazer login.'
            )
            return redirect('perfil:criar')

        if not self.request.session.get('carrinho'):
            messages.info(
                self.request,
                'Seu carrinho está vazio.'
            )
            return redirect('produto:lista')

        carrinho = self.request.session.get('carrinho')
        quantidade = 0
        total = 0
        for item in carrinho:
            it_ch = item[0]
            it_id = int(item[1:])
                    
            if it_ch == 'v':
                bd_work = Variacao.objects.select_related('produto').filter(id=it_id)
            elif it_ch == 's':
                bd_work = Produto.objects.filter(id=it_id)
            else:
                raise Exception('índice inválido no carrinho')
             
            for piece in bd_work:
                pid = it_ch + str(piece.id)
                estoque = piece.estoque
                qtd_carrinho = carrinho[pid]['quantidade']
                preco_unt = carrinho[pid]['preco_unitario']
                preco_unt_promo = carrinho[pid]['preco_unitario_promocional']
                quantidade += qtd_carrinho
                if preco_unt_promo:
                    total += preco_unt_promo
                else:
                    total += preco_unt    
                error_msg_estoque = ''
                if estoque < qtd_carrinho:
                    carrinho[pid]['quantidade'] = estoque
                    carrinho[pid]['preco_quantitativo'] = estoque * preco_unt
                    carrinho[pid]['preco_quantitativo_promocional'] = estoque * \
                        preco_unt_promo
                    error_msg_estoque = 'Estoque insuficiente para alguns '\
                        'produtos do seu carrinho. '\
                        'Por favor, verifique quais produtos foram afetados.'
                if error_msg_estoque:
                    messages.warning(
                        self.request,
                        error_msg_estoque
                    )
                    self.request.session.save()
                    return redirect('produto:carrinho')
        
        qtd_total_carrinho   = quantidade
        valor_total_carrinho = total
        pedido = Pedido(
            user = self.request.user,
            total = valor_total_carrinho,
            quantidade = qtd_total_carrinho,
            status = 'C',
        )
        pedido.save()
       
        for v in carrinho.values():
            if not v['produto_id']:
                vid = v['variacao_id'][1:]
                pid = 0
            else: 
                pid = v['produto_id'][1:]
                vid = 0
            ItemPedido.objects.bulk_create(
                [
                    ItemPedido(
                        pedido=pedido,
                        produto=v['produto_nome'],
                        produto_id= pid,
                        variacao=v['variacao_nome'],
                        variacao_id=vid,
                        preco=v['preco_quantitativo'],
                        preco_promocional=v['preco_quantitativo_promocional'],
                        quantidade=v['quantidade'],
                        imagem=v['imagem'],
                    ) 
                ]
            )
            
        del self.request.session['carrinho']
        return redirect(
            reverse(
                'pedido:pagar',
                kwargs={
                    'pk': pedido.pk
                }
            )
        )
class OrderDetails(View):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'pedido/detalhe.html'
    pk_url_kwarg = 'pk'

class OrderList(DispatchLoginRequiredMixin, ListView):
    model = Pedido
    context_object_name = 'pedidos'
    template_name = 'pedido/listar.html'
    paginate_by = 10
    ordering = ['-id']
