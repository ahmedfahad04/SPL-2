import glob
import json
import os

from PyQt5.QtMultimedia import QSound
from Backend.AudioPlayer import MusicPlayer
from Frontend.Student_UI import ui_home
from Frontend.src.Document_Formatter import *
from Frontend.src.Lesson import Lesson_Window
from Frontend.src.Matching import Matching_Window
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
        QTimer.singleShot(1000, self.matching_page)

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
        
        # show current window
        self.home.stackedWidget.setCurrentWidget(self.home.matching_page)
        
        # make object of Matching Window
        self.matching_window = Matching_Window(self.home)
        self.matching_window.load_matching_images()
        
        # load all images
        # self.load_matching_images()
        
    def load_matching_images(self):
        
        folder_pattern = "Resources/m_*"  # Pattern to match folders starting with "m_"
        folder_images = []
        image_tag_dict = {}
        image_tags = []
        

        # Get a list of matching folder paths
        matching_folder = glob.glob(folder_pattern)[0]
        folder_files = os.listdir(matching_folder)
        folder_images = [file for file in folder_files if file.endswith(".png")]
        
        # read image tags from json file
        with open(matching_folder + "/image_data.json", "r") as json_file:
            image_tag_dict = json.load(json_file)
            
            #? update the keys of image_tag_dict to remove set6/ from the key
            image_tag_dict = {key.replace("set6/", ""): value for key, value in image_tag_dict.items()}
            
            # include only those values that are images 
            image_tag_dict = {key: value for key, value in image_tag_dict.items() if key in folder_images}
            
            # fill the image tags 
            image_tags = list(image_tag_dict.values())
            
        # fill the image option labels with image_tags 
        self.home.mat_txt_option_1.setText(image_tags[0])
        self.home.mat_txt_option_2.setText(image_tags[1])
        self.home.mat_txt_option_3.setText(image_tags[2])
        self.home.mat_txt_option_4.setText(image_tags[3]) 
        
        # fill the image labels with images
        
        # change the aspect ration so that it fit any kind of lable
        self.home.mat_img_lbl_1.setScaledContents(True)
        self.home.mat_img_lbl_2.setScaledContents(True)
        self.home.mat_img_lbl_3.setScaledContents(True)
        self.home.mat_img_lbl_4.setScaledContents(True)
        
        self.home.mat_img_lbl_1.setPixmap(QPixmap(matching_folder + "/" + folder_images[0]))
        self.home.mat_img_lbl_2.setPixmap(QPixmap(matching_folder + "/" + folder_images[1]))
        self.home.mat_img_lbl_3.setPixmap(QPixmap(matching_folder + "/" + folder_images[2]))
        self.home.mat_img_lbl_4.setPixmap(QPixmap(matching_folder + "/" + folder_images[3]))          
        
        print(folder_images)
       

    
    def sequencing_page(self):
        
        self.home.stackedWidget.setCurrentWidget(self.home.sequence_page)
        
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
            event.accept()
        else:
            event.ignore()

