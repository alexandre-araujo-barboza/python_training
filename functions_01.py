# exercícios com funções

a = 1000
b = 2000

def func1(): # Teste de escopo
  global a 
  print('Escopo global de a: ', a)
  a = 1100
  print('agora mudou o escopo global de a: ', a)
  try:
    print ('escopo global de b: ', b)
  except UnboundLocalError:
    print('variável b não pode ser acessada no escopo local!')
  b = 2100
  print ('escopo local (em func) de b: ', b)

def func2(x=None, y=None): # Teste de parâmetros opcionais
  if x is not None:
    print('x: ', x)
  if y is not None:
    print('y: ', y)  
  if x is not None or y is not None:
    return 'Um parâmetro pelo menos foi passado'
  return 'Nenhum parâmetro foi passado como argumento da função'

def func3(*args): # Teste de argumentos infinitos
  print(args, type(args))
  lista = list(args) # Converte a tupla para lista
  print(lista, type(lista))
  for value in lista:
    print('valor da lista: ', value)
  return lista
  
def func4(val): # Teste de passagem por referência
  print('variável por referência: ', str(val[0]))
  val[0] = 6

# Função 1
print('O valor inicial de a: ', a)
print('O valor inicial de b: ', b)
func1()
print('O valor final de a: ', a)
print('O valor final de b: ', b)

# Função 2
print(func2())
print(func2(2))
print(func2(2, 4))

# Função 3
print(func3('a','b','c','d','e','f','g','h'))

# Função 4
val = [5]
print('valor = ', val[0])
func4(val)
print('valor agora é = ', val[0])
