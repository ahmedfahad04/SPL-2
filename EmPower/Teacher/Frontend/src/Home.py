'''
    From now, when you want to add a new page, you can follow the same steps:
    1. Create a new class for the new page (in Frontend.src)
    2. Create a new function for the new page (in main.py [e.g. student_info_page()])
    3. Initialize the ui object of the new page (in main.py [e.g. self.std_window = ui_student.Ui_MainWindow()])
    4. Connect the button call to the new page (in main.py [e.g. self.std_window.btn_add_new_student.clicked.connect(std_methods.add_new_row)])
    5. Pass the ui object of the new page to the new class (in main.py [e.g. std_methods = Student_Window(self.std_window)])
    6. Implement the functions of the new class (in Frontend.src) [remember to pass reference of current parent obj, otherwise widget window might not be shown]
'''

from Frontend.Teacher_UI import ui_home_page
from Frontend.src.Document_Formatter import *
from Frontend.src.Student_Window import Student_Window
from Frontend.src.Lesson_Window import Lesson_Window

class Home(QMainWindow):  # Home extends QMainWindow

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.home_page()
        
    def home_page(self):
        
        # load & set up the HOME page
        self.home = ui_home_page.Ui_MainWindow()
        self.home.setupUi(self)
        
        # set window icon and title
        # TODO: Show the window at the middle of the screen
        # self.setGeometry(480, 270, 0, 0)
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("শিখবে সবাই")
        set_drop_shadow(self.home.home_btn_student)
        set_drop_shadow(self.home.home_btn_lesson)
        set_drop_shadow(self.home.home_btn_quiz)
        set_drop_shadow(self.home.home_btn_progress)
        set_drop_shadow(self.home.home_btn_settings)
        
        self.home.stackedWidget.setCurrentWidget(self.home.home_page)
        self.home.home_btn_student.clicked.connect(self.student_page)
        self.home.home_btn_lesson.clicked.connect(self.lesson_page)
        
    def student_page(self):
        
        # instance of student window class
        self.student_window = Student_Window(self.home)
        
        # set window icon and title
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("শিক্ষার্থীর তথ্য")

        # reload table data
        self.student_window.reload_table()
        align_elements(self.home.std_tableWidget)

        # Navigate between windows
        self.home.stackedWidget.setCurrentWidget(self.home.student_page)
        self.home.std_btn_back_to_home.clicked.connect(self.home_page)
        
        # Connecting Student window buttons
        self.home.std_btn_add_student.clicked.connect(self.student_window.add_new_row)
        self.home.std_btn_update_info.clicked.connect(self.student_window.update_student_info)
        self.home.std_btn_remove_student.clicked.connect(self.student_window.remove_rows)
                
    def lesson_page(self):
        
        # instance of lesson window class
        self.lesson_window = Lesson_Window(self.home)
        
        # set window icon and title
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("শিক্ষার্থীর পাঠসমূহ")
        
        # Navigate between windows
        self.home.mediaStackWidget.setCurrentWidget(self.home.image_page)
        self.home.stackedWidget.setCurrentWidget(self.home.lesson_page)
        self.home.lsn_btn_back_to_home.clicked.connect(self.home_page)
                
        # Connecting Lesson window buttons
        self.home.lsn_btn_add_lessons.clicked.connect(self.lesson_window.create_lesson)
        self.home.lsn_cmb_category.currentIndexChanged.connect(self.lesson_window.on_category_changed)
        self.home.lsn_cmb_lessons.currentIndexChanged.connect(self.lesson_window.on_lesson_changed)
        