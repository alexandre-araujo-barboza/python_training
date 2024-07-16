from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Pedido(models.Model):
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    total  = models.FloatField()
    status = models.CharField(
        default="C",
        max_length=1,
        choices=(
            ('C', 'Criado'),
            ('P', 'Pendente'),
            ('A', 'Aprovado'),
            ('R', 'Reprovado'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return f'Pedido Nro. {self.pk}' 
    
class ItemPedido(models.Model):
    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'

    pedido      = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto    = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    variacao  = models.CharField(max_length=255)
    variacao_id = models.PositiveIntegerField()
    preco        = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    quantidade = models.PositiveIntegerField()
    imagem  = models.CharField(max_length=2000) 

    def __str__(self):
        return f'Detalhes do pedido Nro. {self.order}' 
