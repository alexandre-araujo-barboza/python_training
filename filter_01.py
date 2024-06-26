# Mapeamento, filtragem de dados com list comprehension e ordenação com lambda 

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'camiseta', 'preco': 20, },
    {'nome': 'bola', 'preco': 10, },
    {'nome': 'boné', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}   # Mapeia: soma 5% (antes do for) 
    if produto['preco'] > 15 else {**produto}       # Mapeia: aplica soma de 5% se preço maior que 15 (antes do for)
    for produto in produtos
]
novos_produtos.sort(key=lambda item: item['preco']) # Expressão Lambda (ordena por preço)
p(novos_produtos)
print()

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}   # Mapeia: soma 5% (antes do for)
    if produto['preco'] > 15 else {**produto}       # Mapeia: aplica soma de 5% se preço maior que 15 (antes do for)
    for produto in produtos
    if (produto['preco']) > 15                      # Filtra: preço maior que 15 (depois do for)
]
novos_produtos.sort(key=lambda item: item['preco']) # Expressão Lambda (ordena por preço)
p(novos_produtos)
print()