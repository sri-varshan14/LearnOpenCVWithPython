from socketserver import ForkingUDPServer
import cv2 as cv

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output/cam.avi',fourcc,20.0,(640,480))
print(cap.isOpened())
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
cap.set(cv.CAP_PROP_FRAME_WIDTH,)
while True:
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('Frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows() 