# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
# groupby - agrupando valores (itertools)

from itertools import combinations, permutations, product, groupby 


def print_iter(iterator):
  print(*list(iterator), sep='\n')
  print()


pessoas = [
  'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
  ['preta', 'branca'],
  ['p', 'm', 'g'],
  ['masculino', 'feminino', 'unisex'],
  ['algodão', 'poliéster']
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))

alunos = [
  {'nome': 'Luiz', 'nota': 'A'},
  {'nome': 'Letícia', 'nota': 'B'},
  {'nome': 'Fabrício', 'nota': 'A'},
  {'nome': 'Rosemary', 'nota': 'C'},
  {'nome': 'Joana', 'nota': 'D'},
  {'nome': 'João', 'nota': 'A'},
  {'nome': 'Eduardo', 'nota': 'B'},
  {'nome': 'André', 'nota': 'A'},
  {'nome': 'Anderson', 'nota': 'C'},
]

def order_by(aluno):
  return aluno['nota']

alunos_agrupados = sorted(alunos, key=order_by)
grupos = groupby(alunos_agrupados, key=order_by)

for key, group in grupos:
  print(key)
  for aluno in group:
    print(aluno)
