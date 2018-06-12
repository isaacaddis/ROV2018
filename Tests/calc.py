import cv2
import numpy as np
import helpers
KNOWN_DISTANCE_1 =0.08
KNOWN_WIDTH_1 = 0.00635
cap = cv2.VideoCapture(0)
cv2.namedWindow("Testing for Calculations", cv2.WINDOW_NORMAL)
'''
area1 = helpers.area_of_contour(centers[0])
area2 = helpers.area_of_contour(centers[1])
focal_length_1 = helpers.calc_focal_length(KNOWN_DISTANCE_1,KNOWN_WIDTH_1, area1)
focal_length_2 = helpers.calc_focal_length(KNOWN_DISTANCE_2,KNOWN_WIDTH_2, area1)
'''
while cap.isOpened():
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    edged = cv2.Canny(gray,35,125)
    _,cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts)>=2:
        contours = []
        for c in cnts:
            if cv2.contourArea(c)<100:
                continue
            if cv2.contourArea(c)>200:
                continue
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
            M = cv2.moments(c)
            contours.append(c)
            if len(contours)==2:
                print("Area 1")
                area1 = helpers.area_of_contour(contours[0])
                print(area1)
                print("Area 2")
                area2 = helpers.area_of_contour(contours[1])
                print(area2)
                print("Focal length 1 ")
                focal_length_1 = helpers.calc_focal_length(KNOWN_DISTANCE_1,KNOWN_WIDTH_1, area1)
                print(focal_length_1)
                cv2.putText(frame,str(focal_length_1),(frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255,    0), 3)
                #print("Focal length 2")
                #focal_length_2 = helpers.calc_focal_length(KNOWN_DISTANCE_2,KNOWN_WIDTH_2, area1)
                #print(focal_length_2)
    cv2.imshow("Testing for Calculations",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break
