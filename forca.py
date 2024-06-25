# Jogo da Forca

import os
os.system('cls')

while True:
  secret = input('Digite a palavra secreta ou "quit" para sair: ')
  char_found = ''
  count = 0
  if (secret.lower() == 'quit'):
    break
  
  while len(secret) > 4 and ' ' not in secret:
    char = input ('digite uma letra: ')
    count += 1

    if len(char) == 0 or len(char) > 1 or char is ' ':
      print('Letra inválida ou mais de uma letra!')
      continue

    if char in secret:
      char_found += char
    else:
      print(f'Tentativa: {count}. Letra: {char} não encontrada!')
    
    word = ''
    for secret_char in secret:
      if (secret_char in char_found):
        word += secret_char
      else:
        word += "*" 
    print('Palavra secreta: ', word)
    if word == secret:
      print('Parabéns, você ganhou!')
      print('A palavra era: ', secret)
      print('Total de tentativas: ', count)
      break

  else:  
    print('Palavra muito curta ou possui espaços!')
