# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

from exe_class_01a import filename, Pessoa, dump

# fazer_dump()

with open(filename, 'r', encoding='utf8') as fp:
  pessoas = json.load(fp)
  p1 = Pessoa(**pessoas[0])
  p2 = Pessoa(**pessoas[1])
  p3 = Pessoa(**pessoas[2])
  p4 = Pessoa(**pessoas[3])
  p5 = Pessoa(**pessoas[4])
  
  print(p1.nome, p1.idade)
  print(p2.nome, p2.idade)
  print(p3.nome, p3.idade)
  print(p4.nome, p4.idade)
  print(p5.nome, p5.idade)

  