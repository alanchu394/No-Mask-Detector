import os
import numpy as np
from PIL import Image
base = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(base, "target")

for root, firs, files, in os.walk(img_dir):
    for file in files:
        path = os.path.join(root,file)
        #print(path)
        pImg = Image.open(path).convert("L")
        img_arr = np.array(pImg,"uint8")
        print(img_arr)