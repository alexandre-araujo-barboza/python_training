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

# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Carrinho:
  def __init__(self):
    self._produtos = []

  def total(self):
    return sum([p.preco for p in self._produtos])

  def inserir_produtos(self, *produtos):
    for produto in produtos:
      self._produtos.append(produto)

  def listar_produtos(self):
    for produto in self._produtos:
      print(f'Produto: {produto.nome}\t| Preço: {produto.preco}')
    
class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

print()
carrinho = Carrinho()
p1, p2, p3 = Produto('Caneta', 1.20), Produto('Lápis', 0.80), Produto('Régua', 0.40)
carrinho.inserir_produtos(p1, p2, p3)
carrinho.listar_produtos()
print('Total:', carrinho.total())

# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
  def __init__(self, nome):
    self.nome = nome
    self.enderecos = []

  def inserir_endereco(self, rua, numero):
    self.enderecos.append(Endereco(rua, numero))

  def inserir_endereco_externo(self, endereco):
    self.enderecos.append(endereco)

  def listar_enderecos(self):
    for endereco in self.enderecos:
      print(f'Rua: {endereco.rua}, Número: {endereco.numero}')

  def __del__(self):
    print(f'Apagando Nome: {self.nome}')

class Endereco:
    def __init__(self, rua, numero):
      self.rua = rua
      self.numero = numero

    def __del__(self):
      print(f'Apagando Rua: {self.rua}, Número: {self.numero}')

print()

cliente = Cliente('Maria Amélia')
cliente.inserir_endereco('Major Rolinda da Silva', 54)
cliente.inserir_endereco('Buenos Aires', 6745)
endereco_externo = Endereco('Fonte da Saudade', 123213)

cliente.inserir_endereco_externo(endereco_externo)
cliente.listar_enderecos()

del cliente

print(f'Rua: {endereco_externo.rua}, Número: {endereco_externo.numero}')
print('Garbage collector apagando...')
