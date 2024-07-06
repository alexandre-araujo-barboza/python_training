# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python

from pathlib import Path

from PIL import Image

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'images' / 'original.jpg'
NEW_IMAGE = ROOT_FOLDER / 'images' / ' new.jpg'

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size
# exif = pil_image.info['exif']

new_width = 1024
new_height = round(height * new_width / width)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
  NEW_IMAGE,
  optimize=True,
  quality=70,
  # exif=exif,
)
 
print("Image NEW show...")
new_image.show()
