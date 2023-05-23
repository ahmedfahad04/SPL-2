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
from Frontend.src.Task_Window import Task_Window
from Frontend.src.Lesson_Making_Wiindow import Lesson_Making_Window
from Frontend.src.Lesson_Assigning_Window import Lesson_Assigning_Window
from Backend.Database.module_db import module_data as md
from Backend.Database.lesson_db import lesson_data as ld
from Backend.Database.student_db import student_data as sd
from Backend.ScreenShot.ImageCapture import ImageCaptureWidget
import os
import shutil

class Home(QMainWindow):  # Home extends QMainWindow

    def __init__(self):
        super(QMainWindow, self).__init__()
        
        self.home = None
        self.sequence_image_count = 0

        self.home_page()
        
        
    def home_page(self):
        
        # load & set up the HOME page
        
        if self.home is None:
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
        set_drop_shadow(self.home.home_btn_lesson_assigns)
        
        # connect buttons
        self.home.stackedWidget.setCurrentWidget(self.home.home_page)
        self.home.home_btn_student.clicked.connect(self.student_page)
        self.home.home_btn_lesson.clicked.connect(self.lesson_page)
        self.home.home_btn_quiz.clicked.connect(self.task_page)
        self.home.home_btn_lesson_assigns.clicked.connect(self.lesson_assigning_page)
                         
    def student_page(self):
        
        # create table for student info
        sd().create_table()
        
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
        
        os.path.exists('Lessons') or os.mkdir('Lessons') 
        os.path.exists('Lessons/মডিউলসমূহ') or os.mkdir('Lessons/মডিউলসমূহ') 
        os.path.exists('Lessons/পাঠসমূহ') or os.mkdir('Lessons/পাঠসমূহ')
         
        # create table for lesson info
        md().create_table()
        
        # instance of lesson window class
        self.lesson_window = Lesson_Window(self.home)
        
        # set window icon and title
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("পাঠের মডিউলসমূহ") 
        
        # Navigate between windows
        self.home.mediaStackWidget.setCurrentWidget(self.home.image_page)
        self.home.stackedWidget.setCurrentWidget(self.home.lesson_page)
        
                
        # Connecting Lesson window buttons
        self.home.lsn_btn_add_lessons.clicked.connect(self.lesson_window.create_lesson)
        self.home.lsn_cmb_category.currentIndexChanged.connect(self.lesson_window.on_category_changed)
        self.home.lsn_cmb_lessons.currentIndexChanged.connect(self.lesson_window.on_lesson_changed)
        self.home.lsn_btn_reload_window.clicked.connect(self.home_page)
        self.home.lsn_btn_make_lesson.clicked.connect(self.lesson_making_page)
        self.home.lsn_btn_back_to_home.clicked.connect(self.home_page)
            
    def task_page(self):
        
        self.task_window = Task_Window(self.home)
        
        # Navigate between windows
        self.home.stackedWidget.setCurrentWidget(self.home.task_page)
        self.home.evalstackwidget.setCurrentWidget(self.home.matching_page)
        self.home.task_btn_back_to_home.clicked.connect(self.home_page)
        
        # Connecting Task window buttons
        # !need to move on Task Window Page
        self.home.task_btn_matching.clicked.connect(self.matching_page)
        self.home.task_btn_sequence.clicked.connect(self.sequence_page)
        self.home.task_btn_puzzle.clicked.connect(self.puzzle_page)
        self.home.task_puzzle_select_img_btn.clicked.connect(self.select_puzzle_image)
        self.home.task_puzzle_save_set_btn.clicked.connect(self.save_puzzle_set)
        self.home.task_puzzle_show_set_btn.clicked.connect(self.show_puzzle_set)
        self.home.task_seq_img_save_btn.clicked.connect(self.save_sequence_details)
               
    def on_label_clicked(self):
        
        show_confirmation_message("Level clicked", "Level clicked")
        
    def lesson_making_page(self):
        
        # create table for lesson info
        ld().create_table()
        
        # instance of lesson window class
        self.lesson_making_window = Lesson_Making_Window(self.home)
        
        # set window icon and title
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("পাঠ তৈরি করুন")
        
        # Navigate between windows
        self.home.stackedWidget.setCurrentWidget(self.home.lesson_making_page)
        self.home.lsn_btn_back_to_home_3.clicked.connect(self.home_page)
        
        # additional permission for that window widgets
        self.home.lsn_module_table_widget.setDragEnabled(True)
        self.home.lsn_module_table_widget.setDragDropMode(QAbstractItemView.DragOnly)        
        self.home.lsn_new_module_list_view.setAcceptDrops(True)
        self.home.lsn_new_module_list_view.setModel(QStandardItemModel(0, 1))
        
        # connect buttons
        self.home.lsn_btn_remove_module.clicked.connect(self.lesson_making_window.remove_list_item)
        self.home.lsn_btn_finish_add_module.clicked.connect(self.lesson_making_window.make_lesson)
        self.home.lsn_btn_see_lessons.clicked.connect(self.lesson_making_window.show_lessons)
    
    def lesson_assigning_page(self):
        
        # instance of lesson assigning window class
        self.lesson_assinging_window = Lesson_Assigning_Window(self.home)
        
        # set window icon and title
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("পাঠ বরাদ্দের তালিকা")
        
        # navigate between windows
        self.home.stackedWidget.setCurrentWidget(self.home.lesson_assigning_page)
        self.home.lsn_btn_back_to_home_4.clicked.connect(self.home_page)
        
        # connect buttons    
        self.home.lsn_btn_assign_lesson.clicked.connect(self.lesson_assinging_window.assign_lesson)    
    
    #! only module related text to be dragged [TODO]
    def dragEnterEvent(self, event):
        event.accept() if event.mimeData().hasText() else event.ignore()
                
    def dragMoveEvent(self, event):
        event.accept() if event.mimeData().hasText() else event.ignore()

    def dropEvent(self, event): 
        
        # Add the selected row to the list widget
        if event.mimeData().hasText():
            event.setDropAction(Qt.CopyAction)
            self.model().appendRow(QStandardItem(event.mimeData().text())) 
            event.accept()
        else: 
            event.ignore()
                        
    def matching_page(self):
        
        self.home.evalstackwidget.setCurrentWidget(self.home.matching_page)
        
    def sequence_page(self):
        
        self.home.evalstackwidget.setCurrentWidget(self.home.sequence_page) 
        
        # setup the video widget into layout
        if self.home.task_seq_video_frame_widget.count() != 0:
            self.home.task_seq_video_frame_widget.itemAt(
                0).widget().setParent(None)

        self.image_capture_window = ImageCaptureWidget(self.home)
        self.home.task_seq_video_frame_widget.addWidget(self.image_capture_window)
        
        
    def save_sequence_details(self):
        
        # read folder to track the folder names 
        existing_folders = os.listdir('Lessons/Sequence_Images')
        
        # save image to log file as json
        image_description = self.home.task_seq_img_desc_edit.text()
        image_sequence = self.home.task_seq_img_seq_edit.text()
        image_set = self.home.task_seq_set_lbl.text()
        current_saved_image_path = self.image_capture_window.current_saved_file
        
        # convert all spaces with _
        image_description = image_description.replace(" ", "_")
        
        # check if any filed is empty 
        if image_description == "" or image_sequence == "" or image_set == "":
            show_warning_message("ফিল্ড অসম্পূর্ণ", "সব ফিল্ড পূরণ করুন")
            return
        
        
        # make a directory mentioned in image_set 
        if not os.path.exists('Lessons/Sequence_Images/{}'.format(image_set)) and not image_set in existing_folders: 
            os.mkdir('Lessons/Sequence_Images/{}'.format(image_set))
            
        elif image_set in existing_folders and self.sequence_image_count == 0:
            show_warning_message("সেট নাম ইতিমধ্যে ব্যবহৃত", "এই নামের একটি সেট ইতিমধ্যে ব্যবহৃত হয়েছে, অন্য নাম ব্যবহার করুন")
            return
            
        # check if given serial is already exists in set 
        existing_files = os.listdir('Lessons/Sequence_Images/{}'.format(image_set))
        for file in existing_files:
            if image_sequence in file:
                show_warning_message("ভুল সিকোয়েন্স", "{} এই সিকোয়েন্স ইতিমধ্যে ব্যবহৃত হয়েছে".format(image_sequence))
                return 
            
        # check if 4 image is selected or not
        if self.sequence_image_count >= 3:
            shutil.move(current_saved_image_path, 'Lessons/Sequence_Images/{}/{}_{}.png'.format(image_set, image_sequence, image_description))
            show_confirmation_message("সম্পূর্ণ হয়েছে", "{} সেটের ৪ টি ছবি নির্বাচন করা হয়েছে, নতুন ছবি অন্য সেটে যোগ করতে পারেন".format(image_set))
            
            # reset all fields
            self.home.task_seq_img_desc_edit.clear()
            self.home.task_seq_img_seq_edit.clear()
            self.home.task_seq_set_lbl.clear()
            self.home.task_seq_img_view_lbl.clear()
            self.sequence_image_count = 0
            
        else: 
            
            # count number of image for each set 
            self.sequence_image_count += 1
            
            # save images to specific set
            shutil.move(current_saved_image_path, 'Lessons/Sequence_Images/{}/{}_{}.png'.format(image_set, image_sequence, image_description))
            show_warning_message("ছবি নির্বাচন করা হয়নি", "আরো {} ছবি নির্বাচন করতে হবে".format(4 - self.sequence_image_count))

    
    def puzzle_page(self):
        
        self.home.evalstackwidget.setCurrentWidget(self.home.puzzle_page)
        
        # select multiple image files using diaglog box 
                            
    def select_puzzle_image(self):
        
        print("Selecting puzzle image"	)
        file_names = None 
        
        # Open dialog box to select multiple files
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setNameFilter("Image Files (*.png);")
        if dialog.exec_():
            
            file_names = dialog.selectedFiles()
            
            # create a temp folder 
            os.path.exists('Lessons/Puzzle_Images') or os.mkdir('Lessons/Puzzle_Images')
            os.path.exists('Lessons/Puzzle_Images/Temp') or os.mkdir('Lessons/Puzzle_Images/Temp')
                        
        try: 
            
        # show file names in lbl
            names = ""
            for file_name in file_names:
                names += file_name.split("/")[-1] + "\n"
                
            names += "ছবি সংরক্ষন করার জন্য উপরে সেট নম্বর লিখুন এবং \'সংরক্ষন করুন\' বাটনে ক্লিক করুন।"
            self.home.task_puzzle_image_lbl.setText(names)
                 
            # copy image files
            for file_name in file_names: 
                
                # if self.home.task_puzzle_q_set_lbl.text() != "":
                #     folder_name = self.home.task_puzzle_q_set_lbl.text()
                #     try:
                #         shutil.copy2(file_name, 'Lessons/Puzzle_Images/{}/'.format(folder_name))
                #         self.home.task_puzzle_image_lbl.setText("ছবি {} ফোল্ডারে সংরক্ষণ করা হয়েছে।{} নতুন ফোল্ডারে সংরক্ষণের জন্য পুনরায় ছবি নির্বাচন করুন.".format(folder_name,'\n'))
                        
                #     except:
                #         os.mkdir('Lessons/Puzzle_Images/{}'.format(folder_name))
                #         shutil.copy2(file_name, 'Lessons/Puzzle_Images/{}/'.format(folder_name))
                #         self.home.task_puzzle_image_lbl.setText("ছবি {} ফোল্ডারে সংরক্ষণ করা হয়েছে।{} নতুন ফোল্ডারে সংরক্ষণের জন্য পুনরায় ছবি নির্বাচন করুন.".format(folder_name,'\n'))
                # else:
                shutil.copy2(file_name, 'Lessons/Puzzle_Images/Temp')
                
        except:
            pass 

    def save_puzzle_set(self):
        
        # rename folder Temp
        if os.path.exists('Lessons/Puzzle_Images/{}'.format(self.home.task_puzzle_q_set_lbl.text())) == False:
            os.rename('Lessons/Puzzle_Images/Temp', 'Lessons/Puzzle_Images/{}'.format(self.home.task_puzzle_q_set_lbl.text()))
            self.home.task_puzzle_image_lbl.setText("ছবি {} ফোল্ডারে সংরক্ষণ করা হয়েছে।{} নতুন ফোল্ডারে সংরক্ষণের জন্য পুনরায় ছবি নির্বাচন করুন".format(self.home.task_puzzle_q_set_lbl.text(), '\n'))	
            
            self.home.task_puzzle_q_set_lbl.clear()
            show_success_message("ছবি সংরক্ষন সম্পন্ন হয়েছে", "সংরক্ষন সম্পন্ন")
        
        else:
            show_warning_message("ফোল্ডার ইতোমধ্যে তৈরি করা হয়েছে", "{} ফোল্ডার ইতোমধ্যে তৈরি করা হয়েছে! নতুন সেট নম্বর নির্বাচন করুন".format(self.home.task_puzzle_q_set_lbl.text()))
                    
    def show_puzzle_set(self):
        
        # open lesson folder  
        os.startfile('Lessons\Puzzle_Images') 
        
      