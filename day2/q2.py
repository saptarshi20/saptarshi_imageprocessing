import cv2
cap=cv2.VideoCapture(0)
count=0
while True:
    x,frame=cap.read()
    count=count+1
    if count<=100:
        cv2.imshow('display',frame)
        cv2.imwrite('dataset/IMG_'+str(count)+'.jpg',frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break