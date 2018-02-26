import cv2
import numpy as np
import util
cap = cv2.VideoCapture(0)
#cv2.namedWindow("45C Robotics", cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty("45C Robotics",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
centers = []
def run():
	ret, frame = cap.read()
	kernel = np.ones((5,5), np.uint8)
	img = cv2.Canny(frame, 50, 100)
	img = cv2.dilate(img, kernel, iterations=1)	
	img = cv2.erode(img, kernel, iterations=1)
	_, cnts, _ = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,
		                        cv2.CHAIN_APPROX_SIMPLE)
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
	cv2.imshow("45C Robotics", img)
	cv2.waitKey(0)
def kill():
	cap.release()
	cv2.destroyAllWindows()		
