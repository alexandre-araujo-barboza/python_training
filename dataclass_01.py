# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import asdict, astuple, dataclass


@dataclass(repr=True)
class Pessoa:
  nome: str
  sobrenome: str

lista = [Pessoa('Carlos', 'Xavier'), Pessoa('Bruno', 'Yolanda'), Pessoa('Alexandre', 'Zumbi')]
ordenadas_nome = sorted(lista, reverse=False, key=lambda p: p.nome)
ordenadas_sobrenome = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
print(ordenadas_nome)
print(ordenadas_sobrenome)
p1 = Pessoa('Maria', 'José')
print(asdict(p1).keys())
print(asdict(p1).values())
print(asdict(p1).items())
print(astuple(p1)[0])