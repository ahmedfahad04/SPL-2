from PyQt5.QtWidgets import *
from Frontend.src.Home_T import Teacher_Home
import sys 

app = QApplication(sys.argv)

window = Teacher_Home()
window.show()

sys.exit(app.exec_()) 
