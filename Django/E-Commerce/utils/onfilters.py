from django.template import Library

register = Library()

@register.filter
def price_format(val):
    return f'R$ {val:.2f}'.replace('.', ',')
