from PIL import Image
import os
from tqdm import tqdm

path = "Norway/train/images/"
all_files = os.listdir(path)
all_jpegs = [x for x in all_files if x.endswith('.jpg')]

for img_name in tqdm(all_jpegs):

    img_path = f'{path}/{img_name}'
    img = Image.open(img_path)
    wtop = 0
    htop = img.size[1]-1920
    wdown = 1920
    hdown = img.size[1]
    img = img.crop((wtop, htop, wdown, hdown))
    img.save(img_path)

