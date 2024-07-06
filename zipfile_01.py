# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'ZIP' / 'example' 
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'ZIP' / 'example.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'ZIP' / 'example' / 'unzipped'
CAMINHO_ORIGEM = CAMINHO_RAIZ / 'ZIP' / 'example' / 'source'

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)
CAMINHO_ORIGEM.mkdir(exist_ok=True)


def criar_arquivos(qtd: int, zip_dir: Path):
  for i in range(qtd):
    texto = 'arquivo_%s' % (i+1)
    with open(zip_dir / f'{texto}.txt', 'w', encoding='utf-8') as arquivo:
      arquivo.write(texto)

criar_arquivos(10, CAMINHO_ORIGEM)

# Criando um zip e adicionando arquivos
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
  for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
    for file in files:
      zip.write(os.path.join(root, file), file)

# Lendo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
  for arquivo in zip.namelist():
    print(arquivo)

# Extraindo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
  zip.extractall(CAMINHO_DESCOMPACTADO)
