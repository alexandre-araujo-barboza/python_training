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

# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class Escritor:
  def __init__(self, nome) -> None:
    self.nome = nome
    self._ferramenta = None

  @property
  def ferramenta(self):
    return self._ferramenta

  @ferramenta.setter
  def ferramenta(self, ferramenta):
    self._ferramenta = ferramenta

class FerramentaDeEscrever:
  def __init__(self, nome):
    self.nome = nome

  def escrever(self):
    return f'{self.nome} está escrevendo'

escritor = Escritor('Alexandre')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')

print()
escritor.ferramenta = maquina_de_escrever
print(maquina_de_escrever.escrever())
print(f'Escritor ({escritor.nome}) usando: ({escritor.ferramenta.escrever()})')

print()
escritor.ferramenta = caneta
print(caneta.escrever())
print(f'Escritor ({escritor.nome}) usando: ({escritor.ferramenta.escrever()})')
