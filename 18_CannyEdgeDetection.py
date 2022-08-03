from tokenize import Imagnumber
import cv2 as cv
from matplotlib.animation import ImageMagickFileWriter
import numpy as np
from matplotlib import legend_handler, pyplot as plt

img = cv.imread("data/messi5.jpg",0)

canny = cv.Canny(img,100,200)

titles = ['image','Canny']
images = [img,canny]

for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()