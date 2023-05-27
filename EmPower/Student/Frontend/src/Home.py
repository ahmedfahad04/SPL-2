import glob
import json
import os
import shutil
import time

from PyQt5.QtMultimedia import QSound
from Backend.AudioPlayer import MusicPlayer
from Frontend.Student_UI import ui_home
from Frontend.src.Document_Formatter import *
from Frontend.src.Lesson import Lesson_Window
from Frontend.src.MCQ import MCQ_Window
from Frontend.src.Matching import Matching_Window
from Frontend.src.Puzzle import Puzzle_Window
from Frontend.src.Sequence import Sequence_Window

class Home(QMainWindow):  # Home extends QMainWindow

    def __init__(self):
        
        super(QMainWindow, self).__init__()
        self.lesson_window = None
        self.music_player = None 
        self.home = None 
        self.current_window = 'MCQ'
        self.current_lesson_id = None
        self.start_time = time.time()
        self.lesson_completion_data = {}
        # self.current_mcq_question = 1
        # self.mcq_data = {}
        # self.total_mcq_questions = 0
        
        #! TODO: Handle student id and name
        
        self.home_page()
        
    def home_page(self):
        
        print("Home Page")
       
        # load & set up the HOME page
        self.home = ui_home.Ui_MainWindow()
        self.home.setupUi(self)

        # set window icon and title
        self.setWindowIcon(QIcon("Frontend/Images/primary_logo.png"))
        self.setWindowTitle("শিখবে সবাই")
        set_drop_shadow(self.home.btn_lesson)
        
        # create folders 
        os.path.exists('Performance') or os.makedirs('Performance')
        
        # connect buttons
        self.home.n_proceed_btn.clicked.connect(self.puzzle_page)

        # Navigate between pages
        self.home.stackedWidget.setCurrentWidget(self.home.home_page)
        
        # Start a timer to load the lesson widget after 2 seconds
        QTimer.singleShot(1000, self.lesson_page)

    def lesson_page(self):
        
        print("Lesson Page"	)
        self.current_window = "Lesson"
        
        # load & set up the LESSON page
        self.lesson_window = Lesson_Window(self.home)
        self.home.stackedWidget.setCurrentWidget(self.home.lesson_page)
        
        # load current lesson name from Resource folder
        self.load_current_lesson_name()
                
        # set and get current lesson status
        self.config_current_lesson_status()
                      
        # connect buttons to functions
        self.home.btn_next_lesson.clicked.connect(self.lesson_window.load_next_lesson)
        self.home.btn_prev_lesson.clicked.connect(self.lesson_window.load_previous_lesson)
        
    def load_current_lesson_name(self):
        resource_files = os.listdir("Resources")
        for file in resource_files:
            if "পাঠ" in file:
                
                lesson_name = str(file)
                print(lesson_name)
                
                #  Check if the log file exists
                if not os.path.exists('.lesson_completion_log.json'):
                    # Create an empty log file
                    with open('.lesson_completion_log.json', 'w') as outfile:
                        json.dump({}, outfile)
                        
                # check log file to see if the lesson is already completed
                with open('.lesson_completion_log.json') as json_file:
                    data = json.load(json_file)
                    
                    if file in data:
                        print("Lesson already completed")
                
                # if not completed then mark it as current lesson 
                self.current_lesson_id = file.split("_")[1]
        
    def config_current_lesson_status(self):
        
        current_lesson_log_file = '.current_lesson_log.json'

        # Check if the log file exists
        if not os.path.exists(current_lesson_log_file):
            # Create an empty log file
            with open(current_lesson_log_file, 'w') as outfile:
                json.dump({}, outfile)

        # Load the current lesson log
        with open(current_lesson_log_file) as json_file:
            data = json.load(json_file)

        # Get the current lesson ID
        current_lesson_id = self.current_lesson_id
        
        # Check if the 'lessons' key exists in the log
        if 'lessons' not in data:
            # Create an empty 'lessons' dictionary
            data['lessons'] = {}

        # Check if the current lesson exists in the log
        if current_lesson_id not in data['lessons']:
            # Create a new entry for the current lesson
            data['lessons'][current_lesson_id] = {
                "attempt": 1,
                "time": time.time()
            }
        else:
            # Update the attempt for the current lesson
            data['lessons'][current_lesson_id]["attempt"] += 1
            data['lessons'][current_lesson_id]["time"] = time.time()

        # Update the log file with the modified data
        with open(current_lesson_log_file, 'w') as outfile:
            json.dump(data, outfile)
            
    def puzzle_page(self):
        
        self.current_window = "puzzle"
        print("Puzzle Page")
        
        # load & set up the Puzzle page
        # self.evaluation_window = Evaluation_Window(self.home)
         
        puzzle_frames = [self.home.puzzle_piece_frame, self.home.puzzle_widget_frame]
        
        self.puzzle_window = Puzzle_Window(self.home, puzzle_frames)
        self.home.stackedWidget.setCurrentWidget(self.home.puzzle_page)
        
        self.puzzle_window.launch_puzzle()
        self.celebration_page()
        
    def matching_page(self):
        
        print("Matching Page")
        self.current_window = "matching"
        
        # show current window
        self.home.stackedWidget.setCurrentWidget(self.home.matching_page)
        
        # make object of Matching Window
        self.matching_window = Matching_Window(self.home)
        self.matching_window.load_matching_images()
        self.celebration_page()
    
    def sequencing_page(self):
        
        print("Sequence Page")
        self.current_window = "sequencing"
        
        self.home.stackedWidget.setCurrentWidget(self.home.sequence_page)
        
        # load the files from the folder
        self.sequence_window = Sequence_Window(self.home) 
        self.sequence_window.load_sequence_file()  
        self.celebration_page() # need to modify a bit
        
    def mcq_page(self):
        
        print("MCQ Page")
        self.current_window = 'MCQ'
                
        # navigate to mcq page
        self.home.stackedWidget.setCurrentWidget(self.home.mcq_page)
        
        # make object of mcq window
        #! not loading the MCQ Page
        
        self.mcq_window = MCQ_Window(self.home)
        self.mcq_window.load_mcq_question()
        self.celebration_page()
        
        # # connecting buttons
        # self.home.btn_mcq_option_1.clicked.connect(lambda: self.check_answer(self.home.btn_mcq_option_1))
        # self.home.btn_mcq_option_2.clicked.connect(lambda: self.check_answer(self.home.btn_mcq_option_2))
        # self.home.btn_mcq_option_3.clicked.connect(lambda: self.check_answer(self.home.btn_mcq_option_3))
        # self.home.btn_mcq_option_4.clicked.connect(lambda: self.check_answer(self.home.btn_mcq_option_4))
        
        # # read contents
        # folder_pattern = "Resources/q_*"  # Pattern to match folders starting with "m_"

        # # Get a list of matching folder paths
        # self.matching_folder = glob.glob(folder_pattern)[0]
        # self.folder_set_name = self.matching_folder.split("\\")[-1][2:]

        # # read the json
        # with open(r'Resources/q_'+self.folder_set_name+'/questions.json', 'r') as f:
        #     self.mcq_data = json.load(f)
        #     self.total_mcq_questions = len(self.mcq_data)
            
        # self.load_mcq_question()
        
    # def load_mcq_question(self):
        
    #     # reset button state
    #     self.reset_mcq_button_states()
               
    #     # set the question
    #     self.home.lbl_mcq_question.setText(self.mcq_data[str(self.current_mcq_question)]["question"])
    #     self.home.btn_mcq_option_1.setText(self.mcq_data[str(self.current_mcq_question)]["option_1"])        
    #     self.home.btn_mcq_option_2.setText(self.mcq_data[str(self.current_mcq_question)]["option_2"])        
    #     self.home.btn_mcq_option_3.setText(self.mcq_data[str(self.current_mcq_question)]["option_3"])        
    #     self.home.btn_mcq_option_4.setText(self.mcq_data[str(self.current_mcq_question)]["option_4"])   
        
    #     # set the image if available
    #     files = os.listdir(r'Resources/q_'+self.folder_set_name)
        
    #     for content in files:
            
    #         img_id = ''
    #         if '_' in content:
    #             img_id = content.split('_')[1].split('.')[0]
            
    #             print("ID: ", img_id)	
            
    #         if str(self.current_mcq_question) == img_id:
    #             print("Image: ", 'Resources/q_'+self.folder_set_name+'/'+content)
    #             self.home.lbl_mcq_image.setScaledContents(True)
    #             self.home.lbl_mcq_image.setPixmap(QPixmap(r'Resources/q_'+self.folder_set_name+'/'+content))	
    #             break 
      
    # def reset_mcq_button_states(self):
        
    #     self.home.btn_mcq_option_1.setEnabled(True)
    #     self.home.btn_mcq_option_2.setEnabled(True)
    #     self.home.btn_mcq_option_3.setEnabled(True)
    #     self.home.btn_mcq_option_4.setEnabled(True)
        
    #     self.home.btn_mcq_option_1.setStyleSheet(
    #         '''
    #         QPushButton {
    #             border: 3px solid #E07A5F;
    #             background-color:#3D405B;
    #             border-radius: 20px;
    #             color: rgb(255, 170, 127);
    #             }

    #             QPushButton:hover:!pressed {
    #             background-color: #E07A5F;
    #             color: #F4F1DE;
    #             border: 3px solid #3D405B;
    #         }
    #         '''
    #     )  
        
    #     self.home.btn_mcq_option_2.setStyleSheet(
    #         '''
    #         QPushButton {
    #             border: 3px solid #E07A5F;
    #             background-color:#3D405B;
    #             border-radius: 20px;
    #             color: rgb(255, 170, 127);
    #             }

    #             QPushButton:hover:!pressed {
    #             background-color: #E07A5F;
    #             color: #F4F1DE;
    #             border: 3px solid #3D405B;
    #         }
    #         '''
    #     )  
        
    #     self.home.btn_mcq_option_3.setStyleSheet(
    #         '''
    #         QPushButton {
    #             border: 3px solid #E07A5F;
    #             background-color:#3D405B;
    #             border-radius: 20px;
    #             color: rgb(255, 170, 127);
    #             }

    #             QPushButton:hover:!pressed {
    #             background-color: #E07A5F;
    #             color: #F4F1DE;
    #             border: 3px solid #3D405B;
    #         }
    #         '''
    #     )  
        
    #     self.home.btn_mcq_option_4.setStyleSheet(
    #         '''
    #         QPushButton {
    #             border: 3px solid #E07A5F;
    #             background-color:#3D405B;
    #             border-radius: 20px;
    #             color: rgb(255, 170, 127);
    #             }

    #             QPushButton:hover:!pressed {
    #             background-color: #E07A5F;
    #             color: #F4F1DE;
    #             border: 3px solid #3D405B;
    #         }
    #         '''
    #     )      
        
    # def check_answer(self, button_object):
        
    #     correct_answer = self.mcq_data[str(self.current_mcq_question)]["correct_answer"]
        
    #     if correct_answer == button_object.text():
    #         button_object.setStyleSheet("background-color: green; border: 2px dashed black; border-radius: 10px;")
    #         self.disable_mcq_buttons()
    #         self.current_mcq_question += 1
    #         if self.current_mcq_question > self.total_mcq_questions:
    #             print("All Questions Completed")
    #             self.celebration_page()
    #         else:
    #             QTimer.singleShot(2000, lambda: self.load_mcq_question())
    #     else:
    #         button_object.setStyleSheet("background-color: red; border: 2px dashed black; border-radius: 10px;")

    # def disable_mcq_buttons(self):
        
    #     self.home.btn_mcq_option_1.setEnabled(False)
    #     self.home.btn_mcq_option_2.setEnabled(False)
    #     self.home.btn_mcq_option_3.setEnabled(False)
    #     self.home.btn_mcq_option_4.setEnabled(False)
           
    def celebration_page(self):
        
        #! TODO: Mute Unmute Sound
        
        print("Celebration Page")
               
        movie = QMovie(r"Frontend\Images\celebration.gif")
        self.home.c_gif.setMovie(movie)
        movie.start()
        
        # Set the label properties
        self.home.c_gif.setScaledContents(True)
        self.home.c_gif.setAlignment(Qt.AlignCenter)
        
        # current window
        print("CURR: ", self.current_window)
        
        # navigate celebration page
        if self.current_window == "Lesson":
            self.home.c_next_quiz.clicked.connect(self.mcq_page)
            
        if self.current_window == 'MCQ':
            self.home.c_next_quiz.clicked.connect(self.puzzle_page)
            
        elif self.current_window == "puzzle":
            self.home.c_next_quiz.clicked.connect(self.matching_page)
            
        elif self.current_window == "matching":
            self.home.c_next_quiz.clicked.connect(self.sequencing_page)
            
        elif self.current_window == "sequencing":
            self.home.c_lable.setText("অভিনন্দন! তুমি এই পাঠ টি শেষ করেছো।")
            self.layout().removeWidget(self.home.c_right_frame)
            self.home.c_right_frame.deleteLater()
            
            self.lesson_elapsed_time = time.time() - self.start_time
            print(self.lesson_elapsed_time)
            
            
            # read the student detaisl json file to fetch the name and id
            with open('.student_details.json') as json_file:
                data = json.load(json_file)
                student_name = data['name']
                student_id = data['id']
                
            with open('.current_lesson_log.json') as json_file:
                data = json.load(json_file)
                lsn_attempt = data['lessons'][self.current_lesson_id]['attempt']
                lsn_time = data['lessons'][self.current_lesson_id]['time']
                
                print("LSN ID: ", self.current_lesson_id)
                print("LSN Attempt: ", lsn_attempt)
                print("LSN Time: ", lsn_time)
                            
            # # write lesson results in csv
            self.lesson_completion_data['std_name'] = student_name
            self.lesson_completion_data['std_id'] = student_id
            self.lesson_completion_data['lesson_id'] = self.current_lesson_id
            self.lesson_completion_data['attempt'] = lsn_attempt
            self.lesson_completion_data['time'] = lsn_time
            
            # write the data into .lesson_completion_log.json file
            with open('.lesson_completion_log.json', 'w') as outfile:
                json.dump(self.lesson_completion_data, outfile)
                outfile.write('\n')

    
            # create a folder with student id and name
            performance_folder_name = str(student_id)+'_'+student_name+'_Lesson_'+str(self.current_lesson_id)
            os.path.exists(performance_folder_name) or os.makedirs(performance_folder_name)
            
            # copy all the files from the current lesson folder to the new folder
            shutil.copy2('.lesson_completion_log.json',performance_folder_name)
            shutil.copy2('Performance\matching_results.json',performance_folder_name)
            shutil.copy2('Performance\puzzle_results.json',performance_folder_name)
            shutil.copy2('Performance\sequencing_results.json',performance_folder_name)
                  
    def closeEvent(self, event):
        # For example, you can show a message box asking the user if they really want to quit the application
        reply = QMessageBox.question(self, 'সফটওয়্যার বন্ধ করুন', 'আপনি কি সফটওয়্যারটি বন্ধ করতে চান?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            if self.lesson_window is not None:
                self.lesson_window.quit_music()
            event.accept()
        else:
            event.ignore()

