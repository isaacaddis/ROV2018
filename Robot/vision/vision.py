#!/usr/bin/env python

from PySide.QtCore import *
from PySide.QtGui import *
import keyboard
import cv2
import qdarkstyle
import sys
import numpy as np
import threading

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print("Starting: " + self.previewName)
        MainApp.setup_camera(self.previewName, self.camID)
class MainApp(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.video_size = QSize(500,500)
        self.video_size2 = QSize(1000,1000)
        self.setup_ui()
        cam1 = camThread("Cam 1",0)
        cam2 = camThread("Cam 2",1)
        cam1.run()
        cam2.run()

    def setup_ui(self):
        """Initialize widgets.
        """
        self.image_label = QLabel()
        self.image_label.setFixedSize(self.video_size)

        self.image_label2 = QLabel()
        self.image_label2.setFixedSize(self.video_size2)

        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.close)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addWidget(self.image_label2)
        self.main_layout.addWidget(self.quit_button)

        self.setLayout(self.main_layout)
        self.setWindowTitle('45c Robotics Video Multiplexer')
        self.showMaximized()

    def setup_camera(previewName,camID):
        """Initialize camera.
        """
        if camID==0:
            capture = cv2.VideoCapture(0)
            if hasattr(cv2,'cv'):
                capture.set(cv2.cv.CAP_PROP_FRAME_WIDTH, 960)
                # self.capture2.set(cv2.cv.CAP_PROP_FRAME_WIDTH, 640)
                capture.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 540)
                # self.capture2.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 480)
            else:
                capture.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
                # self.capture2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
                # self.capture2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            timer = QTimer()
            timer.timeout.connect(MainApp.cap)
            timer.start(30)
        elif camID==1:
            capture2 = cv2.VideoCapture(1)
            if hasattr(cv2,'cv'):
                # self.capture.set(cv2.cv.CAP_PROP_FRAME_WIDTH, 960)
                capture2.set(cv2.cv.CAP_PROP_FRAME_WIDTH, 640)
                # self.capture.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 540)
                capture2.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 480)
            else:
                # self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
                capture2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                # self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
                capture2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            timer = QTimer()
            timer.timeout.connect(MainApp.cap2)
            timer.start(30)
    #True means turn vision on
    capState = True
    def cap(self):
        if keyboard.is_pressed('A'):
            #Alternate between true and false
            self.capState^=True
            print("State of capState is now: ")
            print(self.capState)
        ret_val, frame = self.capture.read()
        if self.capState:
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
                cntsSorted = sorted(cnts,key=cv2.contourArea,reverse=True)
                cnts1=cntsSorted[0]
                cnts2=cntsSorted[1]
                cntsShort = [cnts1,cnts2]
                x,y,w,h = cv2.boundingRect(cnts1)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
                x,y,w,h = cv2.boundingRect(cnts2)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
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
                D = abs(dy)
                #TODO: Calibrate
                cv2.putText(frame,str(D),
                (frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
                2.0, (0, 255, 0), 3)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(image))
    capState2 = True
    def cap2(self):
        if keyboard.is_pressed('L'):
            self.capState2^=True
            print("State of capState2 is now: ")
            print(self.capState2)
        ret_val, frame = self.capture2.read()
        if self.capState2:
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
                cntsSorted = sorted(cnts,key=cv2.contourArea,reverse=True)
                cnts1=cntsSorted[0]
                cnts2=cntsSorted[1]
                cntsShort = [cnts1,cnts2]
                x,y,w,h = cv2.boundingRect(cnts1)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
                x,y,w,h = cv2.boundingRect(cnts2)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
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
                D = abs(dy)
                #TODO: Calibrate
                cv2.putText(frame,str(D),
                (frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
                2.0, (0, 255, 0), 3)
        image2 = QImage(frame2, frame2.shape[1], frame2.shape[0], frame2.strides[0], QImage.Format_RGB888)
        self.image_label2.setPixmap(QPixmap.fromImage(image2))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dark_stylesheet = qdarkstyle.load_stylesheet_pyside()
    app.setStyleSheet(dark_stylesheet)
    win = MainApp()
    win.show()
    sys.exit(app.exec_())
