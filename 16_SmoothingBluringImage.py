import cv2 as cv
from cv2 import bilateralFilter
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('data/lena.jpg',cv.IMREAD_COLOR)
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

kernel_mat = np.ones((5,5),np.float32)/25

dst = cv.filter2D(img,-1,kernel_mat)
blur = cv.blur(img,(5,5))
gblur = cv.GaussianBlur(img,(5,5),0)
median = cv.medianBlur(img,5)
bilateralFilter = cv.bilateralFilter(img,9,75,75)

titles = ['images','2DConvolution','blur','gblue','median',bilateralFilter]
images = [img,dst,blur,gblur,median,bilateralFilter]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.xticks([])

plt.show()