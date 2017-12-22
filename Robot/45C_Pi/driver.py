import os
import htmlPy
import serial
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

app.web_app.setMinimumWidth(1024)
app.web_app.setMinimumHeight(768)

app.maximized = True

app.template = ("index.html", {})
while True:
	try:
		message = list(ser.readline())
		app.evaluate_javascript("process("+message+")")
	except KeyboardInterrupt:
		ser.close()
	time.sleep(1)
#app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/static/img/icon.png"))


# Binding of back-end functionalities with GUI

# Import back-end functionalities
#from html_to_python import ClassName

# Register back-end functionalities
#app.bind(ClassName())


# Instructions for running application
if __name__ == "__main__":
    # The driver file will have to be imported everywhere in back-end.
    # So, always keep app.start() in if __name__ == "__main__" conditional
    app.start()
