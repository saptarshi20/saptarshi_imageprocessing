import cv2
import time
cap=cv2.VideoCapture(0)
start=int(time.time())
newend=start
oldend=newend
d=0
c=0
while True:
    x,frame=cap.read()
    flip=cv2.flip(frame,0)
    newend=int(time.time())
    cv2.imshow('image',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break   
    if (newend==oldend):
        continue
    d=newend-oldend
    if(c<5):
        c=c+d
        print(c)
    if(c==5):
        cv2.imshow('image',flip)
        cv2.waitkey(200)
        d=0
        c=0
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break  
    oldend=newend  