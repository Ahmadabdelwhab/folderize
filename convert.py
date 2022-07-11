from PIL import Image
import imageio.v2 as imageio
import os
import sys
def convert():
    img = imageio.imread('real.png')
    imageio.imwrite('real1.ico', img)
def change_size():
    im = Image.open('real.png')
    resized = im.resize((612,612))
    os.remove("real.png")
    resized.save("real.png")
change_size()