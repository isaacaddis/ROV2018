import cv2
import numpy as np
import math
from time import sleep

def findBiggestContour(cnt):
	max = cv2.contourArea(cnt[0])
	maxContour = cnt[0]
	for i in cnt:
		if cv2.contourArea(i) > max:
			maxContour = i
			max = cv2.contourArea(i)
	return maxContour
    
#get camera stream
cap = cv2.VideoCapture(0)
(lower,upper) = ([int(165/2), int(0*255), int(0.4*255)], [int(175/2), int(1*255), int(1*255)]) #Define the boundries 
lower = np.array(lower)
upper = np.array(upper)

'''
with this, we get an image from cap, make a mask out of it with inRange,
find the biggest contour and draw a rectangle around it
'''
def processImage():
	global cap
	global lower
	global upper
	_, image = cap.read()
	im = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	#im = cv2.imread("/home/thinkredstone/im.jpg")
	mask = cv2.inRange(im, lower, upper)
	#cv2.imwrite("/home/thinkredstone/mask.jpg",mask)
	contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, 2)
	cnt = findBiggestContour(contours)
	x,y,w,h = cv2.boundingRect(cnt)
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
	#cv2.imwrite("/home/thinkredstone/cnt.jpg",mask)
	cv2.imwrite("/home/admin/im.jpg",image)
	'''
	here we use trigonometry to determine the distance from the object, given that 
	the object is t cm wide and the camera captures d degrees
	'''
	t = 101
	d = 50
	height, width, channels = im.shape
	#print 'width: ', width
	#print 'Traget width: ' , w
	v = t/(w/width)# w is how many pixels wide is the object
	#print v
	h = 0.5*v/(math.tan(math.radians(d)/2))
	#now we need to use basic trigo to caculate actually distance, given that he camera is tilted
	tilt = 30 #the tilt of the camera, in degrees
	distance = h * (math.cos(math.radians(tilt)))
	print 'Distance ', distance
	with open('result', 'w') as f:
		f.write(str(distance))
	return distance
