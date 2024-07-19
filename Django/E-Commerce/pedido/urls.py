from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path(
        '',
        views.OrderPayment.as_view(),
        name='pagar'
    ),
    path(
        'salvar/',
        views.OrderSave.as_view(),
        name='salvar'
    ),
    path(
        'detalhes/',
        views.OrderDetails.as_view(),
        name='detalhes'
    ),
]
