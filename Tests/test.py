import cv2
import numpy as np
#import qdarkstyle
#import RPi.GPIO as GPIO
from time import sleep
import sys
#from PyQt4 import QtGui
#from PyQt4 import QtCore
#from PyQt4.QtGui import *
import os

#__author__ = "isaacaddis"
#os.environ['PYQTGRAPH_QT_LIB'] = 'PyQt'

def vis(mirror=True):
	#it = 0
	cap = cv2.VideoCapture(1)
	if mirror:
		while cap.isOpened():
			#it+=1
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
			if len(cnts)>0:
				cntsSorted = sorted(cnts,key=cv2.contourArea,reverse=True)
				cnts1=cntsSorted[0]
				cnts2=cntsSorted[1]
				cntsShort = [cnts1,cnts2]
				#print(cntsSorted)
				x,y,w,h = cv2.boundingRect(cnts1)
				cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
				x,y,w,h = cv2.boundingRect(cnts2)
				cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
				# Find center point of contours:
				M = cv2.moments(cnts1)
				cX = int(M['m10'] /M['m00'])
				cY = int(M['m01'] /M['m00'])
				centers.append([cX,cY])		
				M = cv2.moments(cnts2)
				cX = int(M['m10'] /M['m00'])
				cY = int(M['m01'] /M['m00'])
				centers.append([cX,cY])		 
				dx= centers[0][0] - centers[1][0]
				dy = centers[0][1] - centers[1][1]
				D = np.sqrt(dx*dx+dy*dy)
				#print(D)
				cv2.putText(frame,str(D),
		(frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
		2.0, (0, 255, 0), 3)
			cv2.namedWindow("45c Robotics", cv2.WND_PROP_FULLSCREEN)
			cv2.setWindowProperty("45c Robotics", cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)			
			cv2.imshow("45c Robotics",frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
				
vis(mirror=True)
