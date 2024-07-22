from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path(
        'pagar/<int:pk>',
        views.OrderPayment.as_view(),
        name='pagar'
    ),
    path(
        'detalhe/<int:pk>',
        views.OrderDetails.as_view(),
        name='detalhe'),
    path(
        'listar/',
        views.OrderList.as_view(),
        name='lista'),
    path(
        'salvar/',
        views.OrderSave.as_view(),
        name='salvar'
    ),
]
    
    