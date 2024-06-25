# Cópia rasa (shallow) -> copia só valores imutáveis (str, integer, boolean, float e tuple)
# Cópia profunda (deep copy) -> copia valores mutáveis (list e dict) IMPORTANTE: ALGORITMO EXPONENCIAL (BIG-O)
import copy # Shallow Copy = (copy) | Deep Copy = (deepcopy)

origem = {
  'item_1' : 'normal', # imutável
  'item_2' : 'testando', # imutável
  'lista_1' : [0, 1, 2, 3, 4 ,5] # mutável 

}

print('ORIGEM:', origem)
print("Dicionário inicial\n")

destino = origem # mesmo endereço de memória
destino['item_2'] = "alterado"

print('ORIGEM:', origem) # origem foi alterado!
print('DESTINO:', destino)
print('Dicionários alterados (no mesmo endereço de memória)\n')

copia = destino.copy() # cópia rasa (não copia os niveis de atributos mutáveis)
copia['item_2'] = 'testado'
copia['lista_1'][5] = 9999 # origem e destino da lista não são alcançados pela cópia

print('ORIGEM:', origem)
print('DESTINO:', destino)
print('CÓPIA:', copia) 
print('Cópia rasa do dicionário (mesmo endereço para dados mutáveis, ex: lista\n')

copia_profunda = copy.deepcopy(copia)
copia_profunda['item_1'] = "cópia profunda"
copia_profunda['item_2'] = "alterado de novo"
copia_profunda["lista_1"][5] = -1

print('ORIGEM:', origem)
print('DESTINO:', destino)
print('CÓPIA:', copia) 
print('CÓPIA PROFUNDA:', copia_profunda) 
print('Cópia profunda do dicionário e da lista em outro endereço de memória\n')
