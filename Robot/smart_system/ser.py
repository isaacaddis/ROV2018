'''
    Raspberry Pi end of Smart System
'''
import serial 
import os 

app = htmlPy.AppGUI(title=u"45C Robotics", maximized=True)

app.template_path = os.path.abspath(".")
app.static_path = os.path.abspath(".")

app.template = ("index.html",{"username":"user")

app.start()

ser = serial.Serial('dev/ttyAMA0',9600,timeout=1)
ser.open()

while true:
    message = ser.readline()
    print message
    except KeyboardInterrupt:
        ser.close()

