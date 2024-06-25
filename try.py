# try = Tentar executar
# except = Em caso de erro

num = input('Digite um número: ')

# tratamento da entrada do usuários
print('Número é um digito? ' + str(num.isdigit()))

try:
  num_float = float(num)
  print(f'O dobro de {num} é: {num_float * 2:.2f}')
except:
  print('Isso não é um número!')

# identidade na memória
var = 'A'
print('ID: ' +str(id(var)))