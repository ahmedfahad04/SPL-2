import datetime
import glob
import json
from math import ceil
import os
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QSound


class MCQ_Window(QWidget):

    def __init__(self, home_ui):
        super().__init__()
        
        self.home_ui = home_ui
        
        self.current_mcq_question = 1
        self.mcq_data = {}
        self.total_mcq_questions = 0
        self.start_time = time.time()
        self.attempts = 0
        self.performance = {}
        self.avg_attempts = 0
        
        # connecting buttons
        self.home_ui.btn_mcq_option_1.clicked.connect(lambda: self.check_answer(self.home_ui.btn_mcq_option_1))
        self.home_ui.btn_mcq_option_2.clicked.connect(lambda: self.check_answer(self.home_ui.btn_mcq_option_2))
        self.home_ui.btn_mcq_option_3.clicked.connect(lambda: self.check_answer(self.home_ui.btn_mcq_option_3))
        self.home_ui.btn_mcq_option_4.clicked.connect(lambda: self.check_answer(self.home_ui.btn_mcq_option_4))
        
         
        self.load_mcq_question()
        
    def load_mcq_question(self):
        
        print("CUR: ", self.current_mcq_question)
        print("TOTAL: ", self.total_mcq_questions)
                
        # read contents
        folder_pattern = "Resources/q_*"  # Pattern to match folders starting with "m_"

        # Get a list of matching folder paths
        self.matching_folder = glob.glob(folder_pattern)[0]
        self.folder_set_name = self.matching_folder.split("\\")[-1][2:]

        # read the json
        with open(r'Resources/q_'+self.folder_set_name+'/questions.json', 'r') as f:
            self.mcq_data = json.load(f)
            self.total_mcq_questions = len(self.mcq_data)
        
        # reset button state
        self.reset_mcq_button_states()
               
        # set the question
        self.home_ui.lbl_mcq_question.setText(self.mcq_data[str(self.current_mcq_question)]["question"])
        self.home_ui.btn_mcq_option_1.setText(self.mcq_data[str(self.current_mcq_question)]["option_1"])        
        self.home_ui.btn_mcq_option_2.setText(self.mcq_data[str(self.current_mcq_question)]["option_2"])        
        self.home_ui.btn_mcq_option_3.setText(self.mcq_data[str(self.current_mcq_question)]["option_3"])        
        self.home_ui.btn_mcq_option_4.setText(self.mcq_data[str(self.current_mcq_question)]["option_4"])   
        
        # set the image if available
        files = os.listdir(r'Resources/q_'+self.folder_set_name)
        
        for content in files:
            
            img_id = ''
            if '_' in content:
                img_id = content.split('_')[1].split('.')[0]
            
                print("ID: ", img_id)	
            
            if str(self.current_mcq_question) == img_id:
                print("Image: ", 'Resources/q_'+self.folder_set_name+'/'+content)
                self.home_ui.lbl_mcq_image.setScaledContents(True)
                self.home_ui.lbl_mcq_image.setPixmap(QPixmap(r'Resources/q_'+self.folder_set_name+'/'+content))	
                break
            
    def reset_mcq_button_states(self):
        
        self.home_ui.btn_mcq_option_1.setEnabled(True)
        self.home_ui.btn_mcq_option_2.setEnabled(True)
        self.home_ui.btn_mcq_option_3.setEnabled(True)
        self.home_ui.btn_mcq_option_4.setEnabled(True)
        
        self.home_ui.btn_mcq_option_1.setStyleSheet(
            '''
            QPushButton {
                border: 3px solid #E07A5F;
                background-color:#3D405B;
                border-radius: 20px;
                color: rgb(255, 170, 127);
                }

                QPushButton:hover:!pressed {
                background-color: #E07A5F;
                color: #F4F1DE;
                border: 3px solid #3D405B;
            }
            '''
        )  
        
        self.home_ui.btn_mcq_option_2.setStyleSheet(
            '''
            QPushButton {
                border: 3px solid #E07A5F;
                background-color:#3D405B;
                border-radius: 20px;
                color: rgb(255, 170, 127);
                }

                QPushButton:hover:!pressed {
                background-color: #E07A5F;
                color: #F4F1DE;
                border: 3px solid #3D405B;
            }
            '''
        )  
        
        self.home_ui.btn_mcq_option_3.setStyleSheet(
            '''
            QPushButton {
                border: 3px solid #E07A5F;
                background-color:#3D405B;
                border-radius: 20px;
                color: rgb(255, 170, 127);
                }

                QPushButton:hover:!pressed {
                background-color: #E07A5F;
                color: #F4F1DE;
                border: 3px solid #3D405B;
            }
            '''
        )  
        
        self.home_ui.btn_mcq_option_4.setStyleSheet(
                '''
                QPushButton {
                    border: 3px solid #E07A5F;
                    background-color:#3D405B;
                    border-radius: 20px;
                    color: rgb(255, 170, 127);
                    }

                    QPushButton:hover:!pressed {
                    background-color: #E07A5F;
                    color: #F4F1DE;
                    border: 3px solid #3D405B;
                }
                '''
            )      
            
    def check_answer(self, button_object):
        
        self.attempts += 1
        correct_answer = self.mcq_data[str(self.current_mcq_question)]["correct_answer"]
        
        given_correct_answer = correct_answer.strip()
        user_answer = button_object.text().strip()
        
        if given_correct_answer == user_answer:
            
            QSound.play(r'Frontend\Audio_Track\correct_answer.wav')
            button_object.setStyleSheet("background-color: green; border: 2px dashed black; border-radius: 10px;")
            self.disable_mcq_buttons()
            self.current_mcq_question += 1
            QSound.play("Frontend\Audio_Track\correct_answer.wav")

            # mcq question done and load next assessment
            if self.current_mcq_question > self.total_mcq_questions:
                                
                print("All Questions Completed")
                QSound.play("Frontend/Audio_Track/clap_sound.wav")
                self.write_to_json()                   
                time.sleep(1)
                self.home_ui.stackedWidget.setCurrentWidget(self.home_ui.celebration_page) 
            else:
                QTimer.singleShot(2000, lambda: self.load_mcq_question())
        else:
            QSound.play("Frontend/Audio_Track/mistake_sound.wav")
            button_object.setStyleSheet("background-color: red; border: 2px dashed black; border-radius: 10px;")

    def disable_mcq_buttons(self):
        
        self.home_ui.btn_mcq_option_1.setEnabled(False)
        self.home_ui.btn_mcq_option_2.setEnabled(False)
        self.home_ui.btn_mcq_option_3.setEnabled(False)
        self.home_ui.btn_mcq_option_4.setEnabled(False)
           
    def write_to_json(self):
        
        # read the student detaisl json file to fetch the name and id
        with open('Student_Info\.student_details.json') as json_file:
            data = json.load(json_file)
            student_name = data['name']
            student_id = data['id']
        
        # write to json file
        # write total moves, time and date into a json file
        self.performance['std_name'] = student_name
        self.performance['std_id'] = student_id
        self.performance['set_name'] = self.matching_folder.split('\\')[-1]
        self.performance['attempts'] = self.attempts
        self.performance['time'] = round(time.time() - self.start_time,2)
        self.performance['success_rate'] = round((2 / self.attempts)*100, 2)
        self.performance['date'] = datetime.datetime.now().strftime("%Y-%m-%d")
        
        with open('Performance' + "/mcq_results.json", "w+") as json_file:
            json.dump(self.performance, json_file)