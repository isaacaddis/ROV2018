#!/usr/bin/env python

from PySide.QtCore import *
from PySide.QtGui import *
import cv2
import qdarkstyle
import sys
import numpy as np

class MainApp(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.video_size = QSize(320, 240)
        self.setup_ui()
        self.setup_camera()

    def setup_ui(self):
        """Initialize widgets.
        """
        self.image_label = QLabel()
        self.image_label.setFixedSize(self.video_size)

        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.close)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addWidget(self.quit_button)

        self.setLayout(self.main_layout)

    def setup_camera(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture(0)
        if hasattr(cv2,'cv'):
            self.capture.set(cv2.cv.CAP_PROP_FRAME_WIDTH, 960)
            #self.capture2.set(cv2.cv.CAP_PROP_FRAME_WIDTH, 640)
            self.capture.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 540)
            #self.capture2.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, 480)
        else:
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
            #self.capture2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
            #self.capture2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        ret_val, frame = self.capture.read()
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
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dark_stylesheet = qdarkstyle.load_stylesheet_pyside()
    app.setStyleSheet(dark_stylesheet)
    win = MainApp()
    win.show()
    sys.exit(app.exec_())
