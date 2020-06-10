
import cv2
import random

img = cv2.imread ('hill.jpg')
dimensions = img.shape
y = (img.shape[1])/7
x = (img.shape[0])/7

for r in range (1,8):
    
    x1 = int(x*(r-1))
    x2 = int(x*r)
    
    for c in range(1,8):  

        y1 = int(y*(c-1))
        y2 = int(y*c)

        img[x1:x2,y1:y2] = (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255))
        cv2.imshow ('frame', img)
    
cv2.waitKey(1000)
cv2.destroyWindow('frame')