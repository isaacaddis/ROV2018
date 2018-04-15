'''
	Open window sized 600x600 pixels for calibration
'''
import cv2

def show(mirror=True):
	cap = cv2.VideoCapture(0)
#	cv2.namedWindow('45c Robotics',cv2.WINDOW_NORMAL)
#	cv2.resizeWindow('45c Robotics', 600,600)
	if mirror:
		while cap.isOpened():
                        print("Opened")
			ret_val, frame = cap.read()
			cv2.imshow('45c Robotics',frame)
show(mirror=True)
