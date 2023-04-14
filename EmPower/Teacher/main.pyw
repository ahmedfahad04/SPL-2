from PyQt5.QtWidgets import *
from Frontend.src.Home import Home
from Frontend.src.Document_Formatter import *
import sys 

app = QApplication(sys.argv)

window = Home()
window.show()

sys.exit(app.exec_()) 

