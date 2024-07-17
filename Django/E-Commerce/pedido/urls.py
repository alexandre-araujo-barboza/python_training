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
        'fechar/',
        views.OrderClose.as_view(),
        name='fechar'
    ),
    path(
        'detalhes/',
        views.OrderDetails.as_view(),
        name='detalhes'
    ),
]
