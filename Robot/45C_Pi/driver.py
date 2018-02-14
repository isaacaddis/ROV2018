import os
import htmlPy
import serial
import ser
import time 

from PyQt4 import QtGui

ser = serial.Serial('/dev/ttyAMA0',9600,timeout=1)
ser.isOpen()
message = ""

# Initial confiurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# GUI initializations
app = htmlPy.AppGUI(title=u"45C Robotics 2018 GUI", maximized=True, plugins=True)


# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")

app.web_app.setMinimumWidth(800)
app.web_app.setMinimumHeight(480)

app.maximized = True

app.template = ("index.html", {})

#app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/static/img/icon.png"))

if __name__ == "__main__":
    app.start()
	while True:
		try:
			message = ser.readline()
			app.evaluate_javascript("process("+message+")")
			time.sleep(0.5)
		except KeyboardInterrupt:
			ser.close()
