# compile the pyrcc and pyuic sequentially

from PyQt5.QtWidgets import *
from sidebar import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.icon_with_lbl_widget.hide()


if __name__ == '__main__':
    app = QApplication([])

    with open('style.qss', 'r') as f:
        style_sheet = f.read()

    app.setStyleSheet(style_sheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
