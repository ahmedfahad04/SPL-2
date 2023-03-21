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
        folder_path = "Resources/নাম_শিখন(Noun)_পাঠ_1"

        # read the lesson name
        lesson_name = os.path.basename(folder_path)
        self.home.lbl_lesson_headline.setText(lesson_name)

        # image load
        image_file_path = os.path.join(folder_path, "image.jpeg")
        self.qt_image = QPixmap(image_file_path)
        self.qt_image = self.qt_image.scaledToHeight(550, Qt.SmoothTransformation)
        self.home.lbl_image.setPixmap(self.qt_image)

        # audio load
        audio_file_path = os.path.join(folder_path, "audio.wav")
        audio = QSound(audio_file_path)
        music_player = MusicPlayer(audio_file_path)
        music_player.start_music()
        # lesson change hoile
            # music_player.stop_music()


        # read content json
        json_file_path = os.path.join(folder_path, "content.json")
        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # set the description of the image
        self.home.lbl_image_text.setText(json_data["lesson_topic"])

    def closeEvent(self, event):
        # stop the player
        self.music_player.stop()

        # exit the application
        # app.quit()
