'''
	@author isaacaddis

'''
import serial
from driver import app

#Start serial coms
ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
ser.isOpen()

'''
	Loop for capturing serial output of Arduino and passing it to the GUI
'''	
while True:
	try:
		message = ser.readline().decode('utf-8')	
		app.evaluate_javascript("process("+String(message)+")")
	except KeyboardInterrupt:
		print("There was an error!")		
		ser.close()
