# coding=utf-8
import cv2
import numpy as np
import math
import RPi.GPIO as GPIO
import time
from time import sleep
import util
import frontCam
import backCam
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

__author__ = "isaacaddis"

'''
Initializations
'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
state = 1

'''
	Main Loop
'''
class MainApp(QtGui.QWidget):
    def __init__(self):
        super(MainApp,self).__init__()
        self.initUI()
        self.initCam()
    def initUI(self):
        exitButton = QtGui.QPushButton("OK")
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(exitButton) 
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.showFullScreen()
        self.setWindowTitle('45c')
        self.show()
    def initCam(self):
    	self.capture = cv2.VideoCapture(0)
    	if hasattr(cv2,'cv'):
			self.capture.set(cv2.cv.CAP_PROP_FRAME_WIDTH, 640)
			self.capture.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 480)
        else:
			self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
			self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    	self.timer=QtCore.QTimer(self)
        self.timer.timeout.connect(self.vis)
        #30 fps
    	self.timer.start(30)
    def vis(self):
	ret, frame = self.capture.read()
	kernel = np.ones((5,5), np.uint8)
	img = cv2.Canny(frame, 50, 100)
	img = cv2.dilate(img, kernel, iterations=1)	
	img = cv2.erode(img, kernel, iterations=1)
	_, cnts, _ = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	for c in cnts:
		# If contours are too small or large, ignore them:
		if cv2.contourArea(c)<100:
			continue
		elif cv2.contourArea(c)>2000:
			continue
        cv2.drawContours(frame, [c], -1, (0,255,0), 3)
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        # Find center point of contours:
        M = cv2.moments(c)
        cX = int(M['m10'] /M['m00'])
        cY = int(M['m01'] /M['m00'])
        centers.append([cX,cY])		
        if len(centers) >=2:
			dx= centers[0][0] - centers[1][0]
			dy = centers[0][1] - centers[1][1]
			D = np.sqrt(dx*dx+dy*dy)
			print(D)
        image = QImage(img,img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(image))
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	win = MainApp()
	win.show()
	sys.exit(app.exec_())		
'''
while True:
	#Default (State 1) - Front Camera
	if state == 1:
		frontCam.run()
		if GPIO.input(18):
			frontcam.kill()
			state ^= 1
	#State 0 - Bottom Camera
	else:
		backCam.run()
		if GPIO.input(18):
			backCam.kill()
			state ^= 1
'''
