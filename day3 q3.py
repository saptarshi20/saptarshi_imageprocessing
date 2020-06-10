import cv2 
import random 
img = cv2.imread('hill.jpg') 
y = (img.shape[1])/7
x = (img.shape[0])/7

for r in range (1,8):
    
    x1 = int(x*(r-1))
    x2 = int(x*r)
    
    if (r%2) == 0: 
        p = 1
        q = 8
        s = 1
    
    if (r%2)!= 0:  
        p = 7
        q = 0
        s = -1

    for c in range(p,q,s):  
        
        y1 = int(y*(c-1))
        y2 = int(y*c)
        img = cv2.imread('hill.jpg') 

        img[x1:x2,y1:y2] = (255,0,0)
        cv2.imshow ('frame', img)
        cv2.waitKey(500)

cv2.destroyWindow('frame')