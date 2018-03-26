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

__author__ = "isaacaddis"
os.environ['PYQTGRAPH_QT_LIB'] = 'PyQt'

def vis(mirror=False):
	'''			
		Vertical Distance mayn
	'''
	cap = cv2.VideoCapture(0)
	while True:
		ret_val, frame = cap.read()
		if mirror: 
			img = cv2.flip(frame, 1)
			kernel = np.ones((5,5), np.uint8)
			img = cv2.erode(img, kernel, iterations=1)
			img = cv2.dilate(img, kernel, iterations=1)
			img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
			img = cv2.bilateralFilter(img, 11, 17, 17)
			'''img	 = cv2.Canny(img, 30, 200) '''
			_,cnts, _ = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
			if len(cnts)==2:
				for c in cnts:
					cv2.drawContours(frame, [c], 0, (0,255,0), 3)
					#For debug
					print(c)
					# If contours are too small or large, ignore them:
					'''if cv2.contourArea(c)<100:
						print("Too small")	
						continue
					'''
					#x,y,w,h = cv2.boundingRect(cnts)
					#cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
					# Find center point of contours:
					M = cv2.moments(c)
					centers = []
					cX = int(M['m10'] /M['m00'])
					cY = int(M['m01'] /M['m00'])
					centers.append([cX,cY])		
					if len(centers) >=2:
						dx= centers[0][0] - centers[1][0]
						dy = centers[0][1] - centers[1][1]
						D = np.sqrt(dx*dx+dy*dy)
						print(D)
					if cv2.waitKey(1) & 0xFF == ord('q'):
						break
		cv2.imshow("45c Robotics",frame)	
vis(mirror=True)
