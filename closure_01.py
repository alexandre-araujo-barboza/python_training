# Exercício: Adiando execução de funções (usando closureS)

def soma(x, y):
  return x + y

def multiplica(x, y):
  return x * y

def executa(funcao, x):
  def interna(y):
    return funcao(x, y)
  return interna

soma_cinco = executa(soma, 5)
multiplica_dez = executa(multiplica, 10)

print(soma_cinco(10))
print(multiplica_dez(2))
