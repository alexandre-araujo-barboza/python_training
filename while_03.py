# conta letras
phrase = 'O Python é uma linguagem de programação ' \
        'multiparadigma.' \
        ' Python foi criado por Guido Van Rossum.'

i = 0
qtd = 0
char = ''
print(phrase)

while i < len(phrase):
  current_char = phrase[i]
  current_qtd = phrase.count(current_char)
  
  if qtd < current_qtd and current_char is not ' ':
    qtd = current_qtd
    char = current_char
  
  i += 1

print(f'A letra que apareceu mais foi "{char}", no total de ({qtd}) vezes.')
