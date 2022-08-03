import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("data/lena.jpg",cv.IMREAD_COLOR)
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()