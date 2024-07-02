# Escopo da classe e de métodos da classe
class Animal:
  def __init__(self, nome):
    self.nome = nome
    
  def comendo(self, alimento):
        return f'{self.nome} está comando {alimento}'

  def comida(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal('Girafa')
print(leao.nome)
print(leao.comida('maçã'))

# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return

        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return

        print(f'{self.nome} está fotografando...')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print()

c2.parar_filmar()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()

# Atributos de classe
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print('Ano Atual: ' + str(Pessoa.ano_atual))
print('Ano nascimento ' + p1.nome + ': ' + str(p1.get_ano_nascimento()))
print('Ano nascimento ' + p2.nome + ': ' + str(p2.get_ano_nascimento()))

# __dict__ e vars para atributos de instância

p1.__dict__['atributo'] = 'novo'
del p1.__dict__['nome']
print(p1.__dict__)
print(vars(p1))

# desempacotando um dicionário para a classe

dados = {'idade' : 54, 'nome' : 'Jorge'}
p3 = Pessoa(**dados)
print(p3.nome)
print(p3.idade)
