# PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

# READER

from pathlib import Path
from PyPDF2 import PdfReader

ROOT_FOLDER = Path(__file__).parent
SOURCE_FOLDER = ROOT_FOLDER / 'pdf_source'
TARGET_FOLDER = ROOT_FOLDER / 'pdf_target'
PDF_FILE = SOURCE_FOLDER / 'R20230210.pdf'

SOURCE_FOLDER.mkdir(exist_ok=True)

reader = PdfReader(PDF_FILE)

page = reader.pages[0]
imagem = page.images[0]

print(page.extract_text())
print('Imagem Name =', imagem.name)
