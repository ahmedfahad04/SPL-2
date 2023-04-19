from Frontend.src.Document_Formatter import *
from Backend.Database.module_db import module_data as ld
from Backend.Database.student_db import student_data as sd 
from Frontend.Teacher_UI import ui_assign_lesson
import os
import json
import shutil


class Lesson_Assigning_Window(QMainWindow):  # Home extends QMainWindow

    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()

        # window
        self.lesson_assinging_window = ui_object
        self.form = None
        
        self.populate_student_list()
        
    def populate_student_list(self):
        
        student_details = sd().load_table()
        data = [(x[0], x[1]) for x in student_details]
        
        self.lesson_assinging_window.lsn_list_students.addItems([str(x[0])+'. '+x[1] for x in data])
        print(data)
        
    def assign_lesson(self):
        
        # get the selected student name and id
        model = self.lesson_assinging_window.lsn_list_students.model()
        index = self.lesson_assinging_window.lsn_list_students.currentIndex()
        print(model.data(index))
        
        if model.data(index) is None:
            show_warning_message("সতর্কতা", "শিক্ষার্থী নির্বাচন করে এরপর বাটনে প্রেস করুন")
            return 
        
        std_id, std_name = model.data(index).split('. ')
        
        # load & set up the Student Add Info page [must use self.custom_form else it will be destroyed as soon as the function ends]
        self.custom_form = QWidget()
        self.form = ui_assign_lesson.Ui_Form()
        self.form.setupUi(self.custom_form)
        self.custom_form.setWindowModality(Qt.ApplicationModal)
        self.custom_form.show()
        
        # set window icon and title
        self.custom_form.setWindowIcon(
            QIcon("../Teacher/Frontend/Images/primary_logo.png"))
        self.custom_form.setWindowTitle("পাঠ নির্ধারণ")
    
        # set the student name and id in the form
        self.form.lsn_edit_student_id.setText(std_id)
        self.form.lsn_edit_student_name.setText(std_name)
        
        