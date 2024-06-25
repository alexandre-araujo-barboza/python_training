# Calculadora com While
# Python aceita ELSE no while
# Loop com controles internos

while True:
  num_1 = input('Digite um número: ')
  num_2 = input('Digite outro número: ')
  operator = input('Digite o operador (+-*/): ')

  valid_number = None
  num_1_float = 0.0
  num_2_float = 0.0
    
  try:
    num_1_float = float(num_1)
    num_2_float = float(num_2)
    valid_number = True
  except:
    valid_number = None
  
  if (valid_number is None):
    print('Número inválido!')
    continue

  valid_operator = '+-*/'
  if (operator not in valid_operator):
    print('Operador inválido!')
    continue

  if (len(operator) > 1):
    print('Use apenas um operador!')
    continue
  
  result = 0.0
  if (operator == '+'):
    result = num_1_float + num_2_float
  elif (operator == '-'):
    result = num_1_float - num_2_float
  elif (operator == '*'):
    result = num_1_float * num_2_float
  elif (operator == '/'):
    
    try:
      result = num_1_float / num_2_float
    except:
      print('Divisão por zero!')
      result = 'ERRO'
        
  else:
    print('Erro não previsto!')
    break

  print('Resultado: ', result)

  cancel = input('Quer sair? [s]im: ').lower().startswith('s')
  if cancel is True:
    break
  