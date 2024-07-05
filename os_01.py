# O módulo os para interação com o sistema
# Doc: https://docs.python.org/3/library/os.html
# O módulo `os` fornece funções para interagir com o sistema operacional.
# Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de
# arquivos e a função os.listdir() pode ser usada para listar os arquivos em um
# diretório. O método os.system() permite executar comandos do sistema
# operacional a partir do seu código Python.
# Windows 11 (PowerShell), Linux, Mac = clear
# Windows (antigo, cmd) = cls
# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('/Users', 'alexandre', 'Desktop', 'exemplo')
counter = count()

for root, dirs, files in os.walk(caminho):
  the_counter = next(counter)
  print(the_counter, 'Pasta atual', root)

  for dir_ in dirs:
    print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
      caminho_completo_arquivo = os.path.join(root, file_)
      print('  ', the_counter, 'FILE:', caminho_completo_arquivo)
      # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
      # os.unlink(caminho_completo_arquivo)

print('#' * 80)

for pasta in os.listdir(caminho):
  caminho_completo_pasta = os.path.join(caminho, pasta)
  print(pasta)
  if not os.path.isdir(caminho_completo_pasta):
    continue
  for imagem in os.listdir(caminho_completo_pasta):
    print('  ', imagem)

print('#' * 80)

os.system('echo "Hello world"')
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)
diretorio, arquivo = os.path.split(caminho)
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print('Nome e extensão: ', nome_arquivo, extensao_arquivo)
print('Existe? ', os.path.exists('/Users/luizotavio/Desktop/curso-python-rep'))
print('Absulute Path', os.path.abspath('.'))
print('Caminho: ', caminho)
print('Basename caminho: ', os.path.basename(caminho))
print('Basename diretorio: ', os.path.basename(diretorio))
print('Dirname: ', os.path.dirname(caminho))




