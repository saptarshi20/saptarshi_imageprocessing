import cv2
cap=cv2.VideoCapture(0)
while True:
    x,frame=cap.read()
    frame=cv2.flip(frame,1)
    cv2.imshow('cap',frame)
    key=cv2.waitKey(1000)
    if key==ord('q'):
        break