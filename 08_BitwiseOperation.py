import cv2 as cv
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = np.zeros_like(img1)
img2 = cv.rectangle(img2,(250,0),(500,250),(255,255,255),-1)

while True:
    cv.imshow("img1",img1)
    cv.imshow("img2",img2)
    cv.imshow("BitWiseAnd",cv.bitwise_and(img1,img2))
    cv.imshow("BitWiseOr",cv.bitwise_or(img1,img2))
    cv.imshow("BitWiseXor",cv.bitwise_xor(img1,img2))
    cv.imshow("BitWiseNot",cv.bitwise_not(img1))
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
