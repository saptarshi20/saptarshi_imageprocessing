import cv2
import numpy as np
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
cv2.namedWindow('trackbar')
cv2.createTrackbar('L-H','trackbar',0,179,nothing)
cv2.createTrackbar('L-S','trackbar',0,255,nothing)
cv2.createTrackbar('L-V','trackbar',0,255,nothing)
cv2.createTrackbar('U-H','trackbar',179,179,nothing)
cv2.createTrackbar('U-S','trackbar',255,255,nothing)
cv2.createTrackbar('U-V','trackbar',255,255,nothing)
while True:
    x,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos('L-H','trackbar')
    ls=cv2.getTrackbarPos('L-S','trackbar')
    lv=cv2.getTrackbarPos('L-V','trackbar')
    uh=cv2.getTrackbarPos('U-H','trackbar')
    us=cv2.getTrackbarPos('U-S','trackbar')
    uv=cv2.getTrackbarPos('U-V','trackbar')

    lrange=np.array([lh,ls,lv])
    urange=np.array([uh,us,uv])
    mask=cv2.inRange(hsv,lrange,urange)
    hotspot=cv2.bitwise_and(frame,frame,mask=mask)
    
    contours, heirarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    areas=[cv2.contourArea(c) for c in contours]
    max_index=np.argmax(areas)
    max_contour=contours[max_index]
    cv2.drawContours(frame,[max_contour],-1,(0,255,0),5)

    cv2.imshow('frame',frame)
    cv2.imshow('a',mask)
    cv2.imshow('b',hotspot)
    key=cv2.waitKey(1)
    if key==27:
        break

