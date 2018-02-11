'''
	@author isaacaddis

	file to handle getting serial input from the onboard Arduino.
'''
import serial
# import threading

ser = serial.Serial('/dev/ttyAMA0',9600,timeout=1)
ser.isOpen()
message = ""
# while True:
def ser():
        try:
			message = ser.readline()
			return message
		except KeyboardInterrupt:
			ser.close()
ser()       
