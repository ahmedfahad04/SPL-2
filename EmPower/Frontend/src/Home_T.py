'''
    From now, when you want to add a new page, you can follow the same steps:
    1. Create a new class for the new page (in Frontend.src)
    2. Create a new function for the new page (in main.py [e.g. student_info_page()])
    3. Initialize the ui object of the new page (in main.py [e.g. self.std_window = ui_student.Ui_MainWindow()])
    4. Connect the button call to the new page (in main.py [e.g. self.std_window.btn_add_new_student.clicked.connect(std_methods.add_new_row)])
    5. Pass the ui object of the new page to the new class (in main.py [e.g. std_methods = Student_Window(self.std_window)])
    6. Implement the functions of the new class (in Frontend.src)
'''

import sys
from Frontend.src.Student_info_T import Student_Window
from Frontend.Teacher_UI import ui_student, ui_home
from document_formatter import *


class Teacher_Home(QMainWindow):  # Home extends QMainWindow

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.home = None
        self.std_window = None
        self.home_page()

    def home_page(self):
        """
            This function configures the property of the home page.
        """

        # load & set up the HOME page
        self.home = ui_home.Ui_MainWindow()
        self.home.setupUi(self) 

        # set window icon and title
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("শিখবে সবাই")

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
        std_methods = Student_Window(self.std_window)

        # set window icon and title
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("শিক্ষার্থীর তথ্য")

        # ==> Connect the buttons
        self.std_window.btn_back_to_home.clicked.connect(self.home_page)
        self.std_window.btn_remove_student.clicked.connect(lambda: std_methods.remove_rows(self.std_window))
        self.std_window.btn_add_new_student.clicked.connect(std_methods.add_new_row)
        self.std_window.btn_update_student_info.clicked.connect(lambda: std_methods.update_student_info(self.std_window))
