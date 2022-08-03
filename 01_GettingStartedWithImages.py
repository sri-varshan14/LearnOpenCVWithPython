import cv2 as cv

img = cv.imread("data/lena.jpg",cv.IMREAD_GRAYSCALE)
cv.imshow("Lena Gray",img)
k = cv.waitKey(0) &0xFF
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite("output/lena_gray.jpg",img)

cv.destroyAllWindows()