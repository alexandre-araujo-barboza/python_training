# Exemplo do uso de try, except, finally e else
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
flag = 1
print('\nControle de erros:\n')

while True:
  try:
    if flag == 1:
      a = 18
      b = 0
      print('Erro: 1')
      c = a / b          # division by zero.
    
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
    
  except ZeroDivisionError as error:
    print('Dividiu por zero.')
    print('Mensagem:', error)
    print('Classe:', error.__class__.__name__)
    
  except NameError as error:
    print('Nome não está definido.')
    print('Mensagem:', error)
    print('Classe:', error.__class__.__name__)
    
  except IndexError as error:
    print('Índice não existente.')
    print('Mensagem:', error)
    print('Classe:', error.__class__.__name__)
    
  except TypeError as error:  
    print('Erro no tipo de dados.')
    print('Mensagem:', error)
    print('Classe:', error.__class__.__name__)
    
  except Exception as error:
    print('ERRO DESCONHECIDO!')
    print('Mensagem:', error)
    print('Classe:', error.__class__.__name__)
  
  else:
    print("NENHUM ERRO!")

  finally:
    print('CONTINUAR:', flag, '\n')
    
    if flag == 4:
      break
    else:
      flag += 1 

print('Todos os erros testados...\nTchau!\n')