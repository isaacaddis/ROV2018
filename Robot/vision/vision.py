import cv2
import numpy as np
import qdarkstyle
import RPi.GPIO as GPIO
from time import sleep
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
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
	self.vis()
    '''
    	Start app layout
    '''
    def initUI(self):
        exitButton = QtGui.QPushButton("Close App")
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(exitButton)
	self.exitButton.triggered.connect(self.closeApplication)
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.showFullScreen()
        self.setWindowTitle('45c Robotics')
        self.show()
    '''
    Close App
    '''
    def closeApplication():
	choice = QtGui.QMessageBox.question(self, 'Message','Do you really want to exit?',QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
	if choice == QtGui.QMessageBox.Yes:
	    print("Exiting application")
	    sys.exit()
	else:
            pass
    def initCam(self):
    	'''
    	Capture
    	'''
    	self.capture = cv2.VideoCapture(0)
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
    def vis(self):
    	'''
    		Vertical Distance mayn
    	'''
    	ret, frame = self.capture.read()
    	kernel = np.ones((5,5), np.uint8)
    	img = cv2.erode(frame, kernel, iterations=1)
    	img = cv2.dilate(img, kernel, iterations=1)	
    	_, cnts, _ = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    	if state == 1:
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
					(mx,my)=midpoint((dx,dy),())
					#Display Num of Units
					cv2.putText(image, "units" % D,
						(img.shape[1] - 200, img.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
						2.0, (0, 255, 0), 3)
		        image = QImage(img,img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888)
		        self.image_label.setPixmap(QPixmap.fromImage(image))
		        '''
			Horizontal Distance Task
		
		ret, frame = self.capture2.read()
		kernel = np.ones((5,5), np.uint8)
		img = cv2.Canny(frame, 50, 100)
		img = cv2.dilate(img, kernel, iterations=1)	
		img = cv2.erode(img, kernel, iterations=1)
		image = QImage(img,img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888)
		self.image_label.setPixmap(QPixmap.fromImage(image))
		'''
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	#Styling
	app.setStyleSheet(qdarkstyle.load_stylesheet_from_environment(is_pyqtgraph=True))
	# Run class
	win = MainApp()
	win.show()
	sys.exit(app.exec_())		
