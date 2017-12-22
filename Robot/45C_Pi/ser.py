'''
	@author isaacaddis

	file to handle getting serial input from the onboard Arduino.
'''
import serial
ser = serial.Serial('/dev/ttyAMA0',9600,timeout=1)
ser.isOpen()
message = ""
while True:
    try:
        message = ser.readline()
        print(message)
    except KeyboardInterrupt:
        ser.close()
