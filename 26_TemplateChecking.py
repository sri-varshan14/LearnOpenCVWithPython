from curses.ascii import TAB
import cv2 as cv
import numpy as np

img = cv.imread('data/messi5.jpg',cv.IMREAD_COLOR)
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("image",img)
while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()