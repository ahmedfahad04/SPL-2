from PyQt5.QtWidgets import *
from Frontend.src.Home import Home
from Frontend.src.Document_Formatter import *
import sys 

if __name__ == '__main__':
    

    app = QApplication(sys.argv)

    window = Home()
    window.showMaximized()
    window.show()

    sys.exit(app.exec_()) 

