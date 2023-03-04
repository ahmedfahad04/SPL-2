from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from Frontend.Teacher_UI import ui_add_lesson, ui_lesson_manager
from Frontend.Teacher_UI import ui_add_lesson
from Backend.connectDB import Database_Manager as dm
from document_formatter import *
from Frontend.Teacher_UI import ui_sound_recorder
from Backend.MediaRecorder.audioRecorder import AudioRecorder


class Lesson_Manager(QMainWindow):  # Home extends QMainWindow

    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()

        self.audio_recorder_q_widget = None
        self.lesson_window = ui_object
        self.form = None

    def create_lesson(self, parentObj):
        # load & set up the Add Lesson Page
        parentObj.custom_form = QWidget()
        self.form = ui_add_lesson.Ui_Form()
        self.form.setupUi(parentObj.custom_form)
        parentObj.hide()
        parentObj.custom_form.show()

        # set window icon and title
        parentObj.custom_form.setWindowIcon(QIcon("../EmPower/Frontend/Images/primary_logo.png"))
        parentObj.custom_form.setWindowTitle("নতুন লেসন তৈরি করুন")

        # connect buttons
        self.form.btn_select_photo.clicked.connect(self.manage_photo)
        # self.form.btn_select_audio.clicked.connect(self.add_audio)
        self.form.btn_record_audio.clicked.connect(self.audio_record_manager)
        self.form.btn_submit.clicked.connect(lambda: self.save_lesson_content(parentObj, parentObj.custom_form))

    def manage_photo(self):
        openFile = QFileDialog()
        file_location = openFile.getOpenFileName()[0]

        if file_location is None:
            # TODO: Show warning box
            print("No File Selected")
            return

        self.qtimg = QPixmap(file_location)

        # TODO: Currently we're resizing the image to fit the frame
        # But our plane is to resize the frame so that any image fit according to it's size
        print(self.qtimg.rect())

        self.qtimg = self.qtimg.scaled(500, 500)
        self.lesson_window.lbl_add_picture.setMinimumSize(QSize(500, 500))
        self.lesson_window.lbl_add_picture.setPixmap(self.qtimg)
        self.form.lbl_photo_name.setText(file_location)
        print(file_location)

    def audio_record_manager(self):
        # set and load the recording widget
        self.audio_recorder_q_widget = QWidget()
        audio_recorder_widget = ui_sound_recorder.Ui_audioRecorderWidget()
        audio_recorder_widget.setupUi(self.audio_recorder_q_widget)
        self.audio_recorder_q_widget.show()

        # set widget icon and title
        self.audio_recorder_q_widget.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.audio_recorder_q_widget.setWindowTitle("অডিও রেকর্ডিং উইন্ডো")

        # handel the operations
        recorder = AudioRecorder()
        audio_recorder_widget.startButton.clicked.connect(lambda: self.start_recording(recorder))
        audio_recorder_widget.stopButton.clicked.connect(lambda: self.stop_recording(recorder))
        audio_recorder_widget.saveButton.clicked.connect(lambda: self.save_recording(audio_recorder_widget, recorder))


    def start_recording(self, recorder):
        recorder.start_recording()

    def stop_recording(self, recorder):
        recorder.stop_recording()

    def save_recording(self, audio_recorder_widget, recorder):
        file_name = audio_recorder_widget.fileName.text()
        recorder.set_fileName(file_name)
        recorder.quitCommandFlag()
        recorder.stop_recording()


    def save_lesson_content(self, parentObj, childObj):
        """
            This function saves the lesson content to the database.
        """
        childObj.hide()
        parentObj.show()
