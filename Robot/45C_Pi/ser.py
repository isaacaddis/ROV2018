
'''
	@author isaacaddis
'''
import time
#import serial
from driver import app

#Start serial coms
#ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
#ser.isOpen()

'''
	Loop for capturing serial output of Arduino and passing it to the GUI
'''	
while True:		
	try:
	#	msg = str(ser.readline().decode('utf-8'))
		msg = 'T133'
		if msg.startswith('T1'):
			message = msg[2:]
			print("T1")
			print(message)
			'''
			function t1(msg){
					smartSystem("T1",msg);
					console.log(msg);
					$('#temp').text(msg);
			}
			'''
			app.evaluate_javascript("document.getElementById('temp').innerHTML="+message+";")
			# app.evaluate_javascript("alert(document.getElementById('temp').textContent);")
			# app.evaluate_javascript("alert("+message+");")
		elif msg.startswith('T2'):
			message = msg[2:]
			print("T2")
			print(message)
			app.evaluate_javascript("t2("+message+");")
		elif msg.startswith('V1'):
			message = msg[2:]
			print("V1")
			print(message)
			app.evaluate_javascript("v1("+message+");")
		elif msg.startswith('V2'):	
			message = msg[2:]
			print("V2")
			print(message)
			app.evaluate_javascript("v2("+message+");")
		range(10000) and None; time.sleep(0.02)		
	except KeyboardInterrupt:
		print("There was an error!")		
		#ser.close()
