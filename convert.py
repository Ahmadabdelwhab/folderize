from PIL import Image
import imageio.v2 as imageio
import os
def convert(img_path):
    img = imageio.imread(img_path+"\icon.png")
    imageio.imwrite(img_path+"\icon.ico", img)
def change_size(img_path , size = (512,512)):
    im = Image.open(img_path+"\icon.png")
    resized = im.resize(size)
    os.remove(img_path+"\icon.png")
    resized.save(img_path+"\icon.png")

