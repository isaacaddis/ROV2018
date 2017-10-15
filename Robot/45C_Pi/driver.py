import os
import htmlPy
from PyQt4 import QtGui


# Initial confiurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# GUI initializations
app = htmlPy.AppGUI(title=u"45C Robotics 2018 GUi", maximized=True, plugins=True)


# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")

app.web_app.setMinimumWidth(1280)
app.web_app.setMinimumHeight(720)

app.maximized = True

app.template = ("index.html", {})
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
import os
import htmlPy
from PyQt4 import QtGui


# Initial confiurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# GUI initializations
app = htmlPy.AppGUI(title=u"2018 45C Robotics", maximized=True, plugins=True)


# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")

app.web_app.setMinimumWidth(1024)
app.web_app.setMinimumHeight(768)

app.maximized = True

app.template = ("index.html", {})
# app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/static/img/icon.png"))

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
