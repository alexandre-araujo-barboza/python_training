# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (self, cls)

class Connection:
  def __init__(self, host='localhost'):
    self.host = host
    self.user = None
    self.password = None

  def set_user(self, user):
    self.user = user

  def set_password(self, password):
    self.password = password

  @classmethod
  def create_with_auth(cls, user, password):
    connection = cls()
    connection.user = user
    connection.password = password
    return connection

  @staticmethod
  def log(msg):
    print('LOG:', msg)


def connection_log(msg):
  print('LOG:', msg)


c1 = Connection.create_with_auth('Jorge', '1234')
print(Connection.log('Essa é a mensagem de log'))
print(f'username:{c1.user}')
print(f'password:{c1.password}')

# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
  def __init__(self, cor):
    self.cor_tinta = cor

  @property
  def cor(self):
    return self.cor_tinta

  @property
  def cor_tampa(self):
    return 'transparente'

caneta = Caneta('azul')
print('Caneta Cor:', caneta.cor)
print('Caneta Tampa:', caneta.cor_tampa)

# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Lapis:
  def __init__(self, cor):
    
    self.cor = cor

    # private protected
    self._fabricante = None
    self._tipo = None

  @property
  def fabricante(self):
    return self._fabricante
  
  @property
  def tipo(self):
    return self._tipo

  @fabricante.setter
  def fabricante(self, fabricante):
    self._fabricante = fabricante
  
  @tipo.setter
  def tipo(self, tipo):
    self._tipo = tipo
    print(self.tipo)

lapis = Lapis('preto')
lapis.fabricante = 'Faber Castel'
lapis.tipo = 2

print('Lapis fabricante:', lapis.fabricante)
print('Lapis tipo:', lapis.tipo)
