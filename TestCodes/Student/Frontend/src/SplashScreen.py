import time

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("Frontend/PyQT_UI/splash.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # pixmap = QPixmap("splashBg.jpg")
        # self.setPixmap(pixmap)

    def progress(self):
        for i in range(100):
            time.sleep(0.01)
            self.progressBar.setValue(i)