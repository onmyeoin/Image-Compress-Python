# convert JPG's to PNG's and compresses by running script with directory
# containing JPGs and 1st arg and new directory as 2nd arg

import sys
import os
from PIL import Image

path1 = sys.argv[1]
path2 = sys.argv[2]

# check if destination directory exists, if not then mkdir
if os.path.exists(path2):
    print(path2 + ' : exists')
else:
    os.mkdir(path2)

files_to_convert = os.listdir(path1)

# loop through directory, convert images to png, compress & save to new directory
for names in files_to_convert:
    img = Image.open(f'{path1}/{names}')
    clean_name = os.path.splitext(names)[0]
    img.save(f'{path2}/{clean_name}.png','png',optimize=True,quality=85)
