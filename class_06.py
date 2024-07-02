# super() e a sobreposição de membros - Python Orientado a Objetos

class A(object):
  atributo_a = 'valor a'

  def __init__(self, param1, param2):
    self.atributo1 = param1
    self.atributo2 = param2

  def metodo(self):
    print('CLASS A')

class B(A):
  atributo_b = 'valor b'

  def __init__(self, param1, param2):
    super().__init__(param1, param2)
    self.param1 = param1
    self.param2 = param2
  
  def metodo(self):
    print('CLASS B')

class C(B):
  atributo_c = 'valor c'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def metodo(self):
    super(B, self).metodo()  # CLASS A
    super().metodo()         # CLASS B
    print('CLASS C')

print(A.mro())
print(B.mro())
print(C.mro())

c = C('Atributo 1', 'Atributo 2')
c.metodo()

print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)

print(c.atributo1)
print(c.atributo2)
