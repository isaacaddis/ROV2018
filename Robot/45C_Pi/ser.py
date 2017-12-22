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
    	# threading.Timer(5.0, ser).start()
        message = ser.readline()
        # print(message)
        return message
    except KeyboardInterrupt:
        ser.close()
