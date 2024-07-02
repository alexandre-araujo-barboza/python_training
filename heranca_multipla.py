# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar (Problema do diamante)
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)

class A:
  ...
  def quem_sou(self):
    print('CLASS A')
  
  def eu_sou_A(self):  
    print('Sou A')

class B(A):
  ...
  def quem_sou(self):
    print('CLASS B')
  
  def eu_sou_B(self):  
    print('Sou B')

class C(A):
  ...
  def quem_sou(self):
    print(' CLASS C')

  def eu_sou_C(self):  
    print('Sou C')

class D(B, C):
  ...
  def quem_sou(self):
    print('CLASS D')
  
  def eu_sou_D(self):  
    print('Sou D')

d = D()
d.quem_sou()
print(D.mro())

d.eu_sou_A() # Não dá erro!