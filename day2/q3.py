import cv2
import time
start=time.time()
cap=cv2.VideoCapture(0)
count=0
while True:
    end=time.time()
    diff=end-start
    print(diff)
    x,frame=cap.read()
    if diff>5:
        flipped=cv2.flip('display',-1)
        cv2.imshow('display',flipped)
    else:
        cv2.imshow('display',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break   
    count+=1