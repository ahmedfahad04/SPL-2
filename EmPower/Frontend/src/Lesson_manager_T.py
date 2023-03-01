from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from Frontend.Teacher_UI import ui_add_lesson
from Backend.connectDB import Database_Manager as dm
from document_formatter import *


class Lesson_manager(QMainWindow):  # Home extends QMainWindow

    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()
        
        self.lesson_manager = ui_object
        print("Creating a lesson ...")
        
        
    def create_new_lesson(self):
        
        print("Creating a lesson ...")
        
        # load & set up the Student Add Info page
        custom_form = QWidget()
        form = ui_add_lesson.Ui_Form()
        form.setupUi(custom_form)
        custom_form.show()
        
        # set window icon and title
        custom_form.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        custom_form.setWindowTitle("লেসন তৈরি করুন") 
        
        
    
