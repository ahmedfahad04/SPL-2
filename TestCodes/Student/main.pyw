from PyQt5.QtWidgets import *
from Frontend.src.Home import Home
from Frontend.src.SplashScreen import SplashScreen
import sys 

app = QApplication(sys.argv)

splash = SplashScreen()
splash.show()
splash.progress()

window = Home()
window.showMaximized()
window.show()

splash.finish(window)

sys.exit(app.exec_()) 
