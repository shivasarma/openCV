import cv2


I = cv2.imread("/home/shiva/Documents/cnv.png")
#print(I)

#cv2.namedWindow("some",CV_WINDOW_AUTOSIZE)
cv2.imshow('some',I)
cv2.waitKey()