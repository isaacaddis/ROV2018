import cv2
import numpy as np
import util
cap = cv2.VideoCapture(0)
#cv2.namedWindow("45C Robotics", cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty("45C Robotics",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
def run():
	ret, frame = cap.read()
	kernel = np.ones((5,5), np.uint8)
	img = cv2.Canny(frame, 50, 100)
	img = cv2.dilate(img, kernel, iterations=1)	
	img = cv2.erode(img, kernel, iterations=1)
	_, cnts, _ = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,
		                        cv2.CHAIN_APPROX_SIMPLE)
	if len(cnts)>0:
		#cnt = util.findBiggestContour(cnts)
		x,y,w,h = cv2.boundingRect(cnt)
		cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
	cv2.imshow("45C Robotics", img)
	cv2.waitKey(0)
def kill():
	cap.release()
	cv2.destroyAllWindows()		
