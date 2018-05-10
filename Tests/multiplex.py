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

    cap = cv2.VideoCapture(1)
    cap2 = cv2.VideoCapture(0)
    cv2.namedWindow("45c Robotics", cv2.WINDOW_NORMAL)
    cv2.namedWindow("45c Robotics 2",cv2.WINDOW_NORMAL)
    if mirror:
        while cap.isOpened():
            ret_val, frame = cap.read()
            ret_val2, frame2 = cap2.read()
            #frame = cv2.flip(frame, 1)
            #frame = cv2.flip(frame, 0)
            cv2.imshow("45c Robotics",frame)
            cv2.imshow("45c Robotics 2",frame2)
           # cv2.waitKey(50)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
vis(mirror=True)
