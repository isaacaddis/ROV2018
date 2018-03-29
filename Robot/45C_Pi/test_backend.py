
'''
	Testing script for the htmlPy GUI
'''
import time
from driver import app

while True:		
	try:
		msg = "T175"
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
		range(10000) and None; time.sleep(0.0002)
	except KeyboardInterrupt:
		print("There was an error!")		
		ser.close()
