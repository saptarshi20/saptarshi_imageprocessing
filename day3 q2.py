
import cv2 
import random 
img = cv2.imread('hill.jpg') 
y = (img.shape[1])/7
x = (img.shape[0])/7

for r in range (1,8): #for rows
    
    x1 = int(x*(r-1))
    x2 = int(x*r)
    
    if (r%2) == 0: #for even no. row
        a = 1
        b = 8
        d = 1
    
    if (r%2)!= 0:  #for odd no. row
        a = 7
        b = 0
        d = -1

    for c in range(a,b,d):  #for columns 

        y1 = int(y*(c-1))
        y2 = int(y*c)

        img[x1:x2,y1:y2] = (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255))
        cv2.imshow ('frame', img)
        cv2.waitKey(500)

cv2.destroyWindow('frame')