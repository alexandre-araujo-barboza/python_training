# map, partial, GeneratorType e esgotamento de Iterators
# map - para mapear dados
# filter é um filtro funcional
# reduce - faz a redução de um iterável em um valor

from functools import partial, reduce
from types import GeneratorType

def print_iter(iterator):
  print(*list(iterator), sep='\n')
  print()

produtos = [
  {'nome': 'Produto 5', 'preco': 10.00},
  {'nome': 'Produto 1', 'preco': 22.32},
  {'nome': 'Produto 3', 'preco': 10.11},
  {'nome': 'Produto 2', 'preco': 105.87},
  {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
  return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(
  aumentar_porcentagem,
  porcentagem = 1.1
)

def muda_preco_de_produtos(produto):
  return {
    **produto,
    'preco': aumentar_dez_porcento(
      produto['preco']
    )
  }

novos_produtos = list(map(
  muda_preco_de_produtos,
  produtos
))

print_iter(produtos)
print_iter(novos_produtos)

print(
  list(map(
    lambda x: x * 3,
    [1, 2, 3, 4]
  ))
)

def print_iter(iterator):
  print(*list(iterator), sep='\n')
  print()

def filtrar_preco(produto):
  return produto['preco'] > 100

novos_produtos = filter(
  filtrar_preco,
  produtos
)

print_iter(produtos)
print_iter(novos_produtos)

total = reduce(
  lambda ac, p: ac + p['preco'],
  produtos,
  0
)

print('Total é', round(total, 2))
