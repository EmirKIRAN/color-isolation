import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2
from skimage.io import imshow, imread,show
from skimage.color import rgb2hsv, hsv2rgb

# image read and write
image = imread('image.png')
plt.figure(num=None, figsize=(8, 6), dpi=80)
imshow(image)


# we can clearly see that the red girl is isolated from the rest of the image. 
red_filtered = (image[:,:,0] > 150) & (image[:,:,1] < 100) & (image[:,:,2] < 110)
plt.figure(num=None, figsize=(8, 6), dpi=80)
red_girl_new = image.copy()
red_girl_new[:, :, 0] = red_girl_new[:, :, 0] * red_filtered
red_girl_new[:, :, 1] = red_girl_new[:, :, 1] * red_filtered
red_girl_new[:, :, 2] = red_girl_new[:, :, 2] * red_filtered
imshow(red_girl_new)
show()
