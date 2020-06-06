import cv2
img=cv2.imread('hill.jpg')
print(img.shape)
x=int(input('enter first coordinate'))
y=int(input('enter second coordinate'))
cv2.line(img,(0,0),(x,y),(255,0,0),5)
cv2.imshow('display',img)
cv2.waitKey(0)
