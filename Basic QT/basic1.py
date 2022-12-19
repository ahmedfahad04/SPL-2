import sys
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Qt Window")
        self.resize(QSize(1000, 500))
        
        # Remember, Qt options doesn't provide any suggestion
        # So, you have to remember the options
        
        self.setCursor(QCursor(Qt.WaitCursor)) # https://het.as.utexas.edu/HET/Software/PyQt/qcursor.html#shape 
        
        self.lbl = QLabel("This is Awesome!")
        self.lbl.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.lbl)


app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec_())
