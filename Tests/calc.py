import cv2
import numpy as np
import helpers
KNOWN_DISTANCE = 0.3084 #.3084 meters
KNOWN_WIDTH = 0.0135 # .0135 meters
cap = cv2.VideoCapture(0)
cv2.namedWindow("Testing for Calculations", cv2.WINDOW_NORMAL)
while cap.isOpened():
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    edged = cv2.Canny(gray,35,125)
    _,cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts)>0:
        c = max(cnts,key=cv2.contourArea)
        area = cv2.minAreaRect(c)
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
        focalLength = helpers.calc_focal_length(KNOWN_DISTANCE,KNOWN_WIDTH,area)
        cv2.putText(frame,str(focalLength),(frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
    cv2.imshow("Testing for Calculations",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break