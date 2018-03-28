import os
import htmlPy
import serial
import time 

from PyQt4 import QtGui

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = htmlPy.AppGUI(title=u"45C Robotics 2018",developer_mode=True, maximized=True)

app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")

app.web_app.setMinimumWidth(800)
app.web_app.setMinimumHeight(480)

app.maximized = True

app.template = ("op.html", {})


#app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/static/img/icon.png"))

if __name__ == "__main__":
    app.start()
