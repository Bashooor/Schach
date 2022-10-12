import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg')
re_img = cv2.resize(img, (512, 512))
gray = cv2.cvtColor(re_img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(re_img, 225, 250, apertureSize=3)
lines = cv2.HoughLinesP(canny, 1, np.pi/180, 100, minLineLength=1, maxLineGap=200)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(re_img, (x1,y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('image', re_img)
cv2.imshow('edges', canny)
cv2.imshow('gray', gray)
