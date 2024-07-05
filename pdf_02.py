# WRITER

import os
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter 

ROOT_FOLDER = Path(__file__).parent
SOURCE_FOLDER = ROOT_FOLDER / 'pdf_source'
TARGET_FOLDER = ROOT_FOLDER / 'pdf_target'
PDF_FILE = SOURCE_FOLDER / 'R20230210.pdf'

reader = PdfReader(PDF_FILE)
  
for i, page in enumerate(reader.pages):

  writer = PdfWriter()

  with open(TARGET_FOLDER / f'page{i+1}.pdf', 'wb') as arquivo:
    writer.add_page(page)
    writer.write(arquivo) # type: ignore

arr = next(os.walk(TARGET_FOLDER))[2]
print(arr) 
