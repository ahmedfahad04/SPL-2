from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys
from PIL import Image

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label.setMinimumSize(QtCore.QSize(800, 650))
        self.label.setMaximumSize(QtCore.QSize(800, 650))
        self.label.setObjectName("label")

        # add label to main window
        MainWindow.setCentralWidget(self.centralwidget)

        # set qmovie as label
        self.movie = QMovie("coin.gif")
        self.label.setMovie(self.movie)
        self.movie.start()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
