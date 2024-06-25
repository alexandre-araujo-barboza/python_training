# Exercício QUIZ

perguntas = [
  {
    'Pergunta': 'Quanto é 2 + 2',
    'Opções': ['1', '3', '4', '5'],
    'Resposta': '4',
  },
  {
    'Pergunta': 'Quanto é 5 * 5?',
    'Opções': ['25', '55', '10', '51'],
    'Resposta': '25',
  },
  {
    'Pergunta': 'Quanto é 10 / 2?',
    'Opções': ['4', '5', '2', '1'],
    'Resposta': '5',
  },
]

qtd_acertos = 0
for pergunta in perguntas:
  print('\nPergunta:', pergunta['Pergunta'], '\n')
  
  opcoes = pergunta['Opções']
  for i, opcao in enumerate(pergunta['Opções']):
    print(f'{i})', opcao)

  escolha = input('Escolha uma opção: ')
  valor = None
  acerto = False
  qtd_opcoes = len(opcoes)

  if escolha.isdigit():
    valor = int(escolha)
  
  if valor is not None:
    if valor >= 0 and valor < qtd_opcoes:
      if opcoes[valor] == pergunta['Resposta']:
        acerto = True

  if acerto:
    print('Acertou!')
    qtd_acertos += 1
  else:
    print('Errou!')

print('\nVocê acertou', qtd_acertos, 'de', len(perguntas), 'perguntas.')