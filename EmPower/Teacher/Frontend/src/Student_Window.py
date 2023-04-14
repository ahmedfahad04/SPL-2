from Frontend.Teacher_UI import ui_add_student
from Backend.Database.student_db import student_data as dm
from Frontend.src.Document_Formatter import *


class Student_Window(QWidget):  # Home extends QMainWindow

    def __init__(self, ui_object):
        super(QWidget, self).__init__()

        self.std_window = ui_object

    # ==> Helper functions: Add a new row into the table
    def add_new_row(self):
        
        print("Hello")

        # load & set up the Student Add Info page
        custom_form = QWidget()
        form = ui_add_student.Ui_Form()
        form.setupUi(custom_form)
        custom_form.setWindowModality(Qt.ApplicationModal)
        custom_form.show()

        # set window icon and title
        custom_form.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        custom_form.setWindowTitle("তথ্য যুক্তকরণ উইন্ডো")

        # connect the buttons
        form.btn_submit.clicked.connect(lambda: self.get_form_data(custom_form, form, -1))

    # ==> Helper functions: Remove a row from the table
    def remove_rows(self):

        try:
            current_row = self.std_window.std_tableWidget.currentRow()

            # TODO: show warning box
            if current_row == -1:
                print(
                    'Please select a row first, then press delete button [show warning box].')

            # remove from database
            student_id = self.std_window.std_tableWidget.item(current_row, 0).text()
            dm().delete_entry(student_id)

            # remove from pyqt table
            self.std_window.std_tableWidget.removeRow(current_row)

        except Exception as e:
            print("Error: ", e)

    # ==> Helper functions: Reload the table
    def reload_table(self):

        # reload data from database
        table_data = dm().load_table()
        rows = len(table_data)
        columns = self.std_window.std_tableWidget.columnCount()
        self.std_window.std_tableWidget.setRowCount(rows)

        # store the reloaded value into the PyQt_UI
        for row in range(rows):
            for col in range(columns):
                self.std_window.std_tableWidget.setItem(
                    row, col, QTableWidgetItem(str(table_data[row][col])))

    # ==> Helper function: update user data
    def update_student_info(self):
        
        # TODO: need to check duplicate id number or entry of teacher

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
            current_row = self.std_window.std_tableWidget.currentRow()
            columns = self.std_window.std_tableWidget.columnCount()

            # fetch the data of that row
            for cell in range(columns):
                value = self.std_window.std_tableWidget.item(
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
                    form.input_address.setText(value)
                elif cell == 4:
                    form.input_guardian.setText(value)
                elif cell == 5:
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
        total_rows = self.std_window.std_tableWidget.rowCount()
        total_cols = self.std_window.std_tableWidget.columnCount()

        # get the data from the form
        self.std_id = obj.input_id.text()
        self.name = obj.input_name.text()
        self.age = obj.input_age.text()
        self.address = obj.input_address.text()
        self.guardian = obj.input_guardian.text()
        self.phone = obj.input_phone.text()

        # create a blank row to store the values
        if row_id == -1:

            # TODO: Show warning box to add new entry
            print("Adding new rows...")

            # add new row
            self.std_window.std_tableWidget.insertRow(total_rows)
            data = [self.std_id, self.name, self.age, self.address,self.guardian, self.phone]

            # set the values into the new row
            for i in range(total_cols):
                self.std_window.std_tableWidget.setItem(
                    total_rows, i, QTableWidgetItem(data[i]))

            # insert the data into the database
            dm().add_entry(data)

        else:

            # TODO: Show warning box to update existing entry
            print("Updating existing rows...")

            # update row
            total_rows = row_id
            data = [self.std_id, self.name, self.age, self.address,self.guardian, self.phone, old_id]

            # set the values into the new row
            for i in range(total_cols):
                self.std_window.std_tableWidget.setItem(
                    total_rows, i, QTableWidgetItem(data[i]))

            dm().update_entry(data)

        # align the elements after inserting new row
        align_elements(self.std_window.std_tableWidget)

        parent_obj.close()
