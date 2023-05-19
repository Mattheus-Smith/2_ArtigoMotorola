import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage import img_as_ubyte
from matplotlib.patches import Rectangle

dinner = imread('dinner.jpg')
plt.imshow(dinner, cmap='gray')