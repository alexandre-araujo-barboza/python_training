# Cria lista a partir de uma iteração

lista = []
for numero in range(10):
  lista.append(numero)

lista = [
  numero * 2
  for numero in range(10)
]
print(lista)

lista = [
  (x, y, z)
  for x in range(5)
  for y in range(5)
  for z in range(5)
]
print(lista)