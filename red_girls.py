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

# ! we can clearly see that the red girl is isolated from the rest of the image
# ? To better isolate these colors, we can make use of the HSV color space.
# * Let create a function for above declaration.

def display_as_hsv(image):
    
    img = cv2.imread(image)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    hsv_list = ['Hue','Saturation','Value']
    fig, ax = plt.subplots(1, 3, figsize=(15,7), sharey = True)
    
    ax[0].imshow(img_hsv[:,:,0], cmap = 'hsv')
    ax[0].set_title(hsv_list[0], fontsize = 20)
    ax[0].axis('off')
    
    
    ax[1].imshow(img_hsv[:,:,1], cmap = 'Greys')
    ax[1].set_title(hsv_list[1], fontsize = 20)
    ax[1].axis('off')
    
    
    ax[2].imshow(img_hsv[:,:,2], cmap = 'gray')
    ax[2].set_title(hsv_list[2], fontsize = 20)
    ax[2].axis('off')
        
    fig.tight_layout()
    show()

display_as_hsv('image.png')



