# QLabel() text is truncated

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap, QFontDatabase


def addCustomFont():
    fid = QFontDatabase.addApplicationFont('fonts/Ador_Noirrit.ttf') # path importing issue
    if fid < 0:
        print("Not Loaded")
    else:
        print("ID: ", fid)

    families = QFontDatabase.applicationFontFamilies(fid)
    print(families)


class MainWindow(QMainWindow):
    def __init__(self):
        """Constructor to Main Window"""
        super().__init__()
        addCustomFont()         # you have to import new fonts whenever you start application
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI"""
        self.setGeometry(200, 300, 500, 500)
        self.setWindowTitle("2.1 - User Profile GUI")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        """Adding images and label to window"""

        user_label = QLabel(self)
        user_label.resize(200, 50)
        user_label.setText("ফাহাদ")
        user_label.setFont(QFont("Li Ador Noirrit", 25))
        user_label.setStyleSheet(
            "color: blue; "
            "background-color: yellow; "
            "font: bold; "
        )
        user_label.move(85, 100)       
        

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())