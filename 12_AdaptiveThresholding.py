import cv2 as cv
import numpy as np

img = cv.imread("data/sudoku.png",0)
_,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,15,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,7,2)
cv.imshow("Image",img)
cv.imshow("ThreshBinary",th1)
cv.imshow("AdaptiveThresholdingMean",th2)
cv.imshow("AdaptiveThresholdingGaussian",th3)
while True:
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()