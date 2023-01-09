# compile the pyrcc and pyuic sequentially

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui_sidebar import Ui_MainWindow
from imgWidget import Ui_Form
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        # load the ui file class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load image file content
        self.form = QWidget()
        self.content = Ui_Form()
        self.content.setupUi(self.form)

        # setup Button content
        self.widgetBtn = self.content.pushButton
        self.widgetBtn.dragStartPos = QPoint()
        self.widgetBtn.dragging = False

        # set current widget on opening screen
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.icon_with_lbl_widget.hide()

        # following lines linked the button with relevant pages of stackedWidget
        self.ui.home_large_btn.clicked.connect(self.on_home_large_btn_toogled)
        self.ui.home_small_btn.clicked.connect(self.on_home_small_btn_toogled)

        self.ui.files_large_btn.clicked.connect(self.on_files_large_btn_toogled)
        self.ui.files_small_btn.clicked.connect(self.on_files_small_btn_toogled)

        self.ui.people_small_btn.clicked.connect(self.on_people_small_btn_toogled)
        self.ui.people_large_btn.clicked.connect(self.on_people_large_btn_toogled)

        self.ui.records_small_btn.clicked.connect(self.on_records_small_btn_toogled)
        self.ui.records_large_btn.clicked.connect(self.on_records_large_btn_toogled)

        # permit the widget to apply drag and drop widget
        self.setAcceptDrops(True)

    # applying drag and drop effect
    # this function work when we Press mouse button to start dragging
    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    # this function works when we release the button to finally place the object
    def dropEvent(self, event):
        position = event.pos()

        self.content.pushButton.move(position)
        event.accept()

    def on_home_small_btn_toogled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_home_large_btn_toogled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_files_large_btn_toogled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_files_small_btn_toogled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_people_small_btn_toogled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_people_large_btn_toogled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_records_large_btn_toogled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_records_small_btn_toogled(self):
        self.ui.stackedWidget.setCurrentIndex(3)


if __name__ == '__main__':
    app = QApplication([])

    with open('style.qss', 'r') as f:
        style_sheet = f.read()

    app.setStyleSheet(style_sheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
