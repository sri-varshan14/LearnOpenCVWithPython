import cv2 as cv
from cv2 import solve
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("data/sudoku.png",cv.IMREAD_GRAYSCALE)

lap = cv.Laplacian(img,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
sobelx = cv.Sobel(img,cv.CV_64F,1,0)
sobely = cv.Sobel(img,cv.CV_64F,0,1)
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobelCombine = cv.bitwise_or(sobely,sobelx)
titles = ['image','Laplacian','sobelx','sobely','sobelCombine']
images = [img,lap,sobelx,sobely,sobelCombine]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()