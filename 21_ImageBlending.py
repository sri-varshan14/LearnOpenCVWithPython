import cv2 as cv
from cv2 import Laplacian
import numpy as np
from matplotlib import pyplot as plt

apple = cv.imread('data/apple.jpg',cv.IMREAD_COLOR)
orange = cv.imread('data/orange.jpg',cv.IMREAD_COLOR)

apple_orange_stacked = np.hstack((apple[:,:256],orange[:,256:]))

# Generate gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# Generate gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# Generate laplacain pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5,0,-1):
    gaussian_expanded = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i-1],gaussian_expanded)
    lp_apple.append(laplacian)

# Generate laplacain pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5,0,-1):
    gaussian_expanded = cv.pyrUp(gp_orange[i])
    laplacian = cv.subtract(gp_orange[i-1],gaussian_expanded)
    lp_orange.append(laplacian)

apple_orange_pyramid = []
n=0
for apple_lap,orange_lap in zip(lp_apple,lp_orange):
    n+=1
    col,rows,ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:,0:int(col/2)],orange_lap[:,int(col/2):]))
    apple_orange_pyramid.append(laplacian)
    
cv.imshow("apple",apple)
cv.imshow("orange",orange)
cv.imshow("apple_orange_stacked",apple_orange_stacked)
cv.imshow("apple_orange_reconstructed",apple_orange_pyramid[0])

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()