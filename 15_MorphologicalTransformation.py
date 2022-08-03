import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("data/smarties.png",cv.IMREAD_GRAYSCALE)

_,mask = cv.threshold(img,220,255,cv.THRESH_BINARY_INV)
kernel_mat = np.ones((3,3),np.uint8)
dilation = cv.dilate(mask,kernel_mat,iterations=3)
erosion = cv.erode(mask,kernel_mat,iterations=3)

opening = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel_mat)
closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel_mat)
mg = cv.morphologyEx(mask,cv.MORPH_GRADIENT,kernel_mat)
th = cv.morphologyEx(mask,cv.MORPH_TOPHAT,kernel_mat)

titles = ['images','mask','dilation','erosion','opening','closing','mg','th']
images = [img,mask,dilation,erosion,opening,closing,mg,th]

for i in range(len(images)):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()