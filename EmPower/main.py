from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from ui_home import Ui_MainWindow
import ui_student
import ui_add_student
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
        self.setWindowIcon(QIcon("UI\only_logo_2.png"))
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
        self.std_window = ui_student.Ui_MainWindow()
        self.std_window.setupUi(self)

        # set window icon and title
        self.setWindowIcon(QIcon("UI\only_logo_2.png"))
        self.setWindowTitle("শিক্ষার্থীর তথ্য")

        # ==> Database Operations

        # Load info from the database
        self.reload_table()
        self.align_elements()

        # ==> Connect the buttons

        self.std_window.btn_back_to_home.clicked.connect(self.home_page)
        self.std_window.btn_remove_student.clicked.connect(
            lambda: self.remove_rows(self.std_window))
        self.std_window.btn_add_new_student.clicked.connect(self.add_new_row)
        self.std_window.btn_update_student_info.clicked.connect(
            lambda: self.update_student_info(self.std_window))

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
        shadow.setXOffset(5)
        shadow.setYOffset(7)
        shadow.setColor(QColor(255, 255, 255, 55))
        ui_object.setGraphicsEffect(shadow)

    # ==> Helper functions: Add a new row into the table
    def add_new_row(self):

        # load & set up the Student Add Info page
        self.custom_form = QWidget()
        self.form = ui_add_student.Ui_Form()
        self.form.setupUi(self.custom_form)
        self.custom_form.show()

        # set window icon and title
        self.custom_form.setWindowIcon(QIcon("UI\only_logo_2.png"))
        self.custom_form.setWindowTitle("তথ্য যুক্তকরণ উইন্ডো")

        # connect the buttons
        self.form.btn_submit.clicked.connect(
            lambda: self.get_form_data(self.custom_form, self.form, -1))

    # ==> Helper functions: Remove a row from the table
    def remove_rows(self, ui_object):

        try:
            current_row = ui_object.tableWidget.currentRow()

            # TODO: show warning box
            if current_row == -1:
                print(
                    'Please select a row first, then press delete button [show warning box].')

            # remove from database
            std_id = ui_object.tableWidget.item(current_row, 0).text()
            dm().delete_student_entry(std_id)

            # remove from pyqt table
            ui_object.tableWidget.removeRow(current_row)

        except Exception as e:
            print("Error: ", e)

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

    # ==> Helper function: update user data
    def update_student_info(self, ui_object):

        # load & set up the Student Add Info page
        self.custom_form = QWidget()
        self.form = ui_add_student.Ui_Form()
        self.form.setupUi(self.custom_form)

        # set window icon and title
        self.custom_form.setWindowIcon(QIcon("UI\only_logo_2.png"))
        self.custom_form.setWindowTitle("তথ্য পরিবর্তনের উইন্ডো")

        # change the heading and submit button text
        self.form.lbl_heading.setText("শিক্ষার্থীর তথ্য আপডেট করুন")
        self.form.btn_submit.setText("আপডেট করুন")
        self.form.btn_submit.setShortcut("Return")

        try:
            # get the selected row id
            current_row = ui_object.tableWidget.currentRow()
            columns = ui_object.tableWidget.columnCount()

            # fetch the data of that row
            for cell in range(columns):
                value = self.std_window.tableWidget.item(
                    current_row, cell).text()

                # set the data into the form
                if cell == 0:
                    previous_id = value
                    self.form.input_id.setText(value)
                elif cell == 1:
                    self.form.input_name.setText(value)
                elif cell == 2:
                    self.form.input_age.setText(value)
                elif cell == 3:
                    self.form.input_guardian.setText(value)
                elif cell == 4:
                    self.form.input_phone.setText(value)

            # show the update Form
            self.custom_form.show()

            # edit the data & press update button
            self.form.btn_submit.clicked.connect(lambda: self.get_form_data(
                self.custom_form, self.form, current_row, previous_id))

        except Exception as e:

            print("[Error] Student Info table UPDATE Failed - ", e)
            return

    # ==> Helper functions: get user entered data from the form
    def get_form_data(self, parent_obj, obj, row_id, old_id=None):

        # calculate current row and column number
        total_rows = self.std_window.tableWidget.rowCount()
        total_cols = self.std_window.tableWidget.columnCount()

        # get the data from the form
        id = obj.input_id.text()
        name = obj.input_name.text()
        age = obj.input_age.text()
        guardian = obj.input_guardian.text()
        phone = obj.input_phone.text()

        # create a blank row to store the values
        if row_id == -1:

            # TODO: Show warning box to add new entry
            print("Adding new rows...")

            # add new row
            self.std_window.tableWidget.insertRow(total_rows)
            data = [id, name, age, guardian, phone]

            # set the values into the new row
            for i in range(total_cols):
                self.std_window.tableWidget.setItem(
                    total_rows, i, QTableWidgetItem(data[i]))

            # insert the data into the database
            dm().add_student_entry(data)

        else:

            # TODO: Show warning box to update existing entry
            print("Updating existing rows...")

            # update row
            total_rows = row_id
            data = [id, name, age, guardian, phone, old_id]

            # set the values into the new row
            for i in range(total_cols):
                self.std_window.tableWidget.setItem(
                    total_rows, i, QTableWidgetItem(data[i]))

            dm().update_student_entry(data)

        # align the elements after inserting new row
        self.align_elements()

        parent_obj.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
