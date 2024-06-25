# Lista (mutável)
lista = ['Maria', 'Helena', 'Paulo', 'Jorge']
lista.append('Pedro')
lista.append('Joana')

# Indices
indices = range(len(lista))
for indice in indices:
  print(indice, lista[indice], type(lista[indice]))

# Tuplas (imutável)
v1, v2, v3, v4, v5, v6 = lista
print("V1:", v1, "V2:", v2, "V3:", v3, "V4:", v4, "V5:", v5, "V6:", v6)

tupla = tuple(lista)
print("Tupla:", tupla)

lista_b = list(tupla)
print("Lista:", lista_b)

# Resto
v1, v2, *resto = lista
print("V1:", v1, "V2:", v2, "Resto:", resto)

# Itens sem uso
*_, v5 = lista
print("V5:", v5)

_, _, v3, *_ = lista
print("V3:", v3)

# Enumerate (iterável)
lista_enum = enumerate(lista)
print("ENUM address: ", lista_enum, type(lista_enum), "\n")

print("CONSUMIDO!")
for item in lista_enum:
  print(item) # já foi consumido 

print("PERMANENTE!")
for item in enumerate(lista):
  print(item) # permanece

print("Partindo do índice 20")  
lista_c = list(enumerate(lista, start=20))
for item in lista_c:
  print(item)
   
for indice, nome in enumerate(lista_b):
  print(indice, nome)

for tupla_enum in enumerate(lista_b):
  print('TUPLA:')
  for value in tupla_enum:
    print(f'\t{value}')
