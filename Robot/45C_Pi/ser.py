
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
		msg = str(ser.readline().decode('utf-8'))
		if msg.startswith('T1'):
			message = msg[2:]
			print(message)
			app.evaluate_javascript("t1("+message+");")
		elif msg.startswith('T2'):
			message = msg[2:]
			print(message)
			app.evaluate_javascript("t2("+message+");")
		elif msg.startswith('V1'):
			message = msg[2:]
			print(message)
			app.evaluate_javascript("v1("+message+");")		
		elif msg.startswith('V2'):
			message = msg[2:]
			print(message)
			app.evaluate_javascript("v2("+message+");")		
	except KeyboardInterrupt:
		print("There was an error!")		
		ser.close()
