from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from ui_home import Ui_MainWindow
from ui_sudent import Ui_StudentInfo
from connectDB import Database_Manager as dm


class MainWindow(QMainWindow):  # Home extends QMainWindow
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
        self.set_drop_shadow(self.home.btn_student)
        self.set_drop_shadow(self.home.btn_lesson)
        self.set_drop_shadow(self.home.btn_quiz)
        self.set_drop_shadow(self.home.btn_progress)
        self.set_drop_shadow(self.home.btn_settings)

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

        
        # ==> Table Modification


        rows = self.std_window.tableWidget.rowCount()
        columns = self.std_window.tableWidget.columnCount()

        # dynamically add/remove a row into the table
        self.std_window.btn_add_new_student.clicked.connect(
            lambda: self.add_new_row(self.std_window))

       
        # ==> Database Operations


        # Store info into the database
        for row in range(rows):
            each_row = []
            for column in range(columns):
                item = self.std_window.tableWidget.item(row, column)
                each_row.append(item.text().strip())

            # add the row into the database
            dm().add_student_entry(each_row)
            

        # Load info from the database
        self.reload_table()

        # align the cell value to the center
        for row in range(rows):
            for column in range(columns):
                item = self.std_window.tableWidget.item(row, column)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)

        # connect the buttons
        self.std_window.btn_back_to_home.clicked.connect(self.home_page)
        self.std_window.btn_remove_student.clicked.connect(
            lambda: self.remove_rows(self.std_window))


    # ==> Helper functions: Apply drop shadow effect to the buttons
    def set_drop_shadow(self, ui_object):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(3)
        shadow.setYOffset(5)
        shadow.setColor(QColor(0, 0, 0, 100))
        ui_object.setGraphicsEffect(shadow)

    # ==> Helper functions: Add a new row into the table
    def add_new_row(self, ui_object):
        current_row_no = ui_object.tableWidget.rowCount()
        ui_object.tableWidget.insertRow(current_row_no)

    # ==> Helper functions: Remove a row from the table
    def remove_rows(self, ui_object):
        row = ui_object.tableWidget.currentIndex().row()
        std_id = ui_object.tableWidget.item(row, 0).text()
        
        current_row_no = ui_object.tableWidget.currentRow()
        ui_object.tableWidget.removeRow(current_row_no)

        dm().delete_student_entry(std_id)
        self.reload_table()

    # Reload the table
    def reload_table(self):
        table_data = dm().load_student_entry()
        rows = len(table_data)
        columns = self.std_window.tableWidget.columnCount()
        self.std_window.tableWidget.setRowCount(rows)

        print(rows, columns)
        
        for row in range(rows):
            for col in range(columns):
                self.std_window.tableWidget.setItem(
                    row, col, QTableWidgetItem(table_data[row][col]))
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
