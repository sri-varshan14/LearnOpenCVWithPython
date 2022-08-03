import cv2 as cv
import numpy as np

img = cv.imread('data/messi5.jpg',cv.IMREAD_COLOR)
img2 = cv.imread('data/opencv-logo.png',cv.IMREAD_COLOR)

print(img.shape)
print(img.size)
print(img.dtype)

b,g,r = cv.split(img)
img = cv.merge((b,g,r))
cv.imshow('B',b)
cv.imshow('G',g)
cv.imshow('R',r)

img = cv.resize(img,(512,512))
img2 = cv.resize(img2,(512,512))

# dst = cv.add(img,img2)
dst = cv.addWeighted(img,0.5,img2,0.5,0)

ball = img[280:340,330:390]
img[273:333, 100:160] = ball
cv.imshow('image',img)
cv.imshow('DST',dst)
cv.waitKey(0)
cv.destroyAllWindows()
