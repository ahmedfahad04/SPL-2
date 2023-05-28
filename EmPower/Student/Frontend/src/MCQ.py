import glob
import json
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MCQ_Window(QWidget):

    def __init__(self, home_ui):
        super().__init__()
        
        self.home_ui = home_ui
        
        self.current_mcq_question = 1
        self.mcq_data = {}
        self.total_mcq_questions = 0
        
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
        
        correct_answer = self.mcq_data[str(self.current_mcq_question)]["correct_answer"]
        
        if correct_answer == button_object.text():
            print("Correct Answer", correct_answer, 'Type: ', type(correct_answer)	)
            print("Button Text", button_object.text(), 'Type: ', type(button_object.text()))
            button_object.setStyleSheet("background-color: green; border: 2px dashed black; border-radius: 10px;")
            self.disable_mcq_buttons()
            self.current_mcq_question += 1
            if self.current_mcq_question > self.total_mcq_questions:
                print("All Questions Completed")
            else:
                QTimer.singleShot(2000, lambda: self.load_mcq_question())
        else:
            button_object.setStyleSheet("background-color: red; border: 2px dashed black; border-radius: 10px;")

    def disable_mcq_buttons(self):
        
        self.home_ui.btn_mcq_option_1.setEnabled(False)
        self.home_ui.btn_mcq_option_2.setEnabled(False)
        self.home_ui.btn_mcq_option_3.setEnabled(False)
        self.home_ui.btn_mcq_option_4.setEnabled(False)
           