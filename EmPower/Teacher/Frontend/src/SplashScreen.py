import time

from PyQt5.QtWidgets import QSplashScreen
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("Frontend/PyQT_UI/splash.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Center the splash screen window on the screen using style commands
        self.setStyleSheet('''
           QSplashScreen {
               background-color: rgba(1,42,89,1);
               background-position: center;
               border-radius: 15px;
           }
       ''')

        # Customize the progress bar
        self.progressBar.setStyleSheet('''
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                background-color: #f0f0f0;
                text-align: center;
                position: center;
            }

            QProgressBar::chunk {
                background-color: #52b29f;  
                width: 8px;
            }
        ''')

    def progress(self):
        for i in range(100):
            time.sleep(0.0125)
            self.progressBar.setValue(i)
