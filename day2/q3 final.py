import cv2
import time
start=(time.time())
cap=cv2.VideoCapture(0)
while True:
    x,frame=cap.read()
    end=time.time()
    diff=int(end-start)

    flipped=cv2.flip(frame,-1)
   
    if diff %5==0:
        cv2.imshow('display',flipped)
    else:
        cv2.imshow('display',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break   