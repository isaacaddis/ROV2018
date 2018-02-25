import cv2
import numpy as np
import math
import RPi.GPIO as GPIO
import time
from time import sleep
import util
import frontCam
import backCam

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
