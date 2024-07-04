# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import asdict, astuple, dataclass, field


@dataclass(repr=True)
class Pessoa:
  nome: str
  sobrenome: str
  idade: int = 18
  enderecos: list[str] = field(default_factory=list)

p1 = Pessoa('Maria', 'José')
print(p1)
print(asdict(p1).keys())
print(asdict(p1).values())
print(asdict(p1).items())
print(astuple(p1)[0])

lista = [Pessoa('Carlos', 'Xavier'), Pessoa('Bruno', 'Yolanda'), Pessoa('Alexandre', 'Zumbi')]
ordenadas_nome = sorted(lista, reverse=False, key=lambda p: p.nome)
ordenadas_sobrenome = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
print(ordenadas_nome)
print(ordenadas_sobrenome)
