# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
  ano = 2023  # atributo de classe

  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  @classmethod
  def metodo_de_classe(cls):
    print('Hey')

  @classmethod
  def criar_com_50_anos(cls, nome):
    return cls(nome, 50)

  @classmethod
  def criar_sem_nome(cls, idade):
    return cls('Anônima', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)

# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Classe:
  @staticmethod
  def funcao_que_esta_na_classe(*args, **kwargs):
    print('Oi', args, kwargs)

  def funcao(*args, **kwargs):
    print('Oi', args, kwargs)

c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)
c1.funcao(1, 2, 3)

Classe.funcao_que_esta_na_classe(nomeado=1)
c1.funcao(nomeado=1)
