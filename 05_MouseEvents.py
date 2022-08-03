import cv2 as cv
import numpy as np

events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

def click_event(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        strXY = str(x)+', '+str(y)
        cv.putText(img,strXY,(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1)
        cv.imshow('image',img)
    if event == cv.EVENT_RBUTTONDOWN:
        strXY = str(img[x,y,2])+', '+str(img[x,y,1])+', '+str(img[x,y,0])
        cv.putText(img,strXY,(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
        cv.imshow('image',img)


img = np.zeros((500,500,3),np.uint8)
img = cv.imread('data/lena.jpg',cv.IMREAD_COLOR)
cv.imshow('image',img)
cv.setMouseCallback('image', click_event)
k = cv.waitKey(0)
cv.destroyAllWindows()