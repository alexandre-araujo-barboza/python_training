# POO - pilares:
#    1) Abstração
#    2) Encapsulamento
#    3) Herança
#    4) Polimorfismo    
# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

from functools import partial

class Foo:
  def __init__(self):
    self.public = 'isso é público'
    self._protected = 'isso é protegido'
    self.__private = 'isso é private'

  def metodo_publico(self):
    print(self.__private)
    print(self.__metodo_private())
    print()

    print(self._protected)
    print(self._metodo_protected())
    print()

    print(self.public)
    return 'metodo_publico'

  def _metodo_protected(self):
    return '_metodo_protected'

  def __metodo_private(self):
    return '__metodo_private'

f = Foo()
print(f.metodo_publico() + '\n') # Permitido
print(f'Não usar fora da classe:  {f._metodo_protected()}')   # Não recomendado
print(f'Não usar fora da classe: {f._Foo__metodo_private()}') # Não recomendado mesmo!
