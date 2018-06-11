import cv2
import numpy as np
from time import sleep
import sys
import os
import keyboard
import helpers
import math

__author__ = "isaacaddis"

def vis(mirror=True):
    print("""/
    ___    _______  _______    _______  _______  ______   _______ __________________ _______  _______
   /   )  (  ____ \(  ____ \  (  ____ )(  ___  )(  ___ \ (  ___  )\__   __/\__   __/(  ____ \(  ____ \
  / /) |  | (    \/| (    \/  | (    )|| (   ) || (   ) )| (   ) |   ) (      ) (   | (    \/| (    \/
 / (_) (_ | (____  | |        | (____)|| |   | || (__/ / | |   | |   | |      | |   | |      | (_____
(____   _)(_____ \ | |        |     __)| |   | ||  __ (  | |   | |   | |      | |   | |      (_____  )
     ) (        ) )| |        | (\ (   | |   | || (  \ \ | |   | |   | |      | |   | |            ) |
     | |  /\____) )| (____/\  | ) \ \__| (___) || )___) )| (___) |   | |   ___) (___| (____/\/\____) |
     (_)  \______/ (_______/  |/   \__/(_______)|/ \___/ (_______)   )_(   \_______/(_______/\_______)

 """)
    vis1 = True
    ANGLE = 1
    FOCAL_LENGTH = 1
    KNOWN_WIDTH_1 = 1
    KNOWN_WIDTH_2 = 1
    cap2 = cv2.VideoCapture(0)
    cv2.namedWindow("45c Robotics", cv2.WINDOW_NORMAL)
    cv2.namedWindow("45c Robotics 2",cv2.WINDOW_NORMAL)
    if mirror:
        while cap.isOpened():
            ret_val, frame = cap.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.flip(frame, 0)
            ret_val2, frame2 = cap2.read()
           # frame2 = cv2.flip(frame2, 1)
            if keyboard.press('a'):
                vis1^=True
                print("Vision state switched on Camera 0.")
            if vis1 == True:
                kernel = np.ones((5,5), np.uint8)
                img = cv2.GaussianBlur(frame,(5,5),0)
                img = cv2.erode(img, kernel, iterations=1)
                img = cv2.dilate(img, kernel, iterations=1)
                img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY)
                img = cv2.Canny(img,100,200)
                img = cv2.bilateralFilter(img, 11, 17, 17)
                _,cnts, _ = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                if len(cnts)>=2:
                    contours = []
                    for c in cnts:
                        if cv2.contourArea(c)<100:
                            continue
                        if cv2.contourArea(c)>1500:
                            continue
                        x,y,w,h = cv2.boundingRect(c)
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
                        M = cv2.moments(c)
                        contous.append(c)
                        if len(centers)==2:
                            area1 = helpers.area_of_contour(centers[0])
                            area2 = helpers.area_of_contour(centers[1])
                            focal_length_1 = helpers.calc_focal_length(KNOWN_DISTANCE_1,KNOWN_WIDTH_1, area1)
                            focal_length_2 = helpers.calc_focal_length(KNOWN_DISTANCE_2,KNOWN_WIDTH_2, area1)
                            distance_between_contours = math.sqrt((focal_length_1**2)+(focal_length_2**2)-(2*focal_length_1*focal_length_2*(math.cos(ANGLE))))
                            cv2.putText(frame,str(distance_between_contours)+" meters",(frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
            cv2.putText(frame,"Vision State: "+str(vis1),(frame.shape[1] - 400, frame.shape[0] - 200), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
            cv2.imshow("45c Robotics",frame)
            cv2.imshow("45c Robotics 2",frame2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
vis(mirror=True)
