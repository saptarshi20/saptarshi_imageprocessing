import cv2
import numpy as np
points = []
flag = 0

cap = cv2.VideoCapture(0)
def mouse(event, x, y, flags, param):
    global points, flag
    if event == cv2.EVENT_LBUTTONDOWN:
        points = [(x, y)]
        flag = 1
    elif event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))
        flag = 0
        cv2.rectangle(frame, points[0], points[1], (0, 255, 0), 2)


cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse)
while True:
    x , frame = cap.read()
    if len(points) == 2:
        cropped = frame[points[0][1]:points[1][1], points[0][0]:points[1][0]]
        template = cv2.cvtColor(cropped,cv2.COLOR_BGR2GRAY)
        w = template.shape[1]
        h = template.shape[0]
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.7)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)
            cv2.putText(frame,'object',(pt[0],pt[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))

    cv2.imshow("image", frame)
    if cv2.waitKey(100) & 0xFF == ord("q"):
        break