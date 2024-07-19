from django.template import Library

register = Library()

@register.filter
def price_format(val):
    return f'R$ {val:.2f}'.replace('.', ',')

@register.filter
def product_sum(carrinho):
    count = 0
    for product in carrinho:
      if product['preco_quantitativo_promocional']:
          count += product['preco_quantitativo_promocional']
      else:
          count += product['preco_quantitativo']
    return count

@register.filter
def quantity_total(carrinho):
    count = 0
    for product in carrinho:
        count += product['quantidade']
    return count    
    