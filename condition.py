# if / elif / else
# se / se não se / se não

condition = input('Digite "entrar" ou "sair" ')

in_condition = condition == 'entrar'
out_condition = condition == 'sair'

if in_condition: # mandatory
  print('Você entrou!')  
elif out_condition: # same repetition
  print('você saiu!')
else:                   # always at end
  print('Opção inválida!')

print("\nend Of Program.")

# São considerados valores FALSY: 0, 0.0, False e ''.
# também existe o tipo None que representa um não valor.
# existem os operadores: and, or e not.

'''
Isso também é comentário!
'''

"""
E isso também!
"""

print(20 * '_') # Repete o caracter _ 20 vezes

# operadores in e not in (está entre e não está entre) para valores iteráveis (ex: string).

nome = 'Araújo';
print("Letra: " + nome[3])  # string como um vetor iterável

exist = 'ú' in nome
not_exist = 'z' not in nome

print('Letra ú está no nome? ' + str(exist))
print('Letra z não está no nome? ' + str(not_exist))

# CONSTANTES COM LETRAS MAIÚSCULAS

velocidade = 70
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

carro_pass_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) \
and local_carro <= LOCAL_1 + RADAR_RANGE

veloc_acima_limite = velocidade > RADAR_1
carro_mult_radar_1 = carro_pass_radar_1 and veloc_acima_limite

if carro_pass_radar_1:
  print('Carro passou no radar 1')

if carro_mult_radar_1:
  print('carro multado em radar 1')

# USO DO None

condicional = False
pass_by_if  = None

if condicional: 
  print("Passou!")
  pass_by_if = True

if (pass_by_if is None):
  print("NÃO passou!")
