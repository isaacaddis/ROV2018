
'''
	@author isaacaddis
'''
import time
import serial
from driver import app
import PySide.QtCore as q

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
			print("T1")
			print(message)
			app.evaluate_javascript("document.getElementById('temp').innerHTML="+message+";")
			die_time=q.QTime.currentTime().addSecs(1)
			while q.QTime.currentTime() < die_time:
				q.QCoreApplication.processEvents(q.QEventLoop.AllEvents,100)
		elif msg.startswith('T2'):
			message = msg[2:]
			print("T2")
			print(message)
			app.evaluate_javascript("document.getElementById('temp2').innerHTML="+message+";")
			die_time=q.QTime.currentTime().addSecs(1)
			while q.QTime.currentTime() < die_time:
				q.QCoreApplication.processEvents(q.QEventLoop.AllEvents,100)
		elif msg.startswith('V1'):
			message = msg[2:]
			print("V1")
			print(message)
			app.evaluate_javascript("document.getElementById('volt').innerHTML="+message+";")
			die_time=q.QTime.currentTime().addSecs(1)
			while q.QTime.currentTime() < die_time:
				q.QCoreApplication.processEvents(q.QEventLoop.AllEvents,100)
		elif msg.startswith('V2'):	
			message = msg[2:]
			print("V2")
			print(message)
			app.evaluate_javascript("document.getElementById('volt2').innerHTML="+message+";")
			die_time=q.QTime.currentTime().addSecs(1)
			while q.QTime.currentTime() < die_time:
				q.QCoreApplication.processEvents(q.QEventLoop.AllEvents,100)
		range(10000) and None; time.sleep(0.02)		
	except KeyboardInterrupt:
		print("There was an error!")		
		#ser.close()
