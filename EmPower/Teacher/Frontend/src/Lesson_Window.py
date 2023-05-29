from Frontend.Teacher_UI import ui_add_lesson, ui_sound_recorder
from Backend.VideoPlayer.video_player import Window
from Frontend.src.Document_Formatter import *
from Backend.Database.module_db import module_data as md
from Backend.MediaRecorder import audioRecorder
from PyQt5.QtCore import QTimer, QTime, Qt
import os
import shutil
import glob
import json
import datetime


class Lesson_Window(QMainWindow):  # Home extends QMainWindow

    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()

        # window
        self.lesson_window = ui_object
        self.form = None

        # widgets
        self.media_file_name = None
        self.media_file_location = None
        self.category_id = 0
        self.lesson_id = 0
        self.lesson_topic = None
        self.audio_name = None
        self.audio_location = None
        self.folder_name = None
        self.content = None
        self.lesson_elements = md().load_table('*')
        self.current_category = None
        self.category_lesson_mappings = dict()
        self.lesson_window.lsn_cmb_lessons.clear()
        self.lesson_window.lsn_cmb_category.setCurrentIndex(0)
        self.lesson_window.lsn_lbl_lesson_image.clear()
        
        # disable the first option of lsb_cmb_category
        self.lesson_window.lsn_cmb_category.setItemData(0, 0, Qt.UserRole - 1)

        # dictionary
        self.categories = {
            1: 'নাম_শিখন(Noun)',
            2: 'ক্রিয়া_শিখন(Verb)',
            3: 'সম্পর্ক_শিখন(Association)',
            4: 'কর্মধারা_শিখন(Activity)'
        }

        self.videoFormat = ['mp4', 'avi', 'mkv',
                            'flv', 'wmv', 'mov', '3gp', 'webm']

        self.audioFormat = ['mp3', 'wav', 'ogg', 'wma', 'aac', 'flac', 'm4a']

        # self.load_lessons()

    def create_lesson(self):

        print("lesson creation")

        # load & set up the Add Lesson Page
        # TODO: Audio file name should be shown in the sub window
        custom_form = QWidget()
        self.form = ui_add_lesson.Ui_Form()
        self.form.setupUi(custom_form)
        # custom_form.setWindowModality(Qt.ApplicationModal)
        custom_form.show()
        

        # set window icon and title
        custom_form.setWindowIcon(
            QIcon("../Teacher/Frontend/Images/primary_logo.png"))
        custom_form.setWindowTitle("নতুন লেসন তৈরি করুন")

        # connect buttons
        self.form.btn_select_photo.clicked.connect(self.manage_media)
        self.form.btn_select_audio.clicked.connect(self.manage_audio)
        self.form.btn_record_audio.clicked.connect(self.record_audio)
        self.form.btn_submit.clicked.connect(
            lambda: self.save_lesson_content(custom_form))
        self.form.cmb_category.currentIndexChanged.connect(
            self.on_lsn_creating_category_changed)

    def manage_media(self):

        # open file dialog box
        self.media_file_location = QFileDialog.getOpenFileName(self, "Open File")[
            0]

        # check file is correctly located or not
        if self.media_file_location is None:
            # TODO: Show warning box
            print("No Image Selected")
            return

        # check file format
        file_format = self.media_file_location.split('.')[-1]

        if file_format in self.videoFormat:

            # navigate to video page
            self.lesson_window.mediaStackWidget.setCurrentWidget(
                self.lesson_window.video_page)

            # get and set image name
            self.media_file_name = self.media_file_location.split('/')[-1]
            self.form.lbl_photo_name.setText(self.media_file_name)

        else:
            self.lesson_window.mediaStackWidget.setCurrentWidget(
                self.lesson_window.image_page)

            # TODO: Currently we're resizing the image to fit the frame
            # But our plane is to resize the frame so that any image fit according to it's size
            self.qtimg = QPixmap(self.media_file_location)
            self.qtimg = self.qtimg.scaledToHeight(
                700, Qt.SmoothTransformation)
            self.lesson_window.lsn_lbl_lesson_image.setPixmap(self.qtimg)

            # get and set image name
            self.media_file_name = self.media_file_location.split('/')[-1]
            self.form.lbl_photo_name.setText(self.media_file_name)

    def manage_audio(self):

        # open file dialog box
        openFile = QFileDialog()
        self.audio_location = openFile.getOpenFileName()[0]
        self.audio_name = self.audio_location.split('/')[-1]
        self.form.lbl_audio.setText(self.audio_name)

        # check file is correctly located or not
        if self.audio_location is None:
            # TODO: Show warning box
            print("No Audio Selected")
            return

    def record_audio(self):

        # load & set up the Add Lesson Page
        custom_form = QWidget()
        self.audio_form = ui_sound_recorder.Ui_audioRecorderWidget()
        self.audio_form.setupUi(custom_form)

        custom_form.show()

        # set window icon and title
        custom_form.setWindowIcon(
            QIcon("../Teacher/Frontend/Images/primary_logo.png"))
        custom_form.setWindowTitle("অডিও রেকর্ড করুন")

        # before start recording
        self.audio_form.stopButton.setEnabled(False)
        self.audio_form.soundingButton.setEnabled(False)
        self.audio_form.recordingTime.setText("00:00:00")
        self.audio_form.recordingTime.setAlignment(Qt.AlignCenter)
        # Set the initial time to 0
        self.time = QTime(0, 0, 0)
        # Create a timer that updates every second
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        # now record the audio
        recorder = audioRecorder.AudioRecorder()
        self.audio_form.startButton.clicked.connect(
            lambda: self.start_recording(recorder))
        self.audio_form.stopButton.clicked.connect(
            lambda: self.stop_recording(recorder))

        # close the audio form
        self.audio_form.saveButton.clicked.connect(
            lambda: self.save_audio(custom_form))

    def start_recording(self, recorder):
        # start recording
        self.audio_form.stopButton.setEnabled(True)
        self.audio_form.soundingButton.setEnabled(True)
        self.audio_form.startButton.setStyleSheet(
            "background-color:  rgb(255, 131, 139); border-radius: 50px;")
        recorder.start_recording()
        # Start the timer
        self.time = QTime(0, 0, 0)
        self.timer.start()

    def stop_recording(self, recorder):
        # stop recording
        self.audio_form.stopButton.setEnabled(False)
        self.audio_form.soundingButton.setEnabled(False)
        self.audio_form.startButton.setStyleSheet(
            "border-radius: 50px; border: 3px solid rgb(206, 95, 95)")
        recorder.stop_recording()
        # Stop the timer
        self.timer.stop()

    def update_timer(self):
        # Increment the time by one second
        self.time = self.time.addSecs(1)

        # Update the label with the new time
        self.audio_form.recordingTime.setText(self.time.toString("hh:mm:ss"))

    def save_audio(self, form):
        audio_fileName = self.audio_form.fileName.text()

        print(audio_fileName)
        # TODO: audio file backend er location a save ache
        # eitake ekhn kothay save kore rakhbi korte paros
        # backend er folder theke copy kore niye lesson er folder a o rakhte paros
        self.audio_location = 'Backend/MediaRecorder/audio.wav'
        self.audio_name = self.audio_location.split('/')[-1]

        form.close()

    def save_lesson_content(self, childObj):
        """
            This function saves the lesson content to the database.
        """
        
        # get & set lesson content name
        self.lesson_topic = self.form.edit_lesson_topic.text()
        self.lesson_window.lsn_lbl_lesson_topic.setText(self.lesson_topic)

        # get & set category
        self.category_id = self.form.cmb_category.currentIndex()
        self.lesson_window.lsn_cmb_category.setCurrentIndex(self.category_id)

        # get lesson id
        self.lesson_id = self.form.edit_lesson_id.text()
        self.lesson_window.lsn_cmb_lessons.addItem(self.lesson_id)

        # !category must be selected
        if self.category_id == 0:
            show_warning_message("সতর্কতা!!", "ক্যাটাগরি নির্বাচন করুন")
            return

        # !lesson id and topic must be selected
        if self.lesson_id == "" or self.lesson_topic == "":
            show_warning_message("সতর্কতা!!", "পাঠের নাম এবং পাঠ নম্বর দিন")
            return

        # make a folder
        self.folder_name = self.categories[self.category_id] + \
            '_মডিউল_' + self.lesson_id
        self.folder_location = 'Lessons/মডিউলসমূহ/' + self.folder_name
        if os.path.exists(self.folder_location) == False:
            os.mkdir(self.folder_location)

        # copy the image
        # !Show warning if any box of add lesson window is empty
        if self.media_file_name is None:
            show_warning_message("সতর্কতা!!", "ছবি/ভিডিও নির্বাচন করুন")
            return

        # check for video format
        if self.media_file_name.split('.')[1] not in self.videoFormat:

            if self.audio_location is None:
                show_warning_message("সতর্কতা!!", "অডিও নির্বাচন করুন")
                return

            shutil.copy2(self.audio_location, self.folder_location +
                         '/' + 'audio.' + self.audio_name.split('.')[1])

        shutil.copy2(self.media_file_location, self.folder_location +
                     '/' + 'media.' + self.media_file_name.split('.')[1])

        # copy the files
        self.content = {
            "category_id": self.category_id,
            "module_id": self.lesson_id,
            "module_topic": self.lesson_topic
        }

        with open(self.folder_location + '/' + 'content.json', 'w+') as fp:
            json.dump(self.content, fp)

        # save the data to the database
        # Show warning while adding duplicate data
        data = [self.category_id, self.lesson_id,
                self.lesson_topic, self.folder_location]
        md().add_entry(data)
        
        show_success_message("সফলতা!!", "পাঠ সংরক্ষণ করা হয়েছে, এখন স্ক্রিনের নিচে থাকা রিলোড বাটনে ক্লিক করুন")
        
        self.lesson_window.lsn_cmb_lessons.clear()
        # self.lesson_window.lsn_lbl_lesson_image.clear()
        # self.lesson_window.lsn_lbl_lesson_topic.clear()
        # self.lesson_window.lsn_cmb_category.setCurrentIndex(0)
        
        childObj.hide()

    def load_lessons(self):

        tmp_lsn_id = set()
        tmp_cat_lsn_pairs = list()

        # add the lessons to the lesson window
        for element in self.lesson_elements:
            print("-->", element)

            # extract the content
            cat_id, lsn_id, lsn_topic, media_loc = element
            tmp_lsn_id.add(str(lsn_id))
            tmp_cat_lsn_pairs.append((cat_id, lsn_id))

        for key, value in tmp_cat_lsn_pairs:
            if key not in self.category_lesson_mappings:
                self.category_lesson_mappings[key] = [value]
            else:
                self.category_lesson_mappings[key].append(value)

        self.lesson_window.lsn_cmb_lessons.addItems(sorted(tmp_lsn_id))

    def on_category_changed(self, index):

        self.current_category = str(index)
        print("Current Category: ", self.current_category)

        self.lesson_elements = md().load_table(index)
        print("Lesson Elements: ", self.lesson_elements)
        
        if len(self.lesson_elements) > 0:
            self.lesson_window.lsn_cmb_lessons.clear()
            for value in self.lesson_elements:
                lsn_id = value[1]
                self.lesson_window.lsn_cmb_lessons.addItem(str(lsn_id))
                print("LSN: "+str(lsn_id))
        elif index > 0:
            show_confirmation_message("লেসন যুক্ত হয়নি", "এখনো কোন লেসন এই ক্যাটাগরিতে যুক্ত করা হয়নি")
            print(f"No lessons found for categoryc-> {self.current_category}")
      
    def on_lesson_changed(self, index):       
        
        current_lesson = self.lesson_window.lsn_cmb_lessons.itemText(index)
        print("Current Lesson--: ", current_lesson)

        # add the lessons to the lesson window
        for element in self.lesson_elements:

            # extract the content
            cat_id, db_lesson, lsn_topic, media_loc = element

            print(cat_id, db_lesson, lsn_topic, 'Type: ', type(db_lesson))

            if current_lesson == str(db_lesson) and self.current_category == str(cat_id):

                # add the content to the lesson window
                self.lesson_window.lsn_cmb_lessons.setCurrentText(
                    str(db_lesson))
                self.lesson_window.lsn_cmb_category.setCurrentText(str(cat_id))
                self.lesson_window.lsn_lbl_lesson_topic.setText(lsn_topic)

                print("Media Location: ", media_loc)
                media_loc = glob.glob(media_loc+'/media.*')[0]
                file_extension = media_loc.split('.')[-1]

                if file_extension in self.videoFormat:

                    if self.lesson_window.video_player_widget.count() != 0:
                        self.lesson_window.video_player_widget.itemAt(
                            0).widget().setParent(None)

                    self.lesson_window.mediaStackWidget.setCurrentWidget(
                        self.lesson_window.video_page)

                    video_player = Window(media_loc)
                    self.lesson_window.video_player_widget.addWidget(video_player)

                else:
                    self.lesson_window.mediaStackWidget.setCurrentWidget(
                        self.lesson_window.image_page)

                    print('IMG LOC: ', media_loc)

                    self.qtimg = QPixmap(media_loc)
                    self.qtimg = self.qtimg.scaledToHeight(
                        700, Qt.SmoothTransformation)
                    self.lesson_window.lsn_lbl_lesson_image.setPixmap(
                        self.qtimg)

    def on_lsn_creating_category_changed(self, index):

        current_category = str(index)
        print("Current Category: ", current_category)
        
        self.lesson_elements = md().load_table(index)
        
        if len(self.lesson_elements) > 0:

            # category_wise_lesson = len(self.category_lesson_mappings[index])
            category_wise_lesson = len(self.lesson_elements)
            self.form.lbl_lsn_cat_status.setText(
                f"এই ক্যাটেগরি তে মোট পাঠ সংখ্যা: {category_wise_lesson}, নতুন পাঠ {category_wise_lesson+1} থেকে শুরু করুন ")

        else:
            self.form.lbl_lsn_cat_status.setText(
                f"এই ক্যাটেগরি এখনো কোন পাঠ নেই, নতুন পাঠ 1 থেকে শুরু করুন")

