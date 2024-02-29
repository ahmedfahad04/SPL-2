import glob
import json
import os
import shutil
import time

from PyQt5.QtMultimedia import QSound

from Backend.AudioPlayer import MusicPlayer
from Backend.track import FaceTracker
from Frontend.src.Document_Formatter import *
from Frontend.src.Lesson import Lesson_Window
from Frontend.src.Matching import Matching_Window
from Frontend.src.MCQ import MCQ_Window
from Frontend.src.Puzzle import Puzzle_Window
from Frontend.src.Sequence import Sequence_Window
from Frontend.Student_UI import ui_home


class Home(QMainWindow):  # Home extends QMainWindow

    def __init__(self):
        
        super(QMainWindow, self).__init__()
        self.face_tracker = None
        self.lesson_window = None
        self.music_player = None 
        self.home = None 
        self.current_window = 'MCQ'
        self.current_lesson_id = None
        self.start_time = time.time()
        self.lesson_completion_data = {}
        
        # file paths
        self.lesson_completion_file_location = 'Lesson_log\.lesson_completion_log.json'
        
        # create studentinfo folder
        os.path.exists('Student_Info') or os.makedirs('Student_Info')
        
        #! TODO: Handle student id and name
        
        self.manage_content()
        self.hide_folders_except('.', ["Frontend", "Backend", "Output"])
        self.home_page()
        # self.matching_page()
                
    def create_file(self, file_path):
        
        # Check if the file already exists
        if not os.path.exists(file_path):
            try:
                # Create the file
                with open(file_path, 'w') as file:
                    file.write("")
                print(f"File {file_path} created successfully.")
            except OSError as e:
                print(f"Error: {e.strerror}")
        else:
            print(f"The file {file_path} already exists.")
    
    def hide_folders_except(self, directory, exceptions):
        for root, dirs, _ in os.walk(directory):
            for folder in dirs:
                if folder not in exceptions:
                    folder_path = os.path.join(root, folder)
                    try:
                        # Set the hidden attribute for the folder
                        os.system(f'attrib +h "{folder_path}"')
                    except Exception as e:
                        print(f"Error hiding folder {folder_path}: {e}")
        
    def manage_content(self):

        parent_folder = '.'
        resources_folder = 'Resources'
        target_folder = ''
        std_roll = ''
        flag = False 
        
        # create necessary folders
        os.path.exists('Resources') or os.makedirs('Resources')
        os.path.exists('Lesson_log') or os.makedirs('Lesson_log')
        os.path.exists('Performance') or os.makedirs('Performance')
        self.create_file(self.lesson_completion_file_location)
        self.create_file('Performance\matching_results.json')
        self.create_file('Performance\puzzle_results.json')
        self.create_file('Performance\sequencing_results.json')
        self.create_file('Performance\mcq_results.json')
                
        #get student roll number
        with open ('Student_Info\.student_details.json') as f:
            data = json.load(f)
            std_roll = data['id']

        # Iterate through the directories in the parent folder
        for folder_name in os.listdir(parent_folder):
            folder_path = os.path.join(parent_folder, folder_name)
            
            # Check if the folder name starts with "11"
            if folder_name.startswith(str(std_roll)) and os.path.isdir(folder_path) and 'পাঠ' in folder_name:
                
                # Remove the subfolders of the resources folder
                shutil.rmtree(resources_folder)
                target_folder = folder_name
                
                # Recreate the resources folder
                os.mkdir(resources_folder)
                
                # Copy the subfolders of the target folder to the resources folder
                target_subfolders = os.listdir(folder_path)
                
                for subfolder_name in target_subfolders:
                    subfolder_path = os.path.join(folder_path, subfolder_name)
                    if os.path.isdir(subfolder_path):
                        shutil.copytree(subfolder_path, os.path.join(resources_folder, subfolder_name))

                flag = True
                
        if flag: 
            shutil.rmtree(target_folder)
            print("DONE: Manage Content", target_folder)
        else: 
            print("Existing folder loaded...")
                     
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
        movie = QMovie(r"Frontend\Images\how_to_puzzle.gif")
        self.home.n_type_lbl.setScaledContents(True)
        self.home.n_type_lbl.setMovie(movie)
        movie.start()

        # Navigate between pages
        self.home.stackedWidget.setCurrentWidget(self.home.home_page)
        
        # Start a timer to load the lesson widget after 2 seconds
        QTimer.singleShot(1000, self.lesson_page)

    def lesson_page(self):
        
        print("Lesson Page"	)
        self.current_window = "Lesson"
        
        # load & set up the LESSON page
        
        # / ****** face tracker code  ***** /
        #add the tracking thread
        self.face_tracker = FaceTracker()
        self.lesson_window = Lesson_Window(self.home, self.face_tracker)
        # / ****** face tracker code  ***** /
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
                if not os.path.exists(self.lesson_completion_file_location):
                    # Create an empty log file
                    with open(self.lesson_completion_file_location, 'w') as outfile:
                        json.dump({}, outfile)
                        
                # check log file to see if the lesson is already completed
                try:
                    with open(self.lesson_completion_file_location) as json_file:
                        data = json.load(json_file)
                        
                        if file in data:
                            print("Lesson already completed")
                        else:
                            print("Lesson not completed yet")
                except json.JSONDecodeError:
                    # Handle the case where the file is empty (JSONDecodeError is raised)
                    print("Lesson not completed yet")
                except FileNotFoundError:
                    # Handle the case where the file does not exist
                    print("Lesson not completed yet")
                
                # if not completed then mark it as current lesson 
                self.current_lesson_id = file.split("_")[1]
        
    def config_current_lesson_status(self):
                
        current_lesson_log_file = 'Lesson_log\.current_lesson_log.json'

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
            
            self.home.c_next_quiz.clicked.connect(self.puzzle_page)
            # / ****** face tracker code  ***** /
            self.face_tracker.stop()
            # / ****** face tracker code  ***** /
            
        if self.current_window == 'puzzle':
            self.home.c_next_quiz.clicked.connect(self.mcq_page)
            
        elif self.current_window == "MCQ":
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
            with open('Student_Info\.student_details.json') as json_file:
                data = json.load(json_file)
                student_name = data['name']
                student_id = data['id']
                
            with open('Lesson_log\.current_lesson_log.json') as json_file:
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
            
            # write the data into self.lesson_completion_file_location file
            with open(self.lesson_completion_file_location, 'w') as outfile:
                json.dump(self.lesson_completion_data, outfile)
                outfile.write('\n')
                
            # make output folder
            os.path.exists('Output') or os.makedirs('Output')
    
            # create a folder with student id and name
            performance_folder_name = 'Output/' + str(student_id)+'_'+student_name+'_Lesson_'+str(self.current_lesson_id)
            if os.path.exists(performance_folder_name):
                shutil.rmtree(performance_folder_name)
            
            os.makedirs(performance_folder_name)
            
            # copy all the files from the current lesson folder to the new folder
            shutil.copy2(self.lesson_completion_file_location,performance_folder_name)
            shutil.copy2('Performance\matching_results.json',performance_folder_name)
            shutil.copy2('Performance\puzzle_results.json',performance_folder_name)
            shutil.copy2('Performance\sequencing_results.json',performance_folder_name)
            shutil.copy2('Performance\mcq_results.json',performance_folder_name)
            shutil.copy2('surveillance_log.json', performance_folder_name)
            
            # remove redundant folders
            os.remove('surveillance_log.json')
                  
    def closeEvent(self, event):
        # For example, you can show a message box asking the user if they really want to quit the application
        reply = QMessageBox.question(self, 'সফটওয়্যার বন্ধ করুন', 'আপনি কি সফটওয়্যারটি বন্ধ করতে চান?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            if self.lesson_window is not None:
                self.lesson_window.quit_music()
                # / ****** face tracker code  ***** /
                self.face_tracker.stop()
                # / ****** face tracker code  ***** /
            event.accept()
        else:
            event.ignore()

