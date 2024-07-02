# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

# Pascal case ex: PessoaFisica, PessoaJuridica (Nome da Class)
# Camel case ex: pessoaFisica, pessoaJuridica (instância do objeto)
# Snake case ex: pessoa_fisica, pessoa juridica (variáveis locais)

class Pessoa:
  def __init__(self, nome=None, sobrenome=None):
    self.nome = nome
    self.sobrenome = sobrenome

p1 = Pessoa()
p1.nome = 'Alexandre'
p1.sobrenome = 'Araujo'

p2 = Pessoa()
p2.nome = 'Maria'
p2.sobrenome = 'Joana'

p3 = Pessoa('Jorge', 'Amado')

print('P1 Nome: ' + p1.nome)
print('P1 Sobrenome: ' + p1.sobrenome)

print('P2 Nome: ' + p2.nome)
print('P2 Sobrenome: ' + p2.sobrenome)

print('P3 Nome: '+ p3.nome)
print('P3 Sobrenome: ' + p3.sobrenome)

print('P1: ' + str(p1))
print('P2: ' + str(p2))
print('P3: ' + str(p2))

print('P1 is Instance of Pessoa? ' + str(isinstance(p1, Pessoa)))
print('P2 is Instance of Pessoa? ' + str(isinstance(p2, Pessoa)))
print('P3 is Instance of Pessoa? ' + str(isinstance(p3, Pessoa)))

# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código (um parãmetro fixo dentro da classe)

class Carro:
  marca = None
  cor = None

  def __init__(self, nome):
    self.nome = nome

  def acelerar(self):
    print(f'{self.nome} está acelerando...')
  
  def frear(self):
    print(f'{self.nome} está freiando...')
    
fusca = Carro('Fusca')
print(fusca.nome)
fusca.marca = "Volkswagen"
fusca.cor = "Amarelo"
print('fusca é: ' + fusca.marca + ' sua cor é: ' + fusca.cor)
fusca.acelerar()
fusca.frear()

celta = Carro(nome='Celta')
print(celta.nome)
celta.marca = "Ford"
celta.cor = "Preto"
print('celta é: ' + celta.marca + ' sua cor é: ' + celta.cor)
celta.acelerar()
celta.frear()