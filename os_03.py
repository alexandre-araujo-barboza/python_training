# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Pasta_1')
NOVA_PASTA = os.path.join(DESKTOP, 'Pasta_2')

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
  for dir_ in dirs:
    caminnho_novo_diretorio = os.path.join(
      root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
    )
    print('Copiando diretório para: ', caminnho_novo_diretorio)
    os.makedirs(caminnho_novo_diretorio, exist_ok=True)
  for file in files:
    caminho_arquivo = os.path.join(root, file)
    caminnho_novo_arquivo = os.path.join(
      root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
    )
    print('Copiando arquivo para: ', caminnho_novo_arquivo)
    shutil.copy(caminho_arquivo, caminnho_novo_arquivo)

print()
print('REMOVE TREE: ', NOVA_PASTA)
shutil.rmtree(NOVA_PASTA, ignore_errors=True)

print('COPY TREE: ', PASTA_ORIGINAL)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

print('MOVE: ', NOVA_PASTA, ' TO: ', NOVA_PASTA + '_EITA' )
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')

print('REMOVE TREE: ', NOVA_PASTA)
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
