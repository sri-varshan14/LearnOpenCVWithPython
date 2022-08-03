import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = np.zeros((200,200),np.uint8)
cv.rectangle(img,(0,100),(200,200),(255),-1)

img2 = cv.imread('data/lena.jpg',cv.IMREAD_COLOR)

b,g,r = cv.split(img2)

cv.imshow("img",img)
cv.imshow("image",img2)
cv.imshow("B",b)
cv.imshow("G",g)
cv.imshow("R",r)

plt.hist(img.ravel(),256,[0,256])
plt.hist(img2.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()


while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()