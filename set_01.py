'''
Sets são iteráveis e mutáveis
São eficientes para remover valores duplicados
Seus valores são sempre únicos
Não aceitam valores mutáveis
Não tem índices
Não garantem ordem
'''
lista_1 = [1, 2, 3, 3, 3, 3, 3, 1]
print(lista_1)

set_1 = set(lista_1)
print(set_1) # valores duplicados foram removidos da lista

lista_2 = list(set_1)
print(lista_2)

set_2 = set('Alexandre')
print(set_2) # não garantem ordem

set_3 = {1, 2, 3, (123,)} # Aceita tuplas (mutável)
print(set_3)

print(3 not in set_3)

set_4 = set()
set_4.add('Alexandre') # Adiciona valor
set_4.add(100)
set_4.update(('Olá mundo', 100, 200, 4.1, False)) # Atualiza valor
print(set_4)

set_4.discard('Olá mundo') # Remove valor
print(set_4)

set_4.clear()
print(set_4)

'''
Operadores:
união = |
interesessão = &
diferença = - (só existe no set da esquerda)
diferença simétrica = ^ (não existem em ambos, fora da intersessão)
'''
s5 = {1, 2, 3}
s6 = {2, 3, 4}
s7 = s5 | s6
s8 = s5 & s6
s9 = s5 - s6
s10 = s5 ^ s6 
print(s7)  # união
print(s8)  # intersessão
print(s9)  # diferença
print(s10) # dif. simétrica
