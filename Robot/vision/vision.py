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
class Main(QtGui.QWidget):
    def __init__(self):
        super(Main,self).__init__()
        self.initUI()
    def initUI(self):
        exitButton = Qt.Gui.QPushButton("OK")
        hbox = QtGui.QHboxLayout()
        hbox.addStretch(1)
        hbox.addWidget(exitButton) 
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.showFullScreen()
        self.setWindowTitle('45c')
        self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
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
