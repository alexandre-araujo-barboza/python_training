# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

filename = 'exe_class_01.json'

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 18)
p4 = Pessoa('Paulo', 50)
p5 = Pessoa('Jorge', 28)

bd = [vars(p1), vars(p2), vars(p3), vars(p4), vars(p5),]

def dump():
  with open(filename, 'w', encoding='utf8') as fp:
    print('__DUMP__')
    json.dump(bd, fp, ensure_ascii=False, indent=2)

if __name__ == '__main__':
  print('__main__')
  dump()

