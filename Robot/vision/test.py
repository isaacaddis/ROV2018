import cv2
import numpy as np
import qdarkstyle
import RPi.GPIO as GPIO
from time import sleep
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import *
import os

__author__ = "isaacaddis"
os.environ['PYQTGRAPH_QT_LIB'] = 'PyQt'

'''
Initializations
'''
GPIO.setmode(GPIO.BCM)
# Pin (18) = Vision On/Off for Cam1
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Pin (19) = Vision On/Off for Cam2
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Defaults - On
state = 1
state1 = 1
'''
	Main Loop
'''
class MainApp(QtGui.QWidget):
    def __init__(self):
        super(MainApp,self).__init__()
        self.initUI()
        self.initCam()
        self.label = QtGui.QLabel(self)
        self.vis(mirror=True)
        
    def initUI(self):
		exitButton = QtGui.QPushButton("Close App")
		hbox = QtGui.QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(exitButton)
		exitButton.clicked.connect(self.close)
		vbox = QtGui.QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)
		self.setLayout(vbox)
		self.showFullScreen()
		self.setWindowTitle('45c')
		self.show()
    def initCam(self):
    	'''
    	Capture
    	'''
    	self.capture = cv2.VideoCapture(0)
    	if not self.capture:
			print "Failed capture. Rip."
			sys.exit(1)
        #self.capture2 = cv2.VideoCapture(1)
    	if hasattr(cv2,'cv'):
			self.capture.set(cv2.cv.CAP_PROP_FRAME_WIDTH, 640)
			#self.capture2.set(cv2.cv.CAP_PROP_FRAME_WIDTH, 640)
			self.capture.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 480)
			#self.capture2.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 480)
        else:
			self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
			#self.capture2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
			self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
			#self.capture2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    	self.timer=QtCore.QTimer(self)
        self.timer.timeout.connect(self.vis)
        #30 fps
    	self.timer.start(30)
    def closeApplication():
		choice = QtGui.QMessageBox.question(self, 'Message','Do you really want to exit?',QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			print("Exiting application")
			sys.exit()
		else:
			pass
    def vis(self,mirror=False):
    	'''
    		Vertical Distance mayn
    	'''
    	while True:
			ret_val, img = self.capture.read()
			if mirror: 
				img = cv2.flip(img, 1)
				kernel = np.ones((5,5), np.uint8)
				img = cv2.erode(img, kernel, iterations=1)
				img = cv2.dilate(img, kernel, iterations=1)
				img = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
				_, cnts,_ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
				
				while True:
					for c in cnts:
						#For debug
						#print(c)
						# If contours are too small or large, ignore them:
						if cv2.contourArea(c)<100:
							print("Too small")	
							continue
						cv2.drawContours(img, [c], -1, (0,255,0), 3)
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
							#Display Num of Units
							'''cv2.putText(image, "units" % D,
								(img.shape[1] - 200, img.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
								2.0, (0, 255, 0), 3)
							'''
						height, width = img.shape
						bytesPerLine = 3 * width
						image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)						
						#image = QImage(img,img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888)
						#cv2.imshow("vision",img)
						#return setPixmap(QPixmap.fromImage(image))
						self.label.setPixmap(QtGui.QPixmap.fromImage(image))

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	#Styling
	app.setStyleSheet(qdarkstyle.load_stylesheet_from_environment(is_pyqtgraph=True))
	# Run class
	win = MainApp()
	win.show()
	sys.exit(app.exec_())	
