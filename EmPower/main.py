from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from ui_home import Ui_MainWindow
from ui_student import Ui_StudentInfo
from ui_add_student import Ui_Form
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
        
        # ==> Student Page Window Modification

        # load & set up the Student Info page
        self.std_window = Ui_StudentInfo()
        self.std_window.setupUi(self)

        # set window icon and title
        self.setWindowIcon(QIcon("UI\only_logo.png"))
        self.setWindowTitle("শিক্ষার্থীর তথ্য")
       
        # ==> Database Operations

        # Load info from the database
        self.reload_table()
        self.align_elements()

        # ==> Connect the buttons
        
        self.std_window.btn_back_to_home.clicked.connect(self.home_page)
        self.std_window.btn_remove_student.clicked.connect(lambda: self.remove_rows(self.std_window))
        self.std_window.btn_add_new_student.clicked.connect(self.add_new_row)


    # ==> Helper functions: Align the elements in the table
    def align_elements(self):
        rows = self.std_window.tableWidget.rowCount()
        columns = self.std_window.tableWidget.columnCount()
        
        for row in range(rows):
            for column in range(columns):
                item = self.std_window.tableWidget.item(row, column)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)   

    # ==> Helper functions: Apply drop shadow effect to the buttons
    def set_drop_shadow(self, ui_object):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(3)
        shadow.setYOffset(5)
        shadow.setColor(QColor(0, 0, 0, 100))
        ui_object.setGraphicsEffect(shadow)

    # ==> Helper functions: Add a new row into the table
    def add_new_row(self):
        
        # load & set up the Student Add Info page
        self.custom_form = QWidget()
        self.form = Ui_Form()
        self.form.setupUi(self.custom_form)
        self.custom_form.show()
        
        # set window icon and title
        self.custom_form.setWindowIcon(QIcon("UI\only_logo.png"))
        self.custom_form.setWindowTitle("শিক্ষার্থীর তথ্য যোগ করুন")
                
        # connect the buttons
        self.form.btn_submit.clicked.connect(lambda: self.get_form_data(self.custom_form, self.form)) 

    # ==> Helper functions: Remove a row from the table
    def remove_rows(self, ui_object):
                
        # remove from pyqt table
        current_row_no = ui_object.tableWidget.currentRow()
        ui_object.tableWidget.removeRow(current_row_no)
        print("current: ",current_row_no)
        
        # remove from database
        try:
            std_id = ui_object.tableWidget.item(current_row_no, 0).text()            
            dm().delete_student_entry(std_id)
        
        except Exception as e:
            print("Error: ", e)
            pass

    # ==> Helper functions: Reload the table
    def reload_table(self):
        table_data = dm().load_student_entry()
        rows = len(table_data)
        columns = self.std_window.tableWidget.columnCount()
        self.std_window.tableWidget.setRowCount(rows)
               
        for row in range(rows):
            for col in range(columns):
                self.std_window.tableWidget.setItem(
                    row, col, QTableWidgetItem(str(table_data[row][col])))
      
    # ==> Helper functions: get user entered data from the form
    def get_form_data(self, parent_obj, obj):
        
        # calculate current row and column number
        current_row = self.std_window.tableWidget.rowCount()
        current_col = self.std_window.tableWidget.columnCount()
        
        # create a blank row to store the values
        self.std_window.tableWidget.insertRow(current_row)
        
        # get the data from the form
        id = obj.input_id.text()
        name = obj.input_name.text()
        age = obj.input_age.text()
        guardian = obj.input_guardian.text()
        phone = obj.input_phone.text()
        data = [id, name, age, guardian, phone]
                       
        # set the values into the new row
        for i in range(current_col):
            print("ROW: ", current_row, "COL: ", i)
            self.std_window.tableWidget.setItem(current_row, i, QTableWidgetItem(data[i]))
            
        # insert the data into the database
        dm().add_student_entry(data)
        
        parent_obj.close()
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
