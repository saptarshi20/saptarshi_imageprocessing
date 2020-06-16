import cv2
import numpy as np
img=cv2.imread('IMG_3879.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
resized=cv2.resize(img_gray,(int(img.shape[1]/6),int(img.shape[0]/6)))
kernel = np.ones((5,5))
dilate = cv2.dilate(resized,kernel)
cv2.imshow('dilate',dilate)
canny = cv2.Canny(dilate,120,480)
cv2.imshow('frame',resized)
cv2.imshow('Canny',canny)
cv2.imshow('dilate',dilate)
cv2.waitKey(0)
print(img_gray.shape)

