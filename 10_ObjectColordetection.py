import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow("TrackingImage")
img = cv.imread("data/smarties.png")
cv.imshow("image",img)

cv.createTrackbar("LH","TrackingImage",0,255,nothing)
cv.createTrackbar("LS","TrackingImage",0,255,nothing)
cv.createTrackbar("LV","TrackingImage",0,255,nothing)
cv.createTrackbar("UH","TrackingImage",255,255,nothing)
cv.createTrackbar("US","TrackingImage",255,255,nothing)
cv.createTrackbar("UV","TrackingImage",255,255,nothing)

while True:
    frame = cv.cvtColor(img,cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos("LH","TrackingImage")
    l_s = cv.getTrackbarPos("LS","TrackingImage")
    l_v = cv.getTrackbarPos("LV","TrackingImage")
    u_h = cv.getTrackbarPos("UH","TrackingImage")
    u_s = cv.getTrackbarPos("US","TrackingImage")
    u_v = cv.getTrackbarPos("UV","TrackingImage")

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv.inRange(frame,l_b,u_b)
    res = cv.bitwise_and(img,img,mask=mask)

    cv.imshow("frame",frame)
    cv.imshow("mask",mask)
    cv.imshow("res",res)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()