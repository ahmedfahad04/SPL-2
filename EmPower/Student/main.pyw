from PyQt5.QtWidgets import *
from Frontend.src.Home import Home
import sys 

app = QApplication(sys.argv)

window = Home()
window.showMaximized()
window.show()

sys.exit(app.exec_()) 
