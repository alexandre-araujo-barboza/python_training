# Exercíco 1 (String):

# digitar seu nome
# digitar sua idade
# se idade e nome forem preenchidos
# mostrar
  # Nome
  # Idade
  # seu nome invertido 
  # nome contém espaços ou não
  # nome tem quantas letras
  # a primeira letra do nome
  # a última letra do nome
# se nome e idade não preenchidos
  # mostrar
  # Desculpa, campos não preenchidos
      
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if (nome and idade):
  print(f'O seu nome é {nome} e a sua idade é {idade}')
  print('O seu nome invertido é: ' + nome[::-1])
  espacos = ' ' in nome
  if (espacos):
    print('O seu nome contém espaços')
  else:
    print('O seu nome não contém espaços')
  tamanho = len(nome)  
  print('O seu nome tem ' + str(tamanho) + " letras")
  primeira = nome[0]
  ultima   = nome[-1]
  print('A primeira letra do seu nome é: ' + primeira)
  print('A última letra do seu nome é: ' + ultima)
else:
  print('Desculpa, campos obrigatórios não preenchidos!')
