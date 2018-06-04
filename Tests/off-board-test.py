import cv2
import numpy as np
from time import sleep
import sys
import os
import keyboard

__author__ = "isaacaddis"

def vis(mirror=True):
    conversion_rate = 0.00214285714
    vis1 = True
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("45c Robotics", cv2.WINDOW_NORMAL)
    if mirror:
        while cap.isOpened():
            ret_val, frame = cap.read()
           # frame = cv2.flip(frame, 1)
           # frame = cv2.flip(frame, 0)
           # ret_val2, frame2 = cap2.read()
           # frame2 = cv2.flip(frame2, 1)
            if keyboard.is_pressed('a'):
                vis1^=True
                print("Vision state switched on Camera 0.")
                cv2.putText(frame,"Change vision state",(frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
            if vis1 == True:
                kernel = np.ones((5,5), np.uint8)
                img = cv2.GaussianBlur(frame,(5,5),0)
                img = cv2.erode(img, kernel, iterations=1)
                img = cv2.dilate(img, kernel, iterations=1)
                img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY)
                img = cv2.Canny(img,100,200)
                img = cv2.bilateralFilter(img, 11, 17, 17)
                _,cnts, _ = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                centers = []
                if len(cnts)>=2:
                    for c in cnts:
                        if cv2.contourArea(c)<100:
                            continue
                        if cv2.contourArea(c)>1500:
                            continue
                        x,y,w,h = cv2.boundingRect(c)
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
                        M = cv2.moments(c)
                        if M['m00']!=0:
                            cX = int(M['m10'] /M['m00'])
                            cY = int(M['m01'] /M['m00'])
                            centers.append([cX,cY])
                        else:
                            print("Impossible to append to centers.")
                        if len(centers)==2:
                            dx= centers[0][0] - centers[1][0]
                            dy = centers[0][1] - centers[1][1]
                            D = abs(dx)
                            print("Distance (pixels): ")
                            print(D)
                            print("Distance (meters): ")
                            D = D * conversion_rate
                            print(D)
                            cv2.putText(frame,str(D)+" meters",(frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
            cv2.imshow("45c Robotics",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
vis(mirror=True)
