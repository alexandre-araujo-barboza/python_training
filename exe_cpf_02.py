# Gerador de CPF em Python

import random
import sys

def set_digit(digit, cpf):
  multi = 9 + digit
  result = 0
  slice = cpf
  for piece in slice:
    result += int(piece) * multi
    multi -= 1
  ret = (result * 10) % 11
  ret = ret if ret <= 9 else 0
  return ret

x = input('Quantos CPFs você quer gerar? ')
try:
  x = int(x)
except ValueError:
  print("Erro: Valor não é número inteiro!")
  sys.exit()  

count = 0  
for _ in range(x):
  count += 1
  cpf = ''
  for i in range(9):
    cpf += str(random.randint(0,9))
    
  piece_1 = cpf[:9]
  slice_1 = set_digit(1, piece_1) # cálculo do primeiro dígito verificador
  
  piece_2 = piece_1 + str(slice_1)
  slice_2 = set_digit(2, piece_2) # cálculo do segundo dígito verificador
  
  confirm = f'{piece_1}{slice_1}{slice_2}' # criação do CPF
  confirm = f'{confirm[0:3]}.{confirm[3:6]}.{confirm[6:9]}-{confirm[9:11]}'
  print(f'({count})\t= {confirm}')
