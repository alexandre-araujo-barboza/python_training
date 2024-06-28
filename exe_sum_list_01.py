# Exercício: Somar os valores de duas listas

list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [2, 4, 6, 8]

list_c = [x + y for x, y in zip(list_a, list_b)]
print(list_c)
