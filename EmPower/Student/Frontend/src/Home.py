import json
import os

from PyQt5.QtMultimedia import QSound

from Backend.AudioPlayer import MusicPlayer
from Frontend.Student_UI import ui_home
from Frontend.src.Document_Formatter import *
from Frontend.src.Lesson import Lesson_Window


class Home(QMainWindow):  # Home extends QMainWindow

    def __init__(self):
        
        super(QMainWindow, self).__init__()
        self.lesson_window = None
        self.music_player = None 
        self.home_page()

    def home_page(self):
        # load & set up the HOME page
        self.home = ui_home.Ui_MainWindow()
        self.home.setupUi(self)

        # set window icon and title
        # TODO: Show the window at the middle of the screen
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("শিখবে সবাই")
        set_drop_shadow(self.home.btn_lesson)

        # Navigate between pages
        self.home.stackedWidget.setCurrentWidget(self.home.home_page)

        # Start a timer to load the lesson widget after 2 seconds
        QTimer.singleShot(2000, self.lesson_page)

    def lesson_page(self):
        self.lesson_window = Lesson_Window(self.home)
        self.home.stackedWidget.setCurrentWidget(self.home.lesson_page)
        self.load_lesson()

    def load_lesson(self):
        
        self.categories = {
            1: 'নাম_শিখন(Noun)',
            2: 'ক্রিয়া_শিখন(Verb)',
            3: 'সম্পর্ক_শিখন(Association)',
            4: 'কর্মধারা_শিখন(Activity)'
        }
        
        # read the file path and the folders
        folder_path = os.listdir('Resources')[1]
        folder_path = os.path.join('Resources', folder_path)

        # image load
        image_file_path = os.path.join(folder_path, "media.png")
        self.qt_image = QPixmap(image_file_path)
        self.qt_image = self.qt_image.scaledToHeight(550, Qt.SmoothTransformation)
        self.home.lsn_lbl_image.setPixmap(self.qt_image)

        # audio load
        audio_file_path = os.path.join(folder_path, "audio.wav")
        QSound(audio_file_path)
        self.music_player = MusicPlayer(audio_file_path)
        self.music_player.start_music()

        # lesson change hoile
        # music_player.stop_music()

        # read content json
        json_file_path = os.path.join(folder_path, "content.json")
        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # set the description of the image
        self.home.lsn_lbl_lesson_topic.setText(json_data["lesson_topic"])
        content_type = self.categories[json_data["category_id"]]
        lesson_name = content_type + '_' + 'পাঠ_' + str(json_data["lesson_id"])
        
        # read the lesson name
        self.home.lbl_lesson_headline.setText(lesson_name)
        
    def load_next_lesson(self):
        pass
    
    def load_previous_lesson(self):
        pass

    def closeEvent(self, event):
        
        self.music_player.stop_music()
        
        reply = QMessageBox.question(
            self, 'সফটওয়্যার বন্ধ করুন', 'আপনি কি সফটওয়্যারটি বন্ধ করতে চান?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            self.music_player.stop_music()
            event.accept()
            print('Window closed')
        else:
            event.ignore()

