from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path(
        '',
        views.ProductsList.as_view(),
        name='lista'
    ),
    path(
        '<slug>',
        views.ProductDetails.as_view(),
        name='detalhe'),
    path(
        'adicionaraocarrinho/',
         views.ProductAddToCart.as_view(),
         name='adicionaraocarrinho'
    ),
    path(
        'removerdocarrinho/',
         views.ProductRemoveFromCart.as_view(),
         name='removerdocarrinho'
    ),
    path(
        'carrinho/',
         views.ProductCart.as_view(),
         name='carrinho'
    ),
    path(
        'finalizar/',
         views.ProductFinish.as_view(),
         name='finalizar'
    ),
]
