flag = 1
print('\nControle de erros:\n')

while True:
  try:
    if flag == 1:
      a = 18
      b = 0
      print('Erro: 1')
      c = a / b          # division by zero
    
    elif flag == 2:
      print('Erro: 2')
      e = b + d          # name 'd' is not defined.
    
    elif flag == 3:
      print('Erro: 3')
      empty = []
      x = empty[1000]    # list index out of range.

    elif flag == 4:
      print('Erro: 4')
      x = 'string'
      y = 1
      x + y              # can only concatenate str (not "int") to str.
    
  except ZeroDivisionError:
    print('Dividiu por zero.')
    
  except NameError:
    print('Nome não está definido.')
    
  except IndexError:
    print('Índice não existente.')

  except TypeError:  
    print('Erro no tipo de dados.')
    
  except Exception:
    print('ERRO DESCONHECIDO.')

  finally:
    print('CONTINUAR:', flag, '\n')
    
    if flag == 4:
      break
    else:
      flag += 1 

print('Todos os erros testados...\nTchau!\n')