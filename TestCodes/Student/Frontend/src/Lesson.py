import glob
import json
import os
import subprocess

from PyQt5.QtMultimedia import QSound
from Backend.AudioPlayer import MusicPlayer
from Backend.VideoPlayer import Window
from Frontend.src.Document_Formatter import *
from PyQt5.QtWidgets import QMainWindow
import shutil
from Backend.track import FaceTracker
import threading

# from pydub import AudioSegment

class Lesson_Window(QMainWindow):

    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()

        # window
        self.threadController = None
        self.lesson_window = ui_object

        self.categories = {
            1: 'নাম_শিখন(Noun)',
            2: 'ক্রিয়া_শিখন(Verb)',
            3: 'সম্পর্ক_শিখন(Association)',
            4: 'কর্মধারা_শিখন(Activity)'
        }

        # class variables
        self.lesson_list = [folder for folder in os.listdir('Resources') if folder.startswith('পাঠ')]
        self.total_lessons = len(self.lesson_list)
        self.current_lesson_id = 0
        self.total_modules = 0
        self.current_module_id = 0
        self.visual_file_content = None
        self.audio_file_path = None
        self.folder_path = None
        self.video_file_formate = ['mp4', 'avi', 'mov', 'wmv', 'flv', 'mkv']
        self.video_player = None
        self.music_player = None
        self.time_elapsed = 0

        # tracking obj
        self.tracker = None

        # switch lesson in every 10 seconds
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.load_next_lesson)
        # self.timer.start(10000)  # rotate every 10 seconds

        # # start the timer to count the elapsed time
        # self.elapsed_timer = QTimer()
        # self.elapsed_timer.timeout.connect(self.update_elapsed_time)
        # self.elapsed_timer.start(1000)  # update every 1 second

        # method
        self.display_lesson()

    def display_lesson(self):

        ##### face tracking code Starts #####
        self.tracker = FaceTracker(self.current_lesson_id)
        self.tracker.start()
        ##### face tracking code Ends #####

        # read the file path and the folders
        self.folder_path = self.lesson_list[self.current_lesson_id]
        self.folder_path = os.path.join('Resources', self.folder_path)
        folder_name = filter_data(self.folder_path.split('\\')[-1])

        self.module_path = os.listdir(self.folder_path)[self.current_module_id]
        self.module_path = os.path.join(self.folder_path, self.module_path)
        self.module_path = os.path.join(os.getcwd(), self.module_path)
        self.total_modules = len(os.listdir(self.folder_path))
        module_name = filter_data(self.module_path.split('\\')[-1])
        print("LESSONID :", self.current_lesson_id)
        print("MODULEID :", self.current_module_id)

        # read audio/video file path
        self.visual_file_content = glob.glob(self.module_path + '/media.*')[0]
        print("Visual File: ", self.visual_file_content)

        # check if the file is audio or video
        if self.visual_file_content.split('.')[-1] in self.video_file_formate:

            if self.lesson_window.video_player_widget.count() != 0:
                self.lesson_window.video_player_widget.itemAt(0).widget().setParent(None)

            self.lesson_window.mediaStackWidget.setCurrentWidget(self.lesson_window.video_page)

            self.video_player = Window(self.visual_file_content)
            self.lesson_window.video_player_widget.addWidget(self.video_player)

            if self.music_player is not None:
                if (self.audio_output_device):
                    self.music_player.stop_music()

        else:

            # stop the video player
            if self.video_player:
                self.video_player.mediaPlayer.stop()
                self.video_player.close()

            self.lesson_window.mediaStackWidget.setCurrentWidget(self.lesson_window.image_page)

            # image load
            self.qt_image = QPixmap(self.visual_file_content)
            self.qt_image = self.qt_image.scaledToWidth(self.lesson_window.lsn_lbl_image.width(),
                                                        Qt.SmoothTransformation)
            self.lesson_window.lsn_lbl_image.setPixmap(self.qt_image)
            self.lesson_window.lsn_lbl_image.setFixedSize(self.lesson_window.lsn_lbl_image.width(),
                                                          self.lesson_window.lsn_lbl_image.width())

            # audio load
            audio_file_name = (glob.glob(self.module_path + '/audio.*')[0]).split('\\')[-1]
            audio_formate = audio_file_name.split('.')[-1]

            # ! TODO: Renme audio file name to mp3

            self.audio_file_path = os.path.join(self.module_path, audio_file_name)
            QSound(self.audio_file_path)
            self.music_player = MusicPlayer(self.audio_file_path)

            self.audio_output_device = False
            if self.music_player.check_audio_devices():
                self.audio_output_device = True

            if (self.audio_output_device):
                self.music_player.start_music()

        # read content json
        json_file_path = os.path.join(self.module_path, "content.json")
        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # set the description of the image
        self.lesson_window.lsn_lbl_lesson_topic.setText(json_data["module_topic"])
        content_type = self.categories[json_data["category_id"]]
        lesson_name = content_type + '_' + 'মডিউল_' + str(json_data["module_id"])

        # read the lesson name
        self.lesson_window.lbl_lesson_headline.setText(folder_name)
        self.lesson_window.lbl_lesson_sub_heading.setText(module_name)

    def load_next_lesson(self):

        self.current_module_id += 1
        finish = False

        # change module when button pressed
        # the module of one lesson is done then change the lesson
        if self.current_module_id >= self.total_modules:
            self.current_module_id = 0
            self.current_lesson_id += 1

        # change lesson when button pressed
        # if all the lesson is done then change the lesson
        if self.current_lesson_id >= self.total_lessons:
            self.current_lesson_id = 0
            finish = True
            self.change_window()

        if finish == False:
            ##### face tracking code Starts #####
            # To stop the tracking:
            self.tracker.get_total_time()
            self.quit_face_tracking()
            ##### face tracking code Ends #####
            self.reset_lesson_window()
            self.display_lesson()

    def load_previous_lesson(self):

        if self.current_module_id > 0:
            self.current_module_id -= 1
            ##### face tracking code Starts #####
            # To stop the tracking:
            self.tracker.get_total_time()
            self.quit_face_tracking()
            ##### face tracking code Ends #####
        self.reset_lesson_window()
        self.display_lesson()

    def quit_music(self):
        if self.music_player is not None:
            if (self.audio_output_device):
                self.music_player.stop_music()

    def reset_lesson_window(self):

        self.visual_file_content = None
        self.audio_file_path = None
        self.module_path = None
        self.time_elapsed = 0

    def update_elapsed_time(self):
        print("TIME: ", self.time_elapsed)
        self.time_elapsed += 1
        print("Time elapsed:", self.time_elapsed, "seconds")

    def change_window(self):
        self.quit_music()
        self.quit_face_tracking()
        self.lesson_window.stackedWidget.setCurrentWidget(self.lesson_window.navigation_page)

    def quit_face_tracking(self):
        self.tracker.stop()
        self.tracker.quit()