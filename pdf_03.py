# MERGER

import os
from pathlib import Path
from PyPDF2 import PdfMerger

ROOT_FOLDER = Path(__file__).parent
TARGET_FOLDER = ROOT_FOLDER / 'pdf_target'

files = [
    TARGET_FOLDER / 'page1.pdf',
    TARGET_FOLDER / 'page2.pdf',
]

merger = PdfMerger()
for file in files:
  merger.append(file)  # type: ignore

merger.write(TARGET_FOLDER / 'merged.pdf')  # type: ignore
merger.close()

arr = next(os.walk(TARGET_FOLDER))[2]
print(arr) 
