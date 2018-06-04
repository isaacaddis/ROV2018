import cv2
import numpy as np
from time import sleep
import sys
import os
import keyboard

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
    conversion_rate = 0.00214285714
    vis1 = True
    vis2 = False
    # Default - Red
    color_mode="red"
    cap = cv2.VideoCapture(1)
    cap2 = cv2.VideoCapture(0)
    cv2.namedWindow("45c Robotics", cv2.WINDOW_NORMAL)
  #  cv2.resizeWindow("45c Robotics", 960,540)
    cv2.namedWindow("45c Robotics 2",cv2.WINDOW_NORMAL)
 #   cv2.resizeWindow("45c Robotics 2",960,540)
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
            if keyboard.is_pressed('l'):
                vis2^=True
                print("Vision state switched on Camera 1.")
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
                            '''
                            #TODO: Calibrate
                            print("Distance (meters): ")
                            D = D * conversion_rate
                            print(D)
                            '''
                            #cv2.putText(frame,str(D)+" pixels",(frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
            if vis2 == True:
                kernel = np.ones((5,5), np.uint8)
                img = cv2.GaussianBlur(frame2,(5,5),0)
                if keyboard.is_pressed('s'):
                    if color_mode == "red":
                        color_mode == "blue"
                        print("Switched color mode to " + color_mode)
                    elif color_mode == "blue":
                        color_mode == "none"
                        print("Switched color mode to " + color_mode)
                    elif color_mode == "none":
                        color_mode == "red"
                        print("Switched color mode to " + color_mode)
                    print("Switched color mode to")
                if color_mode == "red":
                    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                    img = cv2.inRange(hsv,(0,0,30),(80,80,255))
                if color_mode == "blue":
                    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                    img = cv2.inRange(hsv,(110,150,150),(130,255,255))
                img = cv2.erode(img, kernel, iterations=1)
                img = cv2.dilate(img, kernel, iterations=1)
                # img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY)
                img = cv2.Canny(img,100,200)
                img = cv2.bilateralFilter(img, 11, 17, 17)
                _,cnts, _ = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                centers = []
                if len(cnts)>=2:
                    for c in cnts:
                        if cv2.contourArea(c)<100:
                            continue
                        if cv2.contourArea(c)>2000:
                            continue
                       # x,y,w,h = cv2.boundingRect(c)
                       # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
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
                            print ("Distance (meters): ")
                            D = D * conversion_rate
                            print(D)
                            #TODO: Calibrate
                            #cv2.putText(frame,str(D),(frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
            #cv2.putText(frame,"Vision State: "+str(vis1),(frame.shape[1] - 400, frame.shape[0] - 200), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), 3)
            #cv2.putText(frame2,"Vision 2 State: "+str(vis2),(frame.shape[1] - 400, frame.shape[0] - 200), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), 3)
            cv2.imshow("45c Robotics",frame)
            cv2.imshow("45c Robotics 2",frame2)
            cv2.waitKey(50)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
vis(mirror=True)
