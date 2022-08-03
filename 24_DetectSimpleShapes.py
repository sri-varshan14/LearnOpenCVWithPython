# This program may not give optimal answer but it works

import cv2 as cv
import numpy as np

img = cv.imread("data/shapes.jpg")
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

_,thresh = cv.threshold(img_gray,240,255,cv.THRESH_BINARY)

contours,_ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour,0.001*cv.arcLength(contour,True),True)
    cv.drawContours(img,[approx],0,(0,0,0),5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if(len(approx) == 3):
        cv.putText(img,"TRIANGLE",(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif(len(approx) == 4):
        x,y,w,h = cv.boundingRect(approx)
        aspectRatio = float(w)/h
        if aspectRatio >= 0.95 and aspectRatio <=1.05:
            cv.putText(img,"SQUARE",(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
        else:
            cv.putText(img,"RECTANGLE",(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif(len(approx) == 5):
        cv.putText(img,"PENTAGON",(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    elif(len(approx) == 6):
        cv.putText(img,"HEXAGON",(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))
    else:
        cv.putText(img,"CIRCLE",(x,y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0))

cv.imshow("image",img)
while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()