from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from ui_home import Ui_MainWindow


class MainWindow(QMainWindow):        # Home extends QMainWindow
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.home_page()

    def home_page(self):
        """
            This function configures the property of the home page.
        """
        
        # load & setup the HOME page
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set window icon and title
        self.setWindowIcon(QIcon("UI\only_logo.png"))
        self.setWindowTitle("শিখবে সবাই")
        
        # apply drop shadow effect to the buttons
        self.setDropShadowEffect(self.ui.btn_student)
        self.setDropShadowEffect(self.ui.btn_lesson)
        self.setDropShadowEffect(self.ui.btn_quiz)
        self.setDropShadowEffect(self.ui.btn_progress)
        self.setDropShadowEffect(self.ui.btn_settings)

        # connect the buttons
        self.ui.btn_lesson.clicked.connect(lambda: print("Lesson"))
        
    def setDropShadowEffect(self, ui_object):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(3)
        shadow.setYOffset(5)
        shadow.setColor(QColor(0, 0, 0, 100))
        ui_object.setGraphicsEffect(shadow)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
