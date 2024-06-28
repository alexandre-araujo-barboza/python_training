# Exercícios (com import, lambda, sort, deep copy e list comprehension)

import copy
from package import items

# Aumente os preços dos produtos a seguir em 20%
# Gere novos produtos por deep copy (cópia profunda)

n_items = [
    {**p, 'price': round(p['price'] * 1.2, 2)}
    for p in copy.deepcopy(items)
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos ordenados por nome por deep copy (cópia profunda)

sn_items = sorted(
    copy.deepcopy(items),
    key=lambda p: p['name'],
    reverse=True
)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

sp_items = sorted(
    copy.deepcopy(items),
    key=lambda p: p['price']
)

print()

print("Produtos:")
print(*items, sep='\n')
print()

print("Novos Produtos com + 20%:")
print(*n_items, sep='\n')
print()

print("Produtos ordenados por nome decrescente:")
print(*sn_items, sep='\n')
print()

print("Produtos ordenados por preço crescente:")
print(*sp_items, sep='\n')
print()