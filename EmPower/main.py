from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from ui_home import Ui_MainWindow
from ui_sudent import Ui_StudentInfo


class MainWindow(QMainWindow):        # Home extends QMainWindow
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.home_page()

    def home_page(self):
        """
            This function configures the property of the home page.
        """
        
        # load & set up the HOME page
        self.home = Ui_MainWindow()
        self.home.setupUi(self)

        # set window icon and title
        self.setWindowIcon(QIcon("UI\only_logo.png"))
        self.setWindowTitle("শিখবে সবাই")
        
        # apply drop shadow effect to the buttons
        self.setDropShadowEffect(self.home.btn_student)
        self.setDropShadowEffect(self.home.btn_lesson)
        self.setDropShadowEffect(self.home.btn_quiz)
        self.setDropShadowEffect(self.home.btn_progress)
        self.setDropShadowEffect(self.home.btn_settings)

        # connect the buttons
        self.home.btn_student.clicked.connect(self.student_info_page)
        
    def student_info_page(self):
        """
            This function configures the property of the Student Info page.
        """
        
        # load & set up the Student Info page
        self.std_window = Ui_StudentInfo()
        self.std_window.setupUi(self)
        
        # set window icon and title
        self.setWindowIcon(QIcon("UI\only_logo.png"))
        self.setWindowTitle("শিক্ষার্থীর তথ্য")
        
        # connect the buttons
        self.std_window.btn_back_to_home.clicked.connect(self.home_page)
        
        # ==> Table Modification
        
        # align the cell value to the center
        for row in range(self.std_window.tableWidget.rowCount()):
            for column in range(self.std_window.tableWidget.columnCount()):
                item = self.std_window.tableWidget.item(row, column)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)

        # dynamically add/remove a row into the table
        self.std_window.btn_add_new_student.clicked.connect(lambda: self.addNewRow(self.std_window))
        self.std_window.btn_remove_student.clicked.connect(lambda: self.removeRows(self.std_window))
        
        
    # ==> Helper functions: Apply drop shadow effect to the buttons
    def setDropShadowEffect(self, ui_object):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(3)
        shadow.setYOffset(5)
        shadow.setColor(QColor(0, 0, 0, 100))
        ui_object.setGraphicsEffect(shadow)

    # ==> Helper functions: Add a new row into the table
    def addNewRow(self, ui_object):
        current_row_no = ui_object.tableWidget.rowCount()
        ui_object.tableWidget.insertRow(current_row_no)
        
    # ==> Helper functions: Remove a row from the table
    def removeRows(self, ui_object):
        current_row_no = ui_object.tableWidget.currentRow()
        ui_object.tableWidget.removeRow(current_row_no)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
