from PyQt5.QtWidgets import *
from Frontend.src.Home import Home
from Frontend.src.Document_Formatter import *
from Frontend.src.SplashScreen import SplashScreen
import sys 

if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash = SplashScreen()

    # Center the splash screen window on the screen
    splash_width = splash.width()
    splash_height = splash.height()
    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    x = (screen_geometry.width() - splash_width) // 2
    y = (screen_geometry.height() - splash_height) // 2
    splash.move(x, y)

    # now show the splash window
    splash.show()
    splash.progress()

    window = Home()
    window.showMaximized()
    window.show()

    splash.finish(window)

    sys.exit(app.exec_()) 

