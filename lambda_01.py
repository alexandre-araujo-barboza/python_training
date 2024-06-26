# Expressão lambda são funções anônima de uma linha

lista1 = [
  {'nome': 'Luiz', 'sobrenome': 'Miranda'},
  {'nome': 'Maria', 'sobrenome': 'Oliveira'},
  {'nome': 'Daniel', 'sobrenome': 'Silva'},
  {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
  {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena_nome(item):
  return item['nome']

def ordena_sobrenome(item):
  return item['sobrenome']

lista1.sort(key=ordena_nome) # Altera a própria lista
lista2 = sorted(lista1, key=ordena_sobrenome) # Cria uma lista nova (cópia rasa)

print('\nOrdenado por nome a própria lista:')
for x in lista1:
  print(x)

print('\nOrdenado por sobrenome em uma nova lista:')
for y in lista2:
  print(y)

lista2.sort(key=lambda item: item['nome']) # Expressão Lambda (na própria lista)
lista3 = sorted(lista2, key=lambda item: item['sobrenome']) # Expressão Lambda (em uma lista nova [rasa])

print('\nSegunda lista agora ordenada por nome:')
for z in lista2:
  print(z)

print('\nTerceira lista ordenada por sobrenome:')
for k in lista3:
  print(k)

print('\n')