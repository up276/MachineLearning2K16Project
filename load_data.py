import scipy as sp
import os
import re
import keras
import PIL
from keras.preprocessing import image

pix = image.list_pictures('data')

wid=224
ht=224
for i in pix:
    img = image.load_img(i)
    img = img.resize((wid,ht),PIL.Image.ANTIALIAS)
    img.save(i,'JPEG')

