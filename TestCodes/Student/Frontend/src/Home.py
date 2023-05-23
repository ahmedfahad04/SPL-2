import json
import os

from PyQt5.QtMultimedia import QSound
from Backend.AudioPlayer import MusicPlayer
from Frontend.Student_UI import ui_home
from Frontend.src.Document_Formatter import *
from Frontend.src.Lesson import Lesson_Window
from Frontend.src.Puzzle import Puzzle_Window

class Home(QMainWindow):  # Home extends QMainWindow

    def __init__(self):
        
        super(QMainWindow, self).__init__()
        self.lesson_window = None
        self.music_player = None 
        self.home = None 
        
        self.home_page()
        self.celebration_page()

    def home_page(self):
       
        # load & set up the HOME page
        self.home = ui_home.Ui_MainWindow()
        self.home.setupUi(self)

        # set window icon and title
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("শিখবে সবাই")
        set_drop_shadow(self.home.btn_lesson)
        
        # connect buttons
        self.home.n_proceed_btn.clicked.connect(self.puzzle_page)

        # Navigate between pages
        self.home.stackedWidget.setCurrentWidget(self.home.home_page) 

        # Start a timer to load the lesson widget after 2 seconds
        QTimer.singleShot(1000, self.lesson_page)

    def lesson_page(self):
        
        # load & set up the LESSON page
        self.lesson_window = Lesson_Window(self.home)
        self.home.stackedWidget.setCurrentWidget(self.home.lesson_page) 
                
        # connect buttons to functions
        self.home.btn_next_lesson.clicked.connect(self.lesson_window.load_next_lesson)
        self.home.btn_prev_lesson.clicked.connect(self.lesson_window.load_previous_lesson)
        
    def puzzle_page(self):
        
        # load & set up the Puzzle page
        # self.evaluation_window = Evaluation_Window(self.home)
         
        puzzle_frames = [self.home.puzzle_piece_frame, self.home.puzzle_widget_frame]
        
        self.puzzle_window = Puzzle_Window(self.home, puzzle_frames)
        self.home.stackedWidget.setCurrentWidget(self.home.puzzle_page)
        
        self.puzzle_window.launch_puzzle()
        
    def matching_page(self):
        print("Matching page")
        pass 
    
    def sequencing_page(self):
        print("Sequencing page")
        pass
        
    def celebration_page(self):
        
        #! TODO: Mute Unmute Sound
               
        movie = QMovie(r"Frontend\Images\celebration.gif")
        self.home.c_gif.setMovie(movie)
        movie.start()
        
        # Set the label properties
        self.home.c_gif.setScaledContents(True)
        self.home.c_gif.setAlignment(Qt.AlignCenter)
        
        # connect buttons
        self.home.c_again.clicked.connect(self.puzzle_page)
        
        if self.home.stackedWidget.currentWidget() == self.home.puzzle_main:
            self.home.c_next_quiz.clicked.connect(self.matching_page)
        else:
            self.home.c_next_quiz.clicked.connect(self.sequencing_page)

    def closeEvent(self, event):
        # For example, you can show a message box asking the user if they really want to quit the application
        reply = QMessageBox.question(self, 'সফটওয়্যার বন্ধ করুন', 'আপনি কি সফটওয়্যারটি বন্ধ করতে চান?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            if self.lesson_window is not None:
                self.lesson_window.quit_music()
                self.lesson_window.quit_face_tracking()
            event.accept()
        else:
            event.ignore()

