import json
import os

from PyQt5.QtMultimedia import QSound
from Backend.AudioPlayer import MusicPlayer
from Frontend.Student_UI import ui_home
from Frontend.src.Document_Formatter import *
from Frontend.src.Lesson import Lesson_Window
from Frontend.src.Puzzle import Puzzle_Window, PuzzleWidget

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
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("শিখবে সবাই")
        set_drop_shadow(self.home.btn_lesson)

        # Navigate between pages
        self.home.stackedWidget.setCurrentWidget(self.home.home_page) 

        # Start a timer to load the lesson widget after 2 seconds
        QTimer.singleShot(2000, self.evaluation_page)

    def lesson_page(self):
        
        # load & set up the LESSON page
        self.lesson_window = Lesson_Window(self.home)
        self.home.stackedWidget.setCurrentWidget(self.home.lesson_page) 
                
        # connect buttons to functions
        self.home.btn_next_lesson.clicked.connect(self.lesson_window.load_next_lesson)
        self.home.btn_prev_lesson.clicked.connect(self.lesson_window.load_previous_lesson)
        
    def evaluation_page(self):
        
        # load & set up the Puzzle page
        # self.evaluation_window = Evaluation_Window(self.home)
        self.puzzle_window = Puzzle_Window(self.home)
        self.home.stackedWidget.setCurrentWidget(self.home.evaluation_page)
        
        self.puzzle_window.launch_puzzle()
    
    def closeEvent(self, event):
        # For example, you can show a message box asking the user if they really want to quit the application
        reply = QMessageBox.question(self, 'সফটওয়্যার বন্ধ করুন', 'আপনি কি সফটওয়্যারটি বন্ধ করতে চান?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            if self.lesson_window is not None:
                self.lesson_window.quit_music()
            event.accept()
        else:
            event.ignore()

