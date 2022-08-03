import cv2 as cv
import numpy as np

img = cv.imread('data/gradient.png',0)
while True:
    _,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    _,th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
    _,th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
    _,th4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
    _,th5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

    cv.imshow('image',img)
    cv.imshow('ThreshBinary',th1)
    cv.imshow('ThreshBinaryInverse',th2)
    cv.imshow('ThreshThrunc',th3)
    cv.imshow('ThreshToZero',th4)
    cv.imshow('ThreshToZeroInverse',th5)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()