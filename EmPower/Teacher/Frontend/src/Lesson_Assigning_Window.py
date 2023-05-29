from Frontend.src.Document_Formatter import *
from Backend.Database.lesson_db import lesson_data as ld
from Backend.Database.lesson_assigning_db import lesson_assiging_data as lad
from Backend.Database.student_db import student_data as sd
from Frontend.Teacher_UI import ui_assign_lesson
import datetime


class Lesson_Assigning_Window(QMainWindow):  # Home extends QMainWindow

    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()

        # window
        self.lesson_assinging_window = ui_object
        self.form = None
        self.table_data = None
        self.rows = None
        self.columns = None
        
        # table property
        self.lesson_assinging_window.lsn_table_assigning_lessons.setEditTriggers(QAbstractItemView.NoEditTriggers)
        

        self.populate_student_list()
        self.populate_lesson_assigning_table()

    def populate_student_list(self):
        
        # clear the list before populating
        self.lesson_assinging_window.lsn_list_students.clear()

        student_details = sd().load_table()
        data = [(x[0], x[1]) for x in student_details]

        self.lesson_assinging_window.lsn_list_students.addItems(
            [str(x[0])+'. '+x[1] for x in data])
        print(data)
        
    def populate_lesson_assigning_table(self):
        
        # clear previous data before populating
        self.lesson_assinging_window.lsn_table_assigning_lessons.clearContents()
        self.lesson_assinging_window.lsn_table_assigning_lessons.setRowCount(0)
        
        self.table_data = lad().load_table()
        self.rows = len(self.table_data)
        self.columns = self.lesson_assinging_window.lsn_table_assigning_lessons.columnCount()
        print(self.rows, self.columns, self.table_data)
        
        for row in range(self.rows):
            self.lesson_assinging_window.lsn_table_assigning_lessons.insertRow(row)
            for col in range(self.columns):
                print(row, col, self.table_data[row][col])
                self.lesson_assinging_window.lsn_table_assigning_lessons.setItem(row, col, QTableWidgetItem(str(self.table_data[row][col])))
        
    def assign_lesson(self):
                
        lad().create_table()

        # get the selected student name and id
        model = self.lesson_assinging_window.lsn_list_students.model()
        index = self.lesson_assinging_window.lsn_list_students.currentIndex()
        print(model.data(index))

        # show warning if student name is not selected
        if model.data(index) is None:
            show_warning_message(
                "সতর্কতা", "বাম পাশে অবস্থিত শিক্ষার্থীর তালিকা থেকে শিক্ষার্থী নির্বাচন করে এরপর বাটনে প্রেস করুন")
            return

        std_id, std_name = model.data(index).split('. ')

        # load & set up the Student Add Info page [must use self.custom_widget else it will be destroyed as soon as the function ends]
        self.custom_widget = QWidget()
        self.form = ui_assign_lesson.Ui_Form()
        self.form.setupUi(self.custom_widget)
        self.custom_widget.setWindowModality(Qt.ApplicationModal)
        self.custom_widget.show()
        
        self.form.lsn_cmb_lesson_list.clear()

        # set window icon and title
        self.custom_widget.setWindowIcon(
            QIcon("../Teacher/Frontend/Images/primary_logo.png"))
        self.custom_widget.setWindowTitle("পাঠ নির্ধারণ")

        # set the student name and id in the form
        self.form.lsn_edit_student_id.setText(std_id)
        self.form.lsn_edit_student_name.setText(std_name)

        # get lesson data from table
        lesson_details = ld().load_table()
        print("Detials: ", lesson_details)
        data = [str(x[1]).split('/')[-1] for x in lesson_details]
        self.form.lsn_cmb_lesson_list.addItems(data)

        # connect the buttons
        self.form.lsn_btn_assign_lsn_to_std.clicked.connect(self.done_assigning_lesson)

    def done_assigning_lesson(self):
        
         # get data from the form
        get_lesson_id = self.form.lsn_cmb_lesson_list.currentText()
        print("ID: ", get_lesson_id)
        
        if get_lesson_id == '':
            show_warning_message("পাঠ নং নির্বাচন", "পাঠ নং নির্বাচন করুন!")
            return

        warning = show_confirmation_message("নিশ্চিতকরণ", "আপনি কি নিশ্চিত যে আপনি পাঠ নির্ধারণ করতে চান?")
        
         
        if warning:
                           
            get_student_id = self.form.lsn_edit_student_id.text()
            get_student_name = self.form.lsn_edit_student_name.text()
            assigning_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = [get_student_id, get_student_name, get_lesson_id, assigning_time]
            
            # insert data into the table
            lad().add_entry(data)
            
            # hide the form
            self.custom_widget.hide()
            # get the details of lesson assigning table
            rows = self.lesson_assinging_window.lsn_table_assigning_lessons.rowCount()
            columns = self.lesson_assinging_window.lsn_table_assigning_lessons.columnCount()
            
            # add new row
            self.lesson_assinging_window.lsn_table_assigning_lessons.insertRow(rows)
            
            for col in range(columns):
                print(col, ' ', data[col])
                self.lesson_assinging_window.lsn_table_assigning_lessons.setItem(
                    rows, col, QTableWidgetItem(str(data[col])))
                
        else:
            
            print("Warning false!!")
