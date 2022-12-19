# Here we provide the necessary imports.
# The basic GUI widgets are located in QtWidgets module.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLayout, QMainWindow

# Every PyQt5 application must create an application object.
# The application object is located in the QtWidgets module.
# QApplication holds the Eventloop
app = QApplication([])

# The QWidget widget is the base class of all user interface objects in PyQt5.
# We provide the default constructor for QWidget. The default constructor has no parent.
# A widget with no parent is called a window.
root = QMainWindow()
root.show()  # The show() method displays the widget on the screen.

app.exec_()  # Finally, we enter the mainloop of the application.
