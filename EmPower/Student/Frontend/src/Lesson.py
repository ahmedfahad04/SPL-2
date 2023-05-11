import json
import os

from PyQt5.QtMultimedia import QSound
from Backend.AudioPlayer import MusicPlayer
from Frontend.src.Document_Formatter import *
from PyQt5.QtWidgets import QMainWindow


class Lesson_Window(QMainWindow):
    
    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()

        # window
        self.lesson_window = ui_object
        self.music_player = None 

        # load lesson
        self.load_lesson()
    
    def load_lesson(self):
    
        self.categories = {
            1: 'নাম_শিখন(Noun)',
            2: 'ক্রিয়া_শিখন(Verb)',
            3: 'সম্পর্ক_শিখন(Association)',
            4: 'কর্মধারা_শিখন(Activity)'
        }
        
        # read the file path and the folders
        folder_path = os.listdir('Resources')[0]
        folder_path = os.path.join('Resources', folder_path)

        # image load
        image_file_path = os.path.join(folder_path, "media.png")
        self.qt_image = QPixmap(image_file_path)
        self.qt_image = self.qt_image.scaledToHeight(550, Qt.SmoothTransformation)
        self.lesson_window.lsn_lbl_image.setPixmap(self.qt_image)

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
        self.lesson_window.lsn_lbl_lesson_topic.setText(json_data["lesson_topic"])
        content_type = self.categories[json_data["category_id"]]
        lesson_name = content_type + '_' + 'পাঠ_' + str(json_data["lesson_id"])
        
        # read the lesson name
        self.lesson_window.lbl_lesson_headline.setText(lesson_name)
            
    def load_next_lesson(self):
        pass
    
    def load_previous_lesson(self):
        pass
    
    def stop_music(self):
        if self.music_player is not None:
            self.music_player.stop_music()
