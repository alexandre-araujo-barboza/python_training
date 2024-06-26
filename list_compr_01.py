# Cria lista a partir de uma iteração

lista = []
for numero in range(10):
  lista.append(numero)

lista = [
  numero * 2
  for numero in range(10)
]
print(lista)