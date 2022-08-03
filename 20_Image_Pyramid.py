import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Learn about Gaussian and Laplacian pyramid

img = cv.imread("data/lena.jpg",cv.IMREAD_COLOR)

lr1 = cv.pyrDown(img)
lr2 = cv.pyrDown(lr1)

hr2 = cv.pyrUp(lr2)

gp = 
cv.imshow('image',img)
cv.imshow('pyrDown1 image',lr1)
cv.imshow('pyrDown2 image',lr2)
cv.imshow('pyrUp2 image',hr2)

while True:
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()