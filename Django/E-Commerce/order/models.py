from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Order(models.Model):
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    user   = models.ForeignKey(User, on_delete=models.CASCADE)
    total  = models.FloatField()
    status = models.CharField(
        default="C",
        max_length=1,
        choices=(
            ('C', 'Created'),
            ('A', 'Approved'),
            ('D', 'Disapproved'),
            ('P', 'Pending'),
            ('S', 'Sent'),
            ('F', 'Finished'),
        )
    )

    def __str__(self):
        out = _("Order")
        return f'{out} N. {self.pk}' 

class ItemOrder(models.Model):
    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'

    order      = models.ForeignKey(Order, on_delete=models.CASCADE)
    product    = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variation  = models.CharField(max_length=255)
    variation_id = models.PositiveIntegerField()
    price        = models.FloatField()
    price_promotional = models.FloatField(default=0)
    amount = models.PositiveIntegerField()
    image  = models.CharField(max_length=2000) 

    def __str__(self):
        out = _("of Order")
        return f'Item {out} N. {self.order}' 
