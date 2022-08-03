import cv2 as cv
import numpy as np
img = cv.imread('data/lena.jpg',cv.IMREAD_COLOR)
img = np.zeros([512,512,3],np.uint8)
img = cv.line(img,(0,0),(255,255),(0,0,255),2)
img = cv.arrowedLine(img,(0,255),(255,255),(255,0,0),2)
img = cv.rectangle(img,(255,255),(300,300),(0,255,0),-1)
img = cv.circle(img,(350,350),50,(0,255,0),-1)
img = cv.putText(img,"SRI",(10,500),cv.FONT_HERSHEY_SIMPLEX,3,(255,255,255),10)
cv.imshow("Lena",img)
cv.waitKey(0)
cv.destroyAllWindows()