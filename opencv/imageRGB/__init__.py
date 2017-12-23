import cv2
import numpy

I = cv2.imread("/home/shiva/Documents/cnv.png")

R = I[:,:,0]
G = I[:,:,1]
B = I[:,:,2]

cv2.imshow('BLUE',R)
cv2.imshow('GREEN',G)
cv2.imshow('RED',B)

cv2.waitKey(0)