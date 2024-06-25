# Exemplo de Closure

def say_hello(text):
  def hello_person(name):
    return f'{text} {name}'
  return hello_person

morning = say_hello('Good morning')
night = say_hello('Good night')

for name in ['Mary', 'John', 'Peter', 'William', 'Rachel']:
  print(morning(name))
  print(night(name))

# Outro exemplo (em português)

def criar_multiplicador(multiplicador):
  def multiplicar(numero):
    return numero * multiplicador
  return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print('15 x 2 =', duplicar(15))
print('10 x 3 =', triplicar(10))
print('05 x 4 =', quadruplicar(5))
