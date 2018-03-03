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
        _,frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame = cv2.flip(frame,1)
        image = QImage(frame,frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
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
