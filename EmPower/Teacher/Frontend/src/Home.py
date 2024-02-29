'''
    From now, when you want to add a new page, you can follow the same steps:
    1. Create a new class for the new page (in Frontend.src)
    2. Create a new function for the new page (in main.py [e.g. student_info_page()])
    3. Initialize the ui object of the new page (in main.py [e.g. self.std_window = ui_student.Ui_MainWindow()])
    4. Connect the button call to the new page (in main.py [e.g. self.std_window.btn_add_new_student.clicked.connect(std_methods.add_new_row)])
    5. Pass the ui object of the new page to the new class (in main.py [e.g. std_methods = Student_Window(self.std_window)])
    6. Implement the functions of the new class (in Frontend.src) [remember to pass reference of current parent obj, otherwise widget window might not be shown]
'''

import datetime
import json
import os
import random
import re
import shutil

from Backend.Database.evaluation_assessment_db import \
    evaluation_assessment_data as ead
from Backend.Database.lesson_db import lesson_data as ld
from Backend.Database.lesson_performance_db import \
    lesson_performance_data as lpd
from Backend.Database.module_db import module_data as md
from Backend.Database.student_db import student_data as sd
from Backend.Database.surveillance_db import surveillance_data as svd
from Backend.GraphGenerator.BarChart import BarChart
from Backend.GraphGenerator.PieChart import PieChart
from Backend.PDF_ReportGeneration.ReportCard import Report_Card_Generator
from Backend.ScreenShot.ImageCapture import ImageCaptureWidget
from Frontend.src.Document_Formatter import *
from Frontend.src.Lesson_Assigning_Window import Lesson_Assigning_Window
from Frontend.src.Lesson_Making_Wiindow import Lesson_Making_Window
from Frontend.src.Lesson_Window import Lesson_Window
from Frontend.src.Student_Window import Student_Window
from Frontend.src.Task_Window import Task_Window
from Frontend.Teacher_UI import ui_home_page


class Home(QMainWindow):  # Home extends QMainWindow

    def __init__(self):
        super(QMainWindow, self).__init__()

        self.home = None
        self.sequence_image_count = 0
        self.sequence_details = {}
        self.current_matching_set = []
        self.current_matching_image_count = 0
        self.mcq_questions = {}
        self.total_mcq_questions = 1

        self.home_page()
        self.populate_performance_table()

        # buttons

    # def encode_dir_name(name):
    #     return name.encode('utf-8').decode('utf-8')

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
        self.home.home_btn_lesson_assigns.clicked.connect(
            self.lesson_assigning_page)
        self.home.home_btn_progress.clicked.connect(self.performance_page)

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
        self.home.std_btn_add_student.clicked.connect(
            self.student_window.add_new_row)
        self.home.std_btn_update_info.clicked.connect(
            self.student_window.update_student_info)
        self.home.std_btn_remove_student.clicked.connect(
            self.student_window.remove_rows)

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
        self.home.lsn_btn_add_lessons.clicked.connect(
            self.lesson_window.create_lesson)
        self.home.lsn_cmb_category.currentIndexChanged.connect(
            self.lesson_window.on_category_changed)
        self.home.lsn_cmb_lessons.currentIndexChanged.connect(
            self.lesson_window.on_lesson_changed)
        self.home.lsn_btn_reload_window.clicked.connect(self.home_page)
        self.home.lsn_btn_make_lesson.clicked.connect(self.lesson_making_page)
        self.home.lsn_btn_back_to_home.clicked.connect(self.home_page)

    def task_page(self):

        self.task_window = Task_Window(self.home)

        # Navigate between windows
        self.home.stackedWidget.setCurrentWidget(self.home.task_page)
        self.home.evalstackwidget.setCurrentWidget(self.home.matching_page)
        self.home.task_btn_back_to_home.clicked.connect(self.home_page)
        # self.matching_page()

        # Connecting Task window buttons
        # !need to move on Task Window Page
        self.home.task_btn_matching.clicked.connect(self.matching_page)
        self.home.task_btn_sequence.clicked.connect(self.sequence_page)
        self.home.task_btn_puzzle.clicked.connect(self.puzzle_page)
        self.home.task_btn_mcq.clicked.connect(self.mcq_page)
        self.home.task_puzzle_select_img_btn.clicked.connect(
            self.select_puzzle_image)
        self.home.task_puzzle_save_set_btn.clicked.connect(
            self.save_puzzle_set)
        self.home.task_puzzle_show_set_btn.clicked.connect(
            self.show_puzzle_set)
        self.home.task_seq_img_save_btn.clicked.connect(
            self.save_sequence_details)

        # remove temp folder
        os.path.exists('Lessons/Matching_Images/.temp') and shutil.rmtree('Lessons/Matching_Images/.temp')

        # connecting Matching Page buttons
        self.home.task_matching_img_add_btn_1.clicked.connect(
            lambda: self.matching_process(
                self.home.task_matching_img_view_lbl_1
            ))
        self.home.task_matching_img_add_btn_2.clicked.connect(
            lambda: self.matching_process(
                self.home.task_matching_img_view_lbl_2
            ))
        self.home.task_matching_img_add_btn_3.clicked.connect(
            lambda: self.matching_process(
                self.home.task_matching_img_view_lbl_3
            ))
        self.home.task_matching_img_add_btn_4.clicked.connect(
            lambda: self.matching_process(
                self.home.task_matching_img_view_lbl_4
            ))
        self.home.task_matching_save_set_btn.clicked.connect(
            self.save_matching_set)

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
        self.home.lsn_module_table_widget.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.home.lsn_module_table_widget.setDragDropMode(
            QAbstractItemView.DragOnly)
        self.home.lsn_new_module_list_view.setAcceptDrops(True)
        self.home.lsn_new_module_list_view.setModel(QStandardItemModel(0, 1))

        # connect buttons
        self.home.lsn_btn_remove_module.clicked.connect(
            self.lesson_making_window.remove_list_item)
        self.home.lsn_btn_finish_add_module.clicked.connect(
            self.lesson_making_window.make_lesson)
        self.home.lsn_btn_see_lessons.clicked.connect(
            self.lesson_making_window.show_lessons)

    def lesson_assigning_page(self):

        # instance of lesson assigning window class
        self.lesson_assinging_window = Lesson_Assigning_Window(self.home)

        # set window icon and title
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("পাঠ বরাদ্দের তালিকা")

        # navigate between windows
        self.home.stackedWidget.setCurrentWidget(
            self.home.lesson_assigning_page)
        self.home.lsn_btn_back_to_home_4.clicked.connect(self.home_page)

        # connect buttons
        self.home.lsn_btn_assign_lesson.clicked.connect(
            self.lesson_assinging_window.assign_lesson)

    #! TODO: only module related text to be dragged
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

        # check if Matching_Images folder exists or not
        os.path.exists(
            'Lessons/Matching_Images') or os.mkdir('Lessons/Matching_Images')

    #! TODO: Will move this method to separate class if we got times
    def sequence_page(self):

        self.home.evalstackwidget.setCurrentWidget(self.home.sequence_page)

        # check if Sequence_Images folder exists or not
        os.path.exists(
            'Lessons/Sequence_Images') or os.mkdir('Lessons/Sequence_Images')

        # setup the video widget into layout
        if self.home.task_seq_video_frame_widget.count() != 0:
            self.home.task_seq_video_frame_widget.itemAt(
                0).widget().setParent(None)

        self.image_capture_window = ImageCaptureWidget(self.home)
        self.home.task_seq_video_frame_widget.addWidget(
            self.image_capture_window)

    def save_sequence_details(self):

        # read folder to track the folder names
        existing_folders = os.listdir('Lessons/Sequence_Images')

        # save image to log file as json
        image_description = self.home.task_seq_img_desc_edit.text()
        # image_sequence = self.home.task_seq_img_seq_edit.text()
        image_set = 's_' + self.home.task_seq_set_lbl.text()
        current_saved_image_path = self.image_capture_window.current_saved_file

        # convert all spaces with _
        image_description = image_description.replace(" ", "_")

        # check if any filed is empty
        if image_description == "" or image_set == "":
            show_warning_message("ফিল্ড অসম্পূর্ণ", "সব ফিল্ড পূরণ করুন")
            return

        # make a directory mentioned in image_set
        # Make a directory mentioned in image_set
        if not os.path.exists('Lessons/Sequence_Images/{}'.format(image_set)):
            os.mkdir('Lessons/Sequence_Images/{}'.format(image_set))

        elif image_set in existing_folders and self.sequence_image_count == 0:
            show_warning_message(
                "সেট নাম ইতিমধ্যে ব্যবহৃত", "এই নামের একটি সেট ইতিমধ্যে ব্যবহৃত হয়েছে, অন্য নাম ব্যবহার করুন")
            return

        # check if 4 image is selected or not
        if self.sequence_image_count >= 3:
            shutil.move(current_saved_image_path, 'Lessons/Sequence_Images/{}/{}_{}.png'.format(
                image_set, self.sequence_image_count+1, image_description))
            show_confirmation_message(
                "সম্পূর্ণ হয়েছে", "{} সেটের ৪ টি ছবি নির্বাচন করা হয়েছে, নতুন ছবি অন্য সেটে যোগ করতে পারেন".format(image_set))

            # reset all fields
            self.home.task_seq_img_desc_edit.clear()
            self.home.task_seq_img_seq_edit.clear()
            self.home.task_seq_set_lbl.clear()
            self.home.task_seq_img_view_lbl.clear()

            # save data to json
            image_name = '{}/{}.png'.format(image_set, image_description)
            self.sequence_details[self.sequence_image_count+1] = image_name[2:]
            self.sequence_details['creation_date'] = datetime.datetime.now().strftime(
                "%d/%m/%Y")
            self.sequence_details['creation_time'] = datetime.datetime.now().strftime(
                "%H:%M:%S")
            self.sequence_details['topic'] = self.home.task_seq_set_lbl.text()
            json_file_path = 'Lessons/Sequence_Images/{}/image_data.json'.format(
                image_set)
            with open(json_file_path, 'w') as json_file:
                json.dump(self.sequence_details, json_file)

            self.sequence_details = {}
            self.sequence_image_count = 0

        else:

            # count number of image for each set
            self.sequence_image_count += 1

            # save images to specific set
            shutil.move(current_saved_image_path, 'Lessons/Sequence_Images/{}/{}_{}.png'.format(
                image_set, self.sequence_image_count, image_description))
            show_warning_message("ছবি নির্বাচন শেষ হয়নি", "আরো {} ছবি নির্বাচন করতে হবে".format(
                4 - self.sequence_image_count))

            # save data to json
            image_name = '{}/{}.png'.format(image_set, image_description)
            self.sequence_details[self.sequence_image_count] = image_name[2:]

    #! TODO: Will move this method to separate class if we got times

    def puzzle_page(self):

        self.home.evalstackwidget.setCurrentWidget(self.home.puzzle_page)

        # check if Puzzle_Images folder exists or not
        os.path.exists(
            'Lessons/Puzzle_Images') or os.mkdir('Lessons/Puzzle_Images')

    def select_puzzle_image(self):

        print("Selecting puzzle image")
        file_names = None

        # Open dialog box to select multiple files
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Image Files (*.png *.jpg *.jpeg);")
        if dialog.exec_():

            file_names = dialog.selectedFiles()

            # create a temp folder
            os.path.exists(
                'Lessons/Puzzle_Images') or os.mkdir('Lessons/Puzzle_Images')
            os.path.exists(
                'Lessons/Puzzle_Images/.temp') or os.mkdir('Lessons/Puzzle_Images/.temp')

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
                shutil.copy2(file_name, 'Lessons/Puzzle_Images/.temp')

        except:
            pass

    def save_puzzle_set(self):

        puzzle_set = 'p_' + self.home.task_puzzle_q_set_lbl.text()

        # rename folder Temp
        if os.path.exists('Lessons/Puzzle_Images/{}'.format(puzzle_set)) == False:
            os.rename('Lessons/Puzzle_Images/.temp',
                      'Lessons/Puzzle_Images/{}'.format(puzzle_set))
            self.home.task_puzzle_image_lbl.setText("ছবি {} ফোল্ডারে সংরক্ষণ করা হয়েছে।{} নতুন ফোল্ডারে সংরক্ষণের জন্য পুনরায় ছবি নির্বাচন করুন".format(
                self.home.task_puzzle_q_set_lbl.text(), '\n'))

            self.home.task_puzzle_q_set_lbl.clear()
            show_success_message(
                "ছবি সংরক্ষন সম্পন্ন হয়েছে", "সংরক্ষন সম্পন্ন")

        else:
            show_warning_message("ফোল্ডার ইতোমধ্যে তৈরি করা হয়েছে", "{} ফোল্ডার ইতোমধ্যে তৈরি করা হয়েছে! নতুন সেট নম্বর নির্বাচন করুন".format(
                self.home.task_puzzle_q_set_lbl.text()))

    def show_puzzle_set(self):

        # open lesson folder
        os.startfile('Lessons\Puzzle_Images')

    #! TODO: Will move this method to separate class if we got times

    def matching_process(self, frame_name):

        # paths
        file_path = ""
        image_path = ""

        # check if .temp file is in Matching_Images folder
        if os.path.exists('Lessons/Matching_Images/.temp') == False:
            os.mkdir('Lessons/Matching_Images/.temp')

        # open file diaglog box to select image
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFile)

        # accepts png, jpg, jpged files
        dialog.setNameFilter("Image Files (*.png *.jpg *.jpeg);")

        if dialog.exec_() == QFileDialog.Accepted:

            file_path = dialog.selectedFiles()[0]
            image_path = 'Lesson/Matching_Images/.temp/{}'.format(
                file_path.split('/')[-1])
            image_name = file_path.split('/')[-1]

            pixmap = QPixmap()
            pixmap.load(file_path)

            # replace frame_name with actal frame
            if not pixmap.isNull():
                scaled_pixmap = pixmap.scaled(
                    frame_name.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                frame_name.setPixmap(scaled_pixmap)
            else:
                print("Failed to load the image:", image_path)

            # copy the image into temp folder
            shutil.copy2(file_path, 'Lessons/Matching_Images/.temp')

            # rename the image
            try:
                os.rename(
                    'Lessons/Matching_Images/.temp/{}'.format(image_name),
                    'Lessons/Matching_Images/.temp/{}_{}.png'.format(
                        image_name.split('.')[0], frame_name.objectName()[-1])
                )
                self.current_matching_set.append('Lessons/Matching_Images/.temp/{}_{}.png'.format(
                    image_name.split('.')[0], frame_name.objectName()[-1]))

            except:
                print("File already exists")

    def save_matching_set(self):

        # dictionary to store image description
        image_data = {}

        img_desc_1 = self.home.task_matching_img_desc_edit_1.text()
        img_desc_2 = self.home.task_matching_img_desc_edit_2.text()
        img_desc_3 = self.home.task_matching_img_desc_edit_3.text()
        img_desc_4 = self.home.task_matching_img_desc_edit_4.text()

        # check if corresponding images's description are filledup
        for item in self.current_matching_set:

            set_id = item.split('_')[-1].split('.')[0]

            if set_id == '1':
                if img_desc_1 == "":
                    show_warning_message(
                        "বর্ণনা পূরণ করুন", "{} নং ছবির সংক্ষিপ্ত বর্ণনা পূরণ করুন".format(set_id))
                    return False
            elif set_id == '2':
                if img_desc_2 == "":
                    show_warning_message(
                        "বর্ণনা পূরণ করুন", "{} নং ছবির সংক্ষিপ্ত বর্ণনা পূরণ করুন".format(set_id))
                    return False
            elif set_id == '3':
                if img_desc_3 == "":
                    show_warning_message(
                        "বর্ণনা পূরণ করুন", "{} নং ছবির সংক্ষিপ্ত বর্ণনা পূরণ করুন".format(set_id))
                    return False
            elif set_id == '4':
                if img_desc_4 == "":
                    show_warning_message(
                        "বর্ণনা পূরণ করুন", "{} নং ছবির সংক্ষিপ্ত বর্ণনা পূরণ করুন".format(set_id))
                    return False

        # create a new folder according to set name provided
        matching_set_name = 'm_' + self.home.task_matching_set_edit.text()

        # check if set name is provided
        if matching_set_name == "":
            show_warning_message("সেট নাম পূরণ করুন", "সেট নাম পূরণ করুন")
            return False

        # check if set name already exists
        if os.path.exists('Lessons/Matching_Images/{}'.format(matching_set_name)):
            show_warning_message("সেট নাম পুনরায় লিখুন",
                                 "এই নামে একটি সেট আগে থেকেই রয়েছে")
            return False
        else:
            os.mkdir('Lessons/Matching_Images/{}'.format(matching_set_name))

        # copy images from temp folder to new folder
        for item in self.current_matching_set:

            # get the set id
            set_id = item.split('_')[-1].split('.')[0]
            image_name = item.split('/')[-1]

            # move images to new folder
            shutil.move(
                item, 'Lessons/Matching_Images/{}'.format(matching_set_name))
            item = 'Lessons/Matching_Images/{}/{}'.format(
                matching_set_name, image_name)
            item = item.replace('Lessons/Matching_Images/', '')

            # Get the image description based on the set ID
            if set_id == '1':
                image_desc = img_desc_1
            elif set_id == '2':
                image_desc = img_desc_2
            elif set_id == '3':
                image_desc = img_desc_3
            elif set_id == '4':
                image_desc = img_desc_4
            else:
                image_desc = ""

            # Add the image name and description to the dictionary
            image_data[item] = image_desc

        image_data['creation_date'] = datetime.datetime.now().strftime(
            "%d/%m/%Y")
        image_data['creation_time'] = datetime.datetime.now().strftime(
            "%H:%M:%S")

        # Save the image data as a JSON file
        json_file_path = 'Lessons/Matching_Images/{}/image_data.json'.format(
            matching_set_name)
        with open(json_file_path, 'w') as json_file:
            json.dump(image_data, json_file)

        # clear lbls and edits
        self.home.task_matching_img_desc_edit_1.clear()
        self.home.task_matching_img_desc_edit_2.clear()
        self.home.task_matching_img_desc_edit_3.clear()
        self.home.task_matching_img_desc_edit_4.clear()

        self.home.task_matching_img_view_lbl_1.clear()
        self.home.task_matching_img_view_lbl_2.clear()
        self.home.task_matching_img_view_lbl_3.clear()
        self.home.task_matching_img_view_lbl_4.clear()

        # show success message
        set_items = len(os.listdir(
            'Lessons/Matching_Images/{}'.format(matching_set_name)))
        if set_items <= 1:
            show_warning_message("পর্যাপ্ত ছবি নেই", "সেটে ৪টি ছবি থাকতে হবে")
            shutil.rmtree(
                'Lessons/Matching_Images/{}'.format(matching_set_name))
        else:
            show_success_message("সেট সংরক্ষণ সম্পন্ন", "{} সেট সংরক্ষণ সম্পন্ন হয়েছে".format(
                matching_set_name.split('_')[-1]))
            os.startfile('Lessons\Matching_Images\{}'.format(
                matching_set_name))  # ! always use \ for relative path
            self.home.task_matching_set_edit.clear()

    #! TODO: Will move this method to separate class if we got times

    def mcq_page(self):

        self.home.evalstackwidget.setCurrentWidget(self.home.mcq_page)

        # connect the buttons
        self.home.task_mcq_new_set_btn.clicked.connect(self.create_mcq_set)
        self.home.task_mcq_finish_set_btn.clicked.connect(self.finish_mcq_set)
        self.home.task_mcq_next_ques_btn.clicked.connect(
            self.next_mcq_question)
        self.home.task_mcq_upload_img_btn.clicked.connect(
            self.upload_mcq_image)

    def create_mcq_set(self):

        set_no = 'q_'+self.home.task_mcq_set_no_edit.toPlainText()

        # if set name is not provided
        if self.home.task_mcq_set_no_edit.toPlainText() == "":
            show_confirmation_message("সেট নম্বর অনুপস্থিত", "সেট নম্বর প্রদান করুন এবং 'নতুন প্রশ্ন সেট বাটনে ক্লিক করুন।")
            return 

        # make a subfolder inside the mcq_questions folder
        if os.path.exists(f"Lessons/MCQ_Questions/{set_no}"):
            sets = os.listdir('Lessons/MCQ_Questions')
            show_warning_message(
                "সেট নাম পুনরায় লিখুন", "এই নামে একটি সেট আগে থেকেই রয়েছে। বর্তমানে বিদ্যমান সেটগুলো হল : {}".format(sets))
            return
        else:
            os.mkdir(f"Lessons/MCQ_Questions/{set_no}")

        # basic instruction
        show_confirmation_message(
            "প্রশ্ন সেট তৈরি", "এখন প্রশ্ন এবং সম্ভাব্য উত্তরসমূহ প্রদান করুন। নতুন প্রশ্ন তৈরির করতে 'পরবর্তী প্রশ্ন' বাটনে ক্লিক করুন।")

        ques_no = str(self.total_mcq_questions)

        # make folders to save questions
        os.path.exists(
            "Lessons/MCQ_Questions") or os.mkdir("Lessons/MCQ_Questions")

        # enable all edit boxes
        self.home.task_mcq_set_no_edit.setEnabled(True)
        self.home.task_mcq_finish_set_btn.setEnabled(True)
        self.home.task_mcq_next_ques_btn.setEnabled(True)
        self.home.task_mcq_question_edit.setEnabled(True)
        self.home.task_mcq_option_1_edit.setEnabled(True)
        self.home.task_mcq_option_2_edit.setEnabled(True)
        self.home.task_mcq_option_3_edit.setEnabled(True)
        self.home.task_mcq_option_4_edit.setEnabled(True)
        self.home.task_mcq_correct_option_edit.setEnabled(True)
        self.home.task_mcq_upload_img_btn.setEnabled(True)

        self.mcq_questions[ques_no] = {
            "question": '',
            "option_1": '',
            "option_2": '',
            "option_3": '',
            "option_4": '',
            "correct_answer": '',
            "image": ''
        }

    def finish_mcq_set(self):

        # enable button
        self.home.task_mcq_finish_set_btn.setEnabled(True)

        if self.mcq_questions == {}:
            show_warning_message(
                "কোন প্রশ্ন নেই", "কোন প্রশ্ন নেই যার উত্তর সংরক্ষণ করা যাবে")
            return False

        # get the set name
        set_no = 'q_'+self.home.task_mcq_set_no_edit.toPlainText()

        # copy image after json is writen
        # for i in range(1, self.total_mcq_questions+1):
        #     if self.mcq_questions[str(i)]["image"]:
        #         shutil.copy2(self.mcq_questions[str(i)]["image"], f"Lessons/MCQ_Questions/{self.home.task_mcq_set_no_edit.toPlainText()}//q_{i}.png")

        # load the last question
        self.next_mcq_question()

        # save the questions to json
        with open(f"Lessons/MCQ_Questions/{set_no}/questions.json", "w") as f:
            json.dump(self.mcq_questions, f)

        # reset the mcq_questions dict
        self.mcq_questions = {}
        self.total_mcq_questions = 1

        # show message
        show_confirmation_message(
            "সেট সংরক্ষণ সম্পন্ন", f"MCQ {set_no} সেট সংরক্ষণ সম্পন্ন হয়েছে। নতুন প্রশ্ন সেট তৈরির জন্য 'প্রশ্ন সেট তৈরি' বাটনে ক্লিক করুন।")

        # disable buttons
        self.home.task_mcq_finish_set_btn.setEnabled(False)
        self.home.task_mcq_next_ques_btn.setEnabled(False)
        self.home.task_mcq_upload_img_btn.setEnabled(False)
        self.home.task_mcq_question_edit.setEnabled(False)
        self.home.task_mcq_option_1_edit.setEnabled(False)
        self.home.task_mcq_option_2_edit.setEnabled(False)
        self.home.task_mcq_option_3_edit.setEnabled(False)
        self.home.task_mcq_option_4_edit.setEnabled(False)
        self.home.task_mcq_correct_option_edit.setEnabled(False)

    def upload_mcq_image(self):
        # Open dialog to select an image
        img_path = QFileDialog.getOpenFileName(
            self, "ছবি নির্বাচন করুন", "", "Image Files (*.png *.jpg *.jpeg)")[0]
        if img_path != '':
            self.current_mcq_image_path = img_path
            shutil.copy2(
                img_path, f"Lessons/MCQ_Questions/{'q_'+self.home.task_mcq_set_no_edit.toPlainText()}//q_{self.total_mcq_questions}.png")
            self.home.task_mcq_img_lbl.setText(img_path.split("/")[-1])
        else:
            self.current_mcq_image_path = ''
            self.home.task_mcq_img_lbl.setText('')

    def next_mcq_question(self):

        print(self.mcq_questions)

        # Read all the questions and options from the edit boxes
        question = self.home.task_mcq_question_edit.toPlainText()
        option_1 = self.home.task_mcq_option_1_edit.toPlainText()
        option_2 = self.home.task_mcq_option_2_edit.toPlainText()
        option_3 = self.home.task_mcq_option_3_edit.toPlainText()
        option_4 = self.home.task_mcq_option_4_edit.toPlainText()
        correct_answer = self.home.task_mcq_correct_option_edit.toPlainText()

        # Check if any of the edit boxes are empty
        if question == "" or option_1 == "" or option_2 == "" or option_3 == "" or option_4 == "" or correct_answer == "":
            show_warning_message("প্রশ্ন সম্পন্ন করুন",
                                 "সকল অপশনসমূহ প্রদান করুন")
            return

        # Store the current question and options in the dictionary
        self.mcq_questions[str(self.total_mcq_questions)] = {
            "question": question,
            "option_1": option_1,
            "option_2": option_2,
            "option_3": option_3,
            "option_4": option_4,
            "correct_answer": correct_answer,
            # "image": self.current_mcq_image_path
        }

        # Clear all the edit boxes
        self.home.task_mcq_question_edit.clear()
        self.home.task_mcq_option_1_edit.clear()
        self.home.task_mcq_option_2_edit.clear()
        self.home.task_mcq_option_3_edit.clear()
        self.home.task_mcq_option_4_edit.clear()
        self.home.task_mcq_correct_option_edit.clear()
        self.home.task_mcq_img_lbl.setText('')

        # Increment the total questions
        self.total_mcq_questions += 1
        self.current_mcq_image_path = ''

    #! TODO: Will move this method to separate class if we got times

    def performance_page(self):

        # navigate the window
        self.home.stackedWidget.setCurrentWidget(self.home.performance_page)

        # connecting buttons
        self.home.performance_lesson_btn.clicked.connect(
            lambda: self.home.performance_stackwidget.setCurrentWidget(self.home.lesson_stk_widget))
        self.home.performance_module_btn.clicked.connect(
            lambda: self.home.performance_stackwidget.setCurrentWidget(self.home.module_stk_widget))
        self.home.performance_eval_btn.clicked.connect(
            lambda: self.home.performance_stackwidget.setCurrentWidget(self.home.eval_stk_widget))

        self.home.lsn_btn_back_to_home_5.clicked.connect(self.home_page)
        self.home.performance_report_btn.clicked.connect(
            self.load_performance_report)
        self.home.p_eval_matching_btn.clicked.connect(
            self.load_matching_graphs)
        self.home.p_eval_seq_btn.clicked.connect(self.load_sequence_graphs)
        self.home.p_eval_puzzle_btn.clicked.connect(self.load_puzzle_graphs)
        self.home.p_eval_mcq_btn.clicked.connect(self.load_mcq_graphs)

        # read the json files from Performance folder
        # self.populate_performance_table()

        # Disable the first option
        self.home.performance_std_id_cmb.model().item(0).setEnabled(False)

    def load_matching_graphs(self):

        self.home.p_eval_left_graph_lbl.setScaledContents(True)
        self.home.p_eval_left_graph_lbl.setPixmap(
            QPixmap('.temp/matching_success_rate_bar_chart.png'))

        self.home.p_eval_right_graph_lbl.setScaledContents(True)
        self.home.p_eval_right_graph_lbl.setPixmap(
            QPixmap('.temp/matching_time_bar_chart.png'))

    def load_sequence_graphs(self):

        self.home.p_eval_left_graph_lbl.setScaledContents(True)
        self.home.p_eval_left_graph_lbl.setPixmap(
            QPixmap('.temp/sequence_success_rate_bar_chart.png'))

        self.home.p_eval_right_graph_lbl.setScaledContents(True)
        self.home.p_eval_right_graph_lbl.setPixmap(
            QPixmap('.temp/sequence_time_bar_chart.png'))

    def load_puzzle_graphs(self):

        self.home.p_eval_left_graph_lbl.setScaledContents(True)
        self.home.p_eval_left_graph_lbl.setPixmap(
            QPixmap('.temp/puzzle_success_rate_bar_chart.png'))

        self.home.p_eval_right_graph_lbl.setScaledContents(True)
        self.home.p_eval_right_graph_lbl.setPixmap(
            QPixmap('.temp/puzzle_time_bar_chart.png'))

    def load_mcq_graphs(self):

        self.home.p_eval_left_graph_lbl.setScaledContents(True)
        self.home.p_eval_left_graph_lbl.setPixmap(
            QPixmap('.temp/mcq_success_rate_bar_chart.png'))

        self.home.p_eval_right_graph_lbl.setScaledContents(True)
        self.home.p_eval_right_graph_lbl.setPixmap(
            QPixmap('.temp/mcq_time_bar_chart.png'))

    def populate_performance_table(self):

        student_details = {}
        std_name = ''
        std_id = ''

        self.performance_folders = os.listdir('Performance')
        print(self.performance_folders)

        for folder_name in self.performance_folders:

            folder_files = os.listdir('Performance/{}'.format(folder_name))

            # read the json files
            for json_file in folder_files:

                if 'lesson' in json_file:
                    with open(f'Performance\{folder_name}\.lesson_completion_log.json', 'r') as f:
                        lesson_completion_data = json.load(f)
                        data = [
                            lesson_completion_data['std_id'],
                            lesson_completion_data['std_name'],
                            lesson_completion_data['lesson_id'],
                            lesson_completion_data['attempt'],
                            lesson_completion_data['time'],
                        ]
                        student_details[str(data[0])] = data[1]
                        std_name = data[1]
                        std_id = data[0]
                        lpd().add_entry(data)

                elif 'matching' in json_file:
                    with open(f'Performance\{folder_name}\matching_results.json', 'r') as f:
                        matching_completion_data = json.load(f)

                        data = [
                            matching_completion_data['std_id'],
                            matching_completion_data['std_name'],
                            matching_completion_data['set_name'],
                            matching_completion_data['attempts'],
                            matching_completion_data['success_rate'],
                            matching_completion_data['time'],
                        ]
                        ead().add_entry(data)

                elif 'sequencing' in json_file:
                    with open(f'Performance\{folder_name}\sequencing_results.json', 'r') as f:
                        sequencing_completion_data = json.load(f)

                        data = [
                            sequencing_completion_data['std_id'],
                            sequencing_completion_data['std_name'],
                            sequencing_completion_data['set_name'],
                            sequencing_completion_data['attempts'],
                            sequencing_completion_data['success_rate'],
                            sequencing_completion_data['time'],
                        ]
                        ead().add_entry(data)

                elif 'puzzle' in json_file:
                    with open(f'Performance\{folder_name}\puzzle_results.json', 'r') as f:
                        puzzle_completion_data = json.load(f)

                        data = [
                            puzzle_completion_data['std_id'],
                            puzzle_completion_data['std_name'],
                            puzzle_completion_data['set_name'],
                            puzzle_completion_data['total_attempt'],
                            puzzle_completion_data['success_rate'],
                            puzzle_completion_data['time'],
                        ]
                        ead().add_entry(data)

                elif 'mcq' in json_file:

                    with open(f'Performance\{folder_name}\mcq_results.json', 'r') as f:
                        puzzle_completion_data = json.load(f)

                        data = [
                            puzzle_completion_data['std_id'],
                            puzzle_completion_data['std_name'],
                            puzzle_completion_data['set_name'],
                            puzzle_completion_data['attempts'],
                            puzzle_completion_data['success_rate'],
                            puzzle_completion_data['time'],
                        ]
                        ead().add_entry(data)

                else:

                    with open(f'Performance\{folder_name}\surveillance_log.json', 'r') as f:
                        surveillance_data = json.load(f)
                        
                        print("DATA: >> ", surveillance_data)

                        # # Iterate over the dictionary items
                        # for lesson_id, module_data in surveillance_data.items():
                        #     # Iterate over the module data items
                            
                        #     for module_id, completion_time in module_data.items():
                        #         # Execute an SQL INSERT statement to add the data into the table
                        #         data = (std_id, std_name, lesson_id,
                        #                 module_id, completion_time)
                        #         svd().add_entry(data)
                        
                        lesson_id = surveillance_data['lesson_id']
                        module_dict = surveillance_data['module_wise_time'][0]
                        for key, value in module_dict.items():
                            module_id = key
                            completion_time = value
                            data = (std_id, std_name, lesson_id, module_id, completion_time)
                            svd().add_entry(data)

                    print("Surveillance data added to database")

        std_entry = []
        for sid, sname in student_details.items():
            std_entry.append(sid+'_'+sname)

        print(std_entry)

        # add data to combobox
        for entry in std_entry:
            self.home.performance_std_id_cmb.addItem(entry)

        self.home.performance_std_id_cmb.currentIndexChanged.connect(
            self.load_user_performance_data)

    def load_user_performance_data(self, index):

        # if exisits then we need to delete it first as we need new table for
        # each newly selected student
        if os.path.exists('.temp'):
            shutil.rmtree('.temp')

        os.mkdir('.temp')

        # data for specific student selected in the combobox
        student_evaluation_details = []
        student_lesson_details = []
        self.home.performance_eval_btn.setEnabled(True)
        self.home.performance_lesson_btn.setEnabled(True)

        # # get details of student from db
        student_id = self.home.performance_std_id_cmb.currentText().split('_')[
            0]
        student_evaluation_details = ead().load_table(student_id)
        student_lesson_details = lpd().load_table(student_id)
        student_surveillance_details = svd().load_table(student_id)

        matching_data = []
        sequence_data = []
        puzzle_data = []
        mcq_data = []
        surveillance_data = []

        for row in student_evaluation_details:

            if row[2].startswith('m_'):
                matching_data.append(row)
            elif row[2].startswith('s_'):
                sequence_data.append(row)
            elif row[2].startswith('p_'):
                puzzle_data.append(row)
            elif row[2].startswith('q_'):
                mcq_data.append(row)

        for row in student_surveillance_details:
            surveillance_data.append(row)

        print(surveillance_data)

        self.load_lesson_performance_data(student_lesson_details)
        self.load_matching_performance_data(matching_data)
        self.load_sequencing_performance_data(sequence_data)
        self.load_puzzle_performance_data(puzzle_data)
        self.load_mcq_performance_data(mcq_data)
        self.load_surveillance_performance_data(surveillance_data)

    def load_puzzle_performance_data(self, puzzle_data):

        # puzzle labels and valus
        puzzle_labels = []
        puzzle_success_rate = []
        puzzle_time = []

        for row in puzzle_data:
            puzzle_labels.append(row[2][2:])
            puzzle_success_rate.append(row[4])
            puzzle_time.append(row[5])

        # Generate BarChart for puzzle completion
        barchart = BarChart(puzzle_labels, puzzle_success_rate, "Puzzle Set",
                            "Success Rate", "puzzle_success_rate_bar_chart.png", "Puzzle vs Success Rate")
        barchart2 = BarChart(puzzle_labels, puzzle_time, "Puzzle Set", "Completion Time (seconds)",
                             "puzzle_time_bar_chart.png", "Puzzle vs Completion Time (seconds)")

    def load_mcq_performance_data(self, mcq_data):

        # mcq labels and valus
        mcq_labels = []
        mcq_success_rate = []
        mcq_time = []

        for row in mcq_data:
            mcq_labels.append(row[2][2:])
            mcq_success_rate.append(row[4])
            mcq_time.append(row[5])

        # Generate BarChart for mcq completion
        barchart = BarChart(mcq_labels, mcq_success_rate, "MCQ Set", "Success Rate",
                            "mcq_success_rate_bar_chart.png", "MCQ vs Success Rate")
        barchart2 = BarChart(mcq_labels, mcq_time, "MCQ Set", "Completion Time (seconds)",
                             "mcq_time_bar_chart.png", "MCQ vs Completion Time (seconds)")

    def load_surveillance_performance_data(self, sur_data):

        # get the lesson names of which surveillance data are available
        unique_lessons = set(item[2] for item in sur_data)
        lesson_ids = list(unique_lessons)
        module_ids = [item[3] for item in sur_data]
        times = [float(item[4]) for item in sur_data]

        updated_data = []
        for item in sur_data:
            module_name = re.sub(r'^শিখন\(|\)$', '', item[3])
            m_type = module_name.split('_')
            m_id = m_type[1]
            m_name = m_type[0].strip(')') + '_' + m_id
            updated_data.append(m_name)

        # fill up lesson id table
        self.home.p_lesson_id_cmb.addItems(lesson_ids)

        data = [updated_data, times]
        self.home.p_lesson_id_cmb.currentIndexChanged.connect(
            lambda: self.generate_pie_chart(data))

    def generate_pie_chart(self, data):

        # get selected value
        selected_lesson_id = self.home.p_lesson_id_cmb.currentText()
        print(selected_lesson_id)

        PieChart(data[0], data[1], "module_completion_time_pie_chart.png",
                 f"Time Spent on Modules of Lesson {selected_lesson_id}")

        self.home.p_module_graph_lbl.setScaledContents(True)
        self.home.p_module_graph_lbl.setPixmap(
            QPixmap(".temp\module_completion_time_pie_chart.png"))

    def load_sequencing_performance_data(self, sequence_data):

        # sequence labels and values
        sequence_labels = []
        sequence_success_rate = []
        sequence_time = []

        for row in sequence_data:
            sequence_labels.append(row[2][2:])
            sequence_success_rate.append(row[4])
            sequence_time.append(row[5])

        # Generate BarChart for sequence completion
        barchart = BarChart(sequence_labels, sequence_success_rate, "Sequence Set",
                            "Success Rate", "sequence_success_rate_bar_chart.png", "Sequence vs Success Rate")
        barchart2 = BarChart(sequence_labels, sequence_time, "Sequence Set", "Completion Time (seconds)",
                             "sequence_time_bar_chart.png", "Sequence vs Completion Time (seconds)")

    def load_matching_performance_data(self, matching_data):

        # performance labels and values
        # matching labels and values
        matching_labels = []
        matching_success_rate = []
        matching_time = []

        for row in matching_data:
            matching_labels.append(row[2][2:])
            matching_success_rate.append(row[4])
            matching_time.append(row[5])

        # Generate BarChart for matching completion
        barchart = BarChart(matching_labels, matching_success_rate, "Matching Set",
                            "Success Rate", "matching_success_rate_bar_chart.png", "Matching vs Success Rate")
        barchart2 = BarChart(matching_labels, matching_time, "Matching Set", "Completion Time (seconds)",
                             "matching_time_bar_chart.png", "Matching vs Completion Time (seconds)")

    def load_lesson_performance_data(self, student_lesson_details):

        # lesson labels and values
        lesson_labels = []
        lesson_attempts = []
        lesson_times = []
        lesson_attempt_file_name = 'lesson_attempt_bar_chart.png'
        lesson_time_file_name = 'lesson_time_bar_chart.png'
        for row in student_lesson_details:
            lesson_labels.append('Lesson_'+str(row[2]))
            lesson_attempts.append(row[3])
            lesson_times.append(row[4])

        # Generate BarChart for lesson completion
        barchart = BarChart(lesson_labels, lesson_attempts, "",
                            "Attempts", lesson_attempt_file_name, "Lesson vs Attempts")
        barchart = BarChart(lesson_labels, lesson_times, "", "Completion Time (seconds)",
                            lesson_time_file_name, "Lesson vs Completion Time (seconds)")

        # now make graph and chart using student data
        self.home.p_lesson_left_graph_lbl.setScaledContents(True)
        self.home.p_lesson_left_graph_lbl.setPixmap(
            QPixmap('.temp/'+lesson_attempt_file_name))

        self.home.p_lesson_right_graph_lbl.setScaledContents(True)
        self.home.p_lesson_right_graph_lbl.setPixmap(
            QPixmap('.temp/'+lesson_time_file_name))

    def load_performance_report(self):

        print("load performance report",
              self.home.performance_std_id_cmb.currentText())

        # check if the student is selected properly
        if self.home.performance_std_id_cmb.currentText() == "সিলেক্ট করুন":
            show_warning_message("শিক্ষার্থী নির্বাচন করা হয়নি",
                                 "শিক্ষার্থী নির্বাচন করে পারফর্মেন্স রিপোর্ট দেখুন")

        # get student details from db
        try:
            std_id = self.home.performance_std_id_cmb.currentText().split('_')[
                0]
            student_data = sd().get_data_with_id(std_id)[0]
        except Exception as e:
            print(e)

        # convert tuple to list
        student_data = list(student_data)

        # pass the data to the report generator
        try:
            report_card_name = str(
                student_data[0]) + '_' + student_data[1] + '_report_card.pdf'
            reportCard = Report_Card_Generator(student_data, report_card_name)
            show_confirmation_message(
                "অপেক্ষা করুন!", "পারফর্মেন্স রিপোর্ট তৈরি হচ্ছে")
            reportCard.create_report()

        except Exception as e:
            print(e)

        # open Report folder
        os.startfile('Reports')
