# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

import os, json

file_path  = 'teste.txt'
other_file = 'teste2.txt'

try: 
  file = open(other_file, 'r')
except FileNotFoundError:
  print("Arquivo não existe!")

with open(file_path, 'w') as filename:
  print('Arquivo vai ser fechado')
  filename.close()

with open(file_path, 'w+') as filename:
  filename.write('Linha 1\n')
  filename.write('Linha 2\n')
  filename.writelines(
    ('Linha 3\n', 'Linha 4\n')
  )
  filename.seek(0, 0)
  print(filename.read())
  print('Lendo')
  filename.seek(0, 0)
  print(filename.readline(), end='')
  print(filename.readline().strip())
  print(filename.readline().strip())

  print('READLINES')
  filename.seek(0, 0)
  for row in filename.readlines():
    print(row.strip())
  filename.close()

print('#' * 10)
with open(file_path, 'r') as filename:
  print(filename.read())
  filename.close()

with open(file_path, 'w', encoding='utf8') as filename:
  filename.write('Atenção\n')
  filename.writelines(
    ('Caracteres acentuados\n', 'presentes neste arquivo\n')
  )
  filename.close()

with open(other_file, 'w+', encoding='utf8') as filename:
  filename.write('Atenção\n')
  filename.write('Linha 1\n')
  filename.write('Linha 2\n')
  filename.writelines(
    ('Linha 3\n', 'Linha 4\n')
  )
  print('READLINES')
  filename.seek(0, 0)
  for row in filename.readlines():
    print(row.strip())
  filename.close()

os.rename(other_file, 'pronto.txt')
os.remove('pronto.txt') # ou unlink

# JSON

pessoa = {
  'nome': 'Alexandre Araujo',
  'sobrenome': 'Barbosa',
    'enderecos': [
      {'rua': 'R1', 'numero': 32},
      {'rua': 'R2', 'numero': 55},
    ],
  'altura': 1.8,
  'numeros_preferidos': (2, 4, 6, 8, 10),
  'dev': True,
  'nada': None,
}

with open('teste.json', 'w', encoding='utf8') as arquivo:
  json.dump(
    pessoa,
    arquivo,
    ensure_ascii=False,
    indent=2,
  )

with open('teste.json', 'r', encoding='utf8') as arquivo:
  pessoa = json.load(arquivo)
  print(type(pessoa))
  print(pessoa['nome'])

os.unlink('teste.json')
