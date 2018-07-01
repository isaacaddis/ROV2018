import cv2
import numpy as np
from time import sleep
import sys
import os

__author__ = "isaacaddis"
# 0.0056515 meters per pixel
calibrated=0.0056515
def vis(mirror=True):
	cap = cv2.VideoCapture(1)
        global img
	cv2.namedWindow("45c Robotics", cv2.WND_PROP_FULLSCREEN)
	if mirror:
		while cap.isOpened():
			ret_val, frame = cap.read()
			#img = cv2.flip(frame, 1)
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
				centers = []
				for c in cnts:
                                        if cv2.contourArea(c)<20:
                                            continue
                                        if cv2.contourArea(c)<1000:
                                            continue
					x,y,w,h = cv2.boundingRect(c)
					cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
					M = cv2.moments(c)
					if int(M['m00'])!= 0:
					    cX = int(M['m10']/M['m00'])
					    cY = int(M['m01']/M['m00'])
                                        else:
                                            continue
					centers.append([cX,cY])
					if len(centers)==2:
					    dx= centers[0][0] - centers[1][0]
					    dy = centers[0][1] - centers[1][1]
					    D = abs(dy)
					    #TODO: Calibrate
					    cv2.putText(frame,str(D),
					    (frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
					    2.0, (0, 255, 0), 3)
			cv2.imshow("45c Robotics",frame)
			cv2.imshow("45c Robotics 2",img)
			if cv2.waitKey(1) & 0xFF == ord('q'):
					break
vis(mirror=True)
