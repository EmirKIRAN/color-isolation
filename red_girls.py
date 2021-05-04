import numpy as np
import matplotlib.pyplot as plt
from cv2 import cv2
from skimage.io import imshow, imread,show
from skimage.color import rgb2hsv, hsv2rgb

image = imread('image.png')
plt.figure(num=None, figsize=(8, 6), dpi=80)
imshow(image)

red_filter_girl = (image[:,:,0]>150)

red_girl_new = image.copy()
red_girl_new[:, :, 0] = red_girl_new[:, :, 0]*red_filter_girl
red_girl_new[:, :, 1] = red_girl_new[:, :, 1]*red_filter_girl
red_girl_new[:, :, 2] = red_girl_new[:, :, 2]*red_filter_girl

plt.figure(num=None, figsize=(8, 6), dpi=80)
imshow(red_girl_new)

show()
