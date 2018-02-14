'''
	@author isaacaddis

'''
import serial
from driver import app

#Start serial coms
ser = serial.Serial('/dev/ttyAMA0',9600,timeout=1)
ser.isOpen()

'''
	Loop for capturing serial output of Arduino and passing it to the GUI
'''	
while True:
	try:
		message = ser.readline()			
		app.evaluate_javascript("process("+String(message)+")")
	catch:
		print("There was an error!")
	except KeyboardInterrupt:
		ser.close()
