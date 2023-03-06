import json
from Frontend.Teacher_UI import ui_add_lesson, ui_sound_recorder
from document_formatter import *
from Backend.lesson_db import lesson_data as ld
import os, shutil


class Lesson_Manager(QMainWindow):  # Home extends QMainWindow

    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()
        
        # TODO: Video should be added flawlessly

        # window
        self.lesson_window = ui_object
        self.form = None

        # widgets
        self.image_name = None
        self.image_location = None
        self.category_id = 0
        self.lesson_id = 0
        self.lesson_topic = None
        self.audio_name = None
        self.audio_location = None
        self.folder_name = None
        self.content = None
        self.lesson_elements = ld().load_table()
        self.current_category = None 

        # dictionary
        self.categories = {
            1: 'নাম_শিখন(Noun)',
            2: 'ক্রিয়া_শিখন(Verb)',
            3: 'সম্পর্ক_শিখন(Association)',
            4: 'কর্মধারা_শিখন(Activity)'
        }

        if os.path.exists('../Teacher/Lessons/') == False:
            os.mkdir('../Teacher/Lessons/')
            
        self.load_lessons()

    def create_lesson(self, parentObj):
        
        # load & set up the Add Lesson Page
        parentObj.custom_form = QWidget()
        self.form = ui_add_lesson.Ui_Form()
        self.form.setupUi(parentObj.custom_form)
        # parentObj.hide()
        parentObj.custom_form.show()

        # set window icon and title
        parentObj.custom_form.setWindowIcon(QIcon("../Teacher/Frontend/Images/primary_logo.png"))
        parentObj.custom_form.setWindowTitle("নতুন লেসন তৈরি করুন")

        # connect buttons
        self.form.btn_select_photo.clicked.connect(self.manage_photo)
        self.form.btn_select_audio.clicked.connect(self.manage_audio)
        self.form.btn_record_audio.clicked.connect(lambda: self.record_audio(parentObj))
        self.form.btn_submit.clicked.connect(lambda: self.save_lesson_content(parentObj.custom_form))

    def manage_photo(self):
        # open file dialog box
        openFile = QFileDialog()
        self.image_location = openFile.getOpenFileName()[0]

        # check file is correctly located or not
        if self.image_location is None:
            # TODO: Show warning box
            print("No Image Selected")
            return

        # get and set image name
        self.image_name = self.image_location.split('/')[-1]
        self.form.lbl_photo_name.setText(self.image_name)

        # TODO: Currently we're resizing the image to fit the frame
        # But our plane is to resize the frame so that any image fit according to it's size
        self.qtimg = QPixmap(self.image_location)
        self.qtimg = self.qtimg.scaledToHeight(700, Qt.SmoothTransformation)
        self.lesson_window.lbl_image.setPixmap(self.qtimg)

    def manage_audio(self):

        # open file dialog box
        openFile = QFileDialog()
        self.audio_location = openFile.getOpenFileName()[0]
        self.audio_name = self.audio_location.split('/')[-1]

        # check file is correctly located or not
        if self.audio_location is None:
            # TODO: Show warning box
            print("No Audio Selected")
            return

    def record_audio(self, parentObj):
        
        # load & set up the Add Lesson Page
        parentObj.custom_form = QWidget()
        self.form = ui_sound_recorder.Ui_audioRecorderWidget()
        self.form.setupUi(parentObj.custom_form)
        parentObj.custom_form.show()    
        
        # set window icon and title
        parentObj.custom_form.setWindowIcon(QIcon("../Teacher/Frontend/Images/primary_logo.png"))
        parentObj.custom_form.setWindowTitle("অডিও রেকর্ড করুন")
        
    def save_lesson_content(self, childObj):
        """
            This function saves the lesson content to the database.
        """

        # TODO: Backend need to be connected
        # get & set lesson content name
        self.lesson_topic = self.form.edit_lesson_topic.text()
        self.lesson_window.lbl_image_text.setText(self.lesson_topic)

        # get & set category
        self.category_id = self.form.cmb_category.currentIndex()
        self.lesson_window.cmb_category.setCurrentIndex(self.category_id)

        # get lesson id
        self.lesson_id = self.form.edit_lesson_id.text()
        self.lesson_window.cmb_lessons.addItem(self.lesson_id)
        self.lesson_window.cmb_lessons.setCurrentText(self.lesson_id)

        # make a folder
        self.folder_name = self.categories[self.category_id] + '_পাঠ_' + self.lesson_id
        self.folder_location = '../Teacher/Lessons/' + self.folder_name
        if os.path.exists(self.folder_location) == False:
            os.mkdir(self.folder_location)

        # copy the files
        self.content = {
            "category_id": self.category_id,
            "lesson_id": self.lesson_id,
            "lesson_topic": self.lesson_topic
        }
        with open(self.folder_location + '/' + 'content.json', 'w+') as fp:
            json.dump(self.content, fp)

        # copy the image
        # TODO: Show warning if any box of add lesson window is empty
        shutil.copy2(self.image_location, self.folder_location + '/' + 'image.' + self.image_name.split('.')[1])
        shutil.copy2(self.audio_location, self.folder_location + '/' + 'audio.' + self.audio_name.split('.')[1])
        self.image_location = self.folder_location + '/' + 'image.' + self.image_name.split('.')[1]
        self.audio_location = self.folder_location + '/' + 'audio.' + self.audio_name.split('.')[1]

        # save the data to the database
        # TODO: Show warning while adding duplicate data
        data = [self.category_id, self.lesson_id, self.lesson_topic, self.image_location, self.audio_location]
        ld().add_entry(data)

        childObj.hide()        

    def load_lessons(self):
        
        tmp_lsn_id = set()
               
        # add the lessons to the lesson window
        for element in self.lesson_elements:
            
            print(element)
            
            # extract the content
            cat_id, lsn_id, lsn_topic, img_loc, aud_loc = element 
            tmp_lsn_id.add(str(lsn_id))
            
        self.lesson_window.cmb_lessons.addItems(sorted(tmp_lsn_id))
            
    def on_category_changed(self, index):
        
        self.current_category = str(index)
        print("Current Category: ", self.current_category)
        
        self.lesson_window.cmb_lessons.setCurrentIndex(0)
        
    def on_lesson_changed(self, index):
        
        current_lesson = self.lesson_window.cmb_lessons.itemText(index)
        print("Current Lesson: ", current_lesson)
        
        # add the lessons to the lesson window
        for element in self.lesson_elements:
            
            print(element)
            
            # extract the content
            cat_id, db_lesson, lsn_topic, img_loc, aud_loc = element
            
            print(db_lesson, 'Type: ', type(db_lesson))
            
            if current_lesson == str(db_lesson) and self.current_category == str(cat_id):
                
                print("inside")
                
                # add the content to the lesson window
                self.lesson_window.cmb_lessons.setCurrentText(str(db_lesson))
                self.lesson_window.cmb_category.setCurrentText(str(cat_id))
                self.lesson_window.lbl_image_text.setText(lsn_topic)
                
                self.qtimg = QPixmap(img_loc)
                self.qtimg = self.qtimg.scaledToHeight(700, Qt.SmoothTransformation)
                self.lesson_window.lbl_image.setPixmap(self.qtimg)
                
                # lesson topic to be added