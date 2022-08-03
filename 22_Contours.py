import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("data/opencv-logo-white.png")
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(img_gray,127,255,0)
contours,hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print("Number of Contours : ",str(len(contours)))
print(contours[0])

cv.drawContours(img,contours,-1,(0,255,0),1)

cv.imshow("Image",img)
cv.imshow("Image gray",img_gray)
while True:
    if cv.waitKey(1) &0xFF == ord('q'):
        break
cv.destroyAllWindows()