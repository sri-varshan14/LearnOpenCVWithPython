import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def  region_of_intrest(img,vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    # match_mask_color = (255,)*channel_count
    match_mask_color = 255
    cv.fillPoly(mask,vertices,match_mask_color)
    masked_image = cv.bitwise_and(img,mask)
    return masked_image


def draw_lines(img,lines):
    img_copy = np.copy(img)
    blank_image = np.zeros_like(img)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(blank_image,(x1,y1),(x2,y2),(0,255,0),thickness=3)
    img_copy = cv.addWeighted(img,0.8,blank_image,1,0)
    return img_copy
img = cv.imread('data/hough.png')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

height = img.shape[0]
width = img.shape[1]

gray_image = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
canny_image = cv.Canny(gray_image,100,200)
region_of_intrest_vertices = [(0,height),(width/2,height/2),(width,height)]

cropped_image = region_of_intrest(canny_image,np.array([region_of_intrest_vertices],np.int32))

lines = cv.HoughLinesP(cropped_image,6,np.pi/60,160,np.array([]),minLineLength=40,maxLineGap=25)
image_with_lines = draw_lines(img,lines)

plt.imshow(image_with_lines)
plt.show()