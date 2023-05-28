import os
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import *
from Frontend.src.Home import Home
from Frontend.src.SplashScreen import SplashScreen
from Frontend.Student_UI.ui_student_info import Ui_Student_Info
from Frontend.src.Add_Student_Info import Add_Student_info
import sys

app = QApplication(sys.argv)
splash = SplashScreen()

# Center the splash screen window on the screen
splash_width = splash.width()
splash_height = splash.height()
screen = QGuiApplication.primaryScreen()
screen_geometry = screen.availableGeometry()
x = (screen_geometry.width() - splash_width) // 2
y = (screen_geometry.height() - splash_height) // 2
splash.move(x, y)

# now show the splash window
splash.show()
splash.progress()

# MAIN WINDOW
window = Home()
window.showMaximized()
window.show()

splash.finish(window)

sys.exit(app.exec_()) 





