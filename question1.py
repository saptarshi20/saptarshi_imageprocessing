import cv2
n=int(input('enter the number of frames for flip to occur='))
cap=cv2.VideoCapture(0)
counter=0
while True:
    x,frame=cap.read()
    if(counter%n==0):
        flip=cv2.flip(frame,-1)
    else:
        flip=frame
    cv2.imshow('cap',flip)
    if cv2.waitKey(1000) & 0xFF ==ord('q'):
         break
    counter=counter+1    

