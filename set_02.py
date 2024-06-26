# Exmplode uso do Set
letras = set()
while True:
  letra = input('Digite uma letra: ')
  letras.add(letra)
  print(letras)

  if 's' in letras:
    break

print('EOF')