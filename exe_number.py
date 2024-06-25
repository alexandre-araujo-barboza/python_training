"""
Pedir ao usuário para digitar um número inteiro,
informar se o número é par ou ímpar. Caso não seja
número inteiro, mostrar uma mensagem de erro.
"""

num = input("Digite um número: ")
if not num.isdigit(): 
  print(f'valor {num} não é um número inteiro!')
else:
  value = int(num)
  if value % 2 == 0:
    print(f'valor {value} é um número par!')  
  else: 
    print(f'valor {value} é um número ímpar!')

"""
Perguntar a hora ao usuário e baseado nesse horário
mostrar a saudação: bom dia (0-11), boa tarde 12-17 
e boa noite 18-23
"""

time = input("Digite a hora: ")
try:
  value = int(time)
  if value >= 0 and value <= 11:
    print("Bom dia!")
  elif value >= 12 and value <=17:
    print("Boa tarde")
  else:
    print("Boa noite")
except:
  print(f"valor {time} não é uma hora válida")

"""
Pedir para digitar um nome, se o nome tiver 4 letras
ou menos escrever "nome curto" se tiver entre 4 a 6 letras
escrever "nome normal" se tiver mais de 6 letras, escrever
"nome grande" 
"""

name = input("Digite um nome: ")
if (len(name) <= 4):
  print("Nome curto!")
elif (len(name) > 6):
  print("Nome grande!")
else:
  print("Nome normal!")    