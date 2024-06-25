# Criar uma lista de compras com possibilidade para Incluir, Apagar e Listar

opcao = ''
lista = []
while opcao != 'S':
  opcao = input('Digite sua opção: [I]nserir, [R]emover, [L]istar, [S]air : ')
  if opcao == '':
    continue
  opcao = opcao.upper()
  if opcao[0] == 'I':
    item = input('Item: ')
    lista.append(item)
  elif opcao[0] == 'R':
    indice = input('indice: ')
    try:
      lista.pop(int(indice))
    except ValueError:
      print(f'índice não numérico [{indice}]!')
    except IndexError:  
      print(f'índice inválido [{indice}]!')  
  elif opcao[0] == 'L':
      for indice, item in enumerate(lista):
        print(f'{indice} = {item}')
  elif opcao[0] == 'S':
    print("tchau!")
  else:
    print(f'Opção inválida [{opcao[0]}]!')