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
        
        self.categories = {
            1: 'নাম_শিখন(Noun)',
            2: 'ক্রিয়া_শিখন(Verb)',
            3: 'সম্পর্ক_শিখন(Association)',
            4: 'কর্মধারা_শিখন(Activity)'
        }
        
        self.lesson_list = os.listdir('Resources')
        self.total_lessons = len(self.lesson_list)	
        self.current_lesson_id = 0
        self.visual_file_content = None
        self.audio_file_path = None
        self.folder_path = None 
        self.video_file_formate = ['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv']
        
        # method 
        self.display_lesson()
        
    def display_lesson(self):  
      
        # read the file path and the folders
        self.folder_path = self.lesson_list[self.current_lesson_id]
        self.folder_path = os.path.join('Resources', self.folder_path)
        print("Current Lesson: ", self.folder_path)
        
       
        self.visual_file_content = os.path.join(self.folder_path, "media.png")
        
        # check if the file is audio or video
        if self.visual_file_content.split('.')[-1] in self.video_file_formate:
            
            print("Play video")
            
             
        else:
                
            # image load
            self.qt_image = QPixmap(self.visual_file_content)
            self.qt_image = self.qt_image.scaledToHeight(550, Qt.SmoothTransformation)
            self.lesson_window.lsn_lbl_image.setPixmap(self.qt_image)

            # audio load
            self.audio_file_path = os.path.join(self.folder_path, "audio.wav")
            QSound(self.audio_file_path)
            self.music_player = MusicPlayer(self.audio_file_path)
            self.music_player.start_music()
        
        # read content json
        json_file_path = os.path.join(self.folder_path, "content.json")
        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # set the description of the image
        self.lesson_window.lsn_lbl_lesson_topic.setText(json_data["lesson_topic"])
        content_type = self.categories[json_data["category_id"]]
        lesson_name = content_type + '_' + 'পাঠ_' + str(json_data["lesson_id"])
        
        # read the lesson name
        self.lesson_window.lbl_lesson_headline.setText(lesson_name)
            
    def load_next_lesson(self):
        self.current_lesson_id += 1

        if self.current_lesson_id >= self.total_lessons:
            self.current_lesson_id = 0

        self.reset_lesson_window()
        self.display_lesson()
 
    
    def load_previous_lesson(self):
        
        if self.current_lesson_id > 0:
            self.current_lesson_id -= 1
            self.display_lesson()
    
    def stop_music(self):
        if self.music_player is not None:
            self.music_player.stop_music()

    def reset_lesson_window(self):
        
        self.visual_file_content = None
        self.audio_file_path = None 
        self.folder_path = None
        