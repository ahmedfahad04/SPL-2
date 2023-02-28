from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from Frontend.Teacher_UI import ui_add_student, ui_student
from Backend.connectDB import Database_Manager as dm
from document_formatter import *


class Student_Window(QMainWindow):  # Home extends QMainWindow

    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()
        
        self.std_window = ui_object

        # ==> Database Operations
        # Load info from the database
        self.reload_table()
        align_elements(self.std_window)

    # ==> Helper functions: Add a new row into the table
    def add_new_row(self):

        # load & set up the Student Add Info page
        custom_form = QWidget()
        form = ui_add_student.Ui_Form()
        form.setupUi(custom_form)
        custom_form.show()

        # set window icon and title
        custom_form.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        custom_form.setWindowTitle("তথ্য যুক্তকরণ উইন্ডো")

        # connect the buttons
        form.btn_submit.clicked.connect(lambda: self.get_form_data(custom_form, form, -1))

    # ==> Helper functions: Remove a row from the table
    def remove_rows(self, ui_object):

        try:
            current_row = ui_object.tableWidget.currentRow()

            # TODO: show warning box
            if current_row == -1:
                print(
                    'Please select a row first, then press delete button [show warning box].')

            # remove from database
            student_id = ui_object.tableWidget.item(current_row, 0).text()
            dm().delete_student_entry(student_id)

            # remove from pyqt table
            ui_object.tableWidget.removeRow(current_row)

        except Exception as e:
            print("Error: ", e)

    # ==> Helper functions: Reload the table
    def reload_table(self):

        # reload data from database
        table_data = dm().load_student_entry()
        rows = len(table_data)
        columns = self.std_window.tableWidget.columnCount()
        self.std_window.tableWidget.setRowCount(rows)

        # store the reloaded value into the PyQt_UI
        for row in range(rows):
            for col in range(columns):
                self.std_window.tableWidget.setItem(
                    row, col, QTableWidgetItem(str(table_data[row][col])))

    # ==> Helper function: update user data
    def update_student_info(self, ui_object):

        # load & set up the Student Add Info page
        custom_form = QWidget()
        form = ui_add_student.Ui_Form()
        form.setupUi(custom_form)

        # set window icon and title
        custom_form.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        custom_form.setWindowTitle("তথ্য পরিবর্তনের উইন্ডো")

        # change the heading and submit button text
        form.lbl_heading.setText("শিক্ষার্থীর তথ্য আপডেট করুন")
        form.btn_submit.setText("আপডেট করুন")
        form.btn_submit.setShortcut("Return")

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
                    form.input_id.setText(value)
                elif cell == 1:
                    form.input_name.setText(value)
                elif cell == 2:
                    form.input_age.setText(value)
                elif cell == 3:
                    form.input_guardian.setText(value)
                elif cell == 4:
                    form.input_phone.setText(value)

            # show the update Form
            custom_form.show()

            # edit the data & press update button
            form.btn_submit.clicked.connect(lambda: self.get_form_data(
                custom_form, form, current_row, previous_id))

        except Exception as e:

            print("[Error] Student Info table UPDATE Failed - ", e)
            return

    # ==> Helper functions: get user entered data from the form
    def get_form_data(self, parent_obj, obj, row_id, old_id=None):

        # calculate current row and column number
        total_rows = self.std_window.tableWidget.rowCount()
        total_cols = self.std_window.tableWidget.columnCount()

        # get the data from the form
        self.std_id = obj.input_id.text()
        self.name = obj.input_name.text()
        self.age = obj.input_age.text()
        self.guardian = obj.input_guardian.text()
        self.phone = obj.input_phone.text()

        # create a blank row to store the values
        if row_id == -1:

            # TODO: Show warning box to add new entry
            print("Adding new rows...")

            # add new row
            self.std_window.tableWidget.insertRow(total_rows)
            data = [self.std_id, self.name, self.age, self.guardian, self.phone]

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
            data = [self.std_id, self.name, self.age, self.guardian, self.phone, old_id]

            # set the values into the new row
            for i in range(total_cols):
                self.std_window.tableWidget.setItem(
                    total_rows, i, QTableWidgetItem(data[i]))

            dm().update_student_entry(data)

        # align the elements after inserting new row
        align_elements(self.std_window)

        parent_obj.close()

