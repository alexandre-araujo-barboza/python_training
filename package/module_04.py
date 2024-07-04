
# Recomendado usar aspas duplas

"""
ISSO É UM DOCSTRIG DE VÁRIAS LINHAS
Obs.:
    Documentação do módulo
    O que esse módulo vai fazer?
"""

variavel_1 = 'teste'
def function():
  return 'teste'

def soma(x: int | float, y: int | float) -> int | float:
  """Soma x e y
  Este módulo contém funções e exemplos de documentação de funções.
  A função soma você já conhece bastante.
  :param x: Número 1
  :type x: int or float
  :param y: Número 2
  :type y: int or float
  :return: A soma entre x e y
  :rtype: int or float
  """
  return x + y


def multiplica(
  x: int | float,
  y: int | float,
  z: int | float | None = None
) -> int | float:
  """Multiplica x, y e/ou z
  Multiplica x e y. Se z for enviado, multiplica x, y, z.
  """
  if z is None:
    return x * y
  return x * y * z

variavel_2 = 2
variavel_3 = 3
variavel_4 = 4

