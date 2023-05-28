import datetime
import glob
import json
import os
import random
import time
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtMultimedia import QSound
from Backend.AudioPlayer import MusicPlayer
from Frontend.Student_UI import ui_home
from Frontend.src.Document_Formatter import *
from Frontend.src.Lesson import Lesson_Window
from Frontend.src.Puzzle import Puzzle_Window

moves = 0

class DraggableLabel(QLabel):
    
    matchSuccessful = pyqtSignal(str)  # Define a custom signal

    def __init__(self, text):
        super().__init__(text)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return

        drag = QDrag(self)
        mime_data = QMimeData()

        # Set the MIME data as plain text with the label's text
        mime_data.setText(self.text())

        drag.setMimeData(mime_data)

        # Set a pixmap as the drag image
        pixmap = self.grab()
        drag.setPixmap(pixmap)

        # Set the hot spot to the current mouse position relative to the label's top-left corner
        drag.setHotSpot(event.pos())

        # Start the drag operation
        drag.exec_(Qt.MoveAction)

class DroppableLabel(QLabel):
    
    matchSuccessful = pyqtSignal(str)  # Define a custom signal

    def __init__(self, image_frame , image_labels):
        super().__init__()

        self.images_labels = image_labels
        self.image_frame = image_frame
        self.already_matched = False 
        
        self.setAcceptDrops(True)  # Enable drop events

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        
        if event.mimeData().hasText() and len(self.text()) == 0:
            text = event.mimeData().text()
            self.setText(text)

            print("Dropped: ", text)
            print("ANS: ", self.images_labels)
            
            if self.images_labels == text and text != " ":
                self.setStyleSheet("background-color: green; border: none;")
                QSound.play("Frontend\Audio_Track\small_clap_sound.wav")
                self.matchSuccessful.emit(text)
                self.already_matched = True
                global moves 
                moves += 1
                print("Moves: ", moves)
            else:
                QSound.play("Frontend\Audio_Track\mistake_sound.wav")
                self.setStyleSheet("background-color: red; border: none;")
                self.image_frame.layout().itemAt(0).widget().setText("")
                self.already_matched = False 
                moves += 1
                print("Moves: ", moves)
                event.ignore()
                
        else: 
            event.ignore()

class Matching_Window(QWidget):

    def __init__(self, home_ui):
        super().__init__()
        
        self.home_ui = home_ui
        self.images = []
        self.image_tag_dict = {}
        self.image_tags = []
        self.correct_matches = 0
        self.start_time = time.time()
        self.end_time = 0
        self.folder_set_name = None
        self.performance = {}
        self.matching_folder = None

    def load_matching_images(self):

        folder_pattern = "Resources/m_*"  # Pattern to match folders starting with "m_"

        # Get a list of matching folder paths
        self.matching_folder = glob.glob(folder_pattern)[0]
        self.folder_set_name = self.matching_folder.split("\\")[-1].split("_")[-1]
        folder_files = os.listdir(self.matching_folder)
        self.images = [file for file in folder_files if file.endswith(".png")]

        # read image tags from json file
        with open(self.matching_folder + "/image_data.json", "r") as json_file:
            self.image_tag_dict = json.load(json_file)
            
            # ? update the keys of self.image_tag_dict to remove set6/ from the value
            self.image_tag_dict = {key.replace("{}/".format(self.folder_set_name), ""): value for key, value in self.image_tag_dict.items()}
            print("DICT: ", self.image_tag_dict)

            # include only those values that are images
            self.image_tag_dict = {key: value for key, value in self.image_tag_dict.items() if key in self.images}

            # fill the image tags
            self.image_tags = list(self.image_tag_dict.values())
            
        print("IMG: ", self.images)
        print("LABEL: ", self.image_tags)
       

        # change the aspect ration so that it fit any kind of lable
        self.home_ui.mat_img_lbl_1.setScaledContents(True)
        self.home_ui.mat_img_lbl_2.setScaledContents(True)
        self.home_ui.mat_img_lbl_3.setScaledContents(True)
        self.home_ui.mat_img_lbl_4.setScaledContents(True)
        
        self.home_ui.mat_img_lbl_1.setProperty("image",self.images[0])
        self.home_ui.mat_img_lbl_2.setProperty("image",self.images[1])
        self.home_ui.mat_img_lbl_3.setProperty("image",self.images[2])
        self.home_ui.mat_img_lbl_4.setProperty("image",self.images[3])
        
        # fill the image labels with images
        
        self.home_ui.mat_img_lbl_1.setPixmap(
            QPixmap(self.matching_folder + "/" + self.images[0]).scaled(
                self.home_ui.mat_img_lbl_1.size(), 
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
        
        self.home_ui.mat_img_lbl_2.setPixmap(
            QPixmap(self.matching_folder + "/" + self.images[1]).scaled(
                self.home_ui.mat_img_lbl_1.size(), 
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
        
        self.home_ui.mat_img_lbl_3.setPixmap(
            QPixmap(self.matching_folder + "/" + self.images[2]).scaled(
                self.home_ui.mat_img_lbl_1.size(), 
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
        
        self.home_ui.mat_img_lbl_4.setPixmap(
            QPixmap(self.matching_folder + "/" + self.images[3]).scaled(
                self.home_ui.mat_img_lbl_1.size(), 
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
        
        ##################################
        
        # Shuffle the image tags and folder images in the same order
        random.shuffle(self.image_tags)
        random.shuffle(self.images)
        
        
        # list of option_frames 
        option_frames = [
            self.home_ui.mat_option_1_frame,
            self.home_ui.mat_option_2_frame,
            self.home_ui.mat_option_3_frame,
            self.home_ui.mat_option_4_frame
        ]
        
        
        self.set_option_label(self.home_ui.mat_option_1_frame, self.image_tags[0])
        self.set_option_label(self.home_ui.mat_option_2_frame, self.image_tags[1])
        self.set_option_label(self.home_ui.mat_option_3_frame, self.image_tags[2])
        self.set_option_label(self.home_ui.mat_option_4_frame, self.image_tags[3])
        
        self.set_drop_label(self.home_ui.mat_txt_lbl_1_frame, option_frames, self.img_drop_value(1))
        self.set_drop_label(self.home_ui.mat_txt_lbl_2_frame, option_frames, self.img_drop_value(2))
        self.set_drop_label(self.home_ui.mat_txt_lbl_3_frame, option_frames, self.img_drop_value(3))
        self.set_drop_label(self.home_ui.mat_txt_lbl_4_frame, option_frames, self.img_drop_value(4))
        
        ##################################   
        
    def set_option_label(self, label_frame, label_text):
        
        # Create a QVBoxLayout to arrange the labels vertically
        layout_1 = QVBoxLayout()

        # Create draggable labels and add them to the layout
        draggable_label_1 = DraggableLabel(label_text)
        draggable_label_1.setFont(QtGui.QFont("Arial", 10))
        draggable_label_1.setStyleSheet("border: none;")
        draggable_label_1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        draggable_label_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        # add the label to the layout
        layout_1.addWidget(draggable_label_1)
        
        # # Connect the matchSuccessful signal from the draggable label to a slot
        draggable_label_1.matchSuccessful.connect(lambda: self.handle_match_successful(label_frame))

        # Set the layout of the frame
        label_frame.setLayout(layout_1)
        
    def set_drop_label(self, drag_label_frame, drop_label_frame, label_text):
        
        compare_layout_1 = QVBoxLayout()

        # Create draggable labels and add them to the layout
        draggable_compare_label_1 = DroppableLabel(drag_label_frame, label_text)
        draggable_compare_label_1.setFont(QtGui.QFont("Arial", 15))
        draggable_compare_label_1.setStyleSheet("border: none; background-color: none;")
        draggable_compare_label_1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        draggable_compare_label_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        # add the label to the layout
        compare_layout_1.addWidget(draggable_compare_label_1)
        
        # # Connect the matchSuccessful signal from the droppable label to a slot
        draggable_compare_label_1.matchSuccessful.connect(lambda: self.handle_match_successful(drop_label_frame, label_text))

        # Set the layout of the frame
        drag_label_frame.setLayout(compare_layout_1)
        
    def handle_match_successful(self, option_label_frames, matched_text):
        
        # Slot to handle the matchSuccessful signal
        
        self.correct_matches += 1
       
        print("MATCHED!")
                
        # search through all labels in which the text is matched
        for option_frame in option_label_frames:
            
            text = option_frame.layout().itemAt(0).widget().text()
            
            if text == matched_text:
                
                # remove the label text from the frame
                option_frame.layout().itemAt(0).widget().setText("")
                break
            
        if self.correct_matches == 4:
              
            global moves 
            print("ALL MATCHED!, Total Moves: ", moves)
            QSound.play(r'Frontend\Audio_Track\clap_sound.wav')
            
            self.end_time = time.time()
            time_taken = self.end_time - self.start_time
            print("Total time taken:", round(time_taken,2), "seconds")
            
            # read the student detaisl json file to fetch the name and id
            with open('.student_details.json') as json_file:
                data = json.load(json_file)
                student_name = data['name']
                student_id = data['id']
            
            # write total moves, time and date into a json file
            self.performance['std_name'] = student_name
            self.performance['std_id'] = student_id
            self.performance['set_name'] = self.matching_folder
            self.performance['attempts'] = moves+1
            self.performance['time'] = round(time_taken,2)
            success_rate = round((4/moves)*100,2)
            if success_rate > 100:
                success_rate = 100
            self.performance['success_rate'] = success_rate
            self.performance['date'] = datetime.datetime.now().strftime("%Y-%m-%d")
            
            with open('Performance' + "/matching_results.json", "w+") as json_file:
                json.dump(self.performance, json_file)
                
                
                
            self.home_ui.stackedWidget.setCurrentWidget(self.home_ui.celebration_page)
  
    def img_drop_value(self, frame_id):
        
        if frame_id == 1:
                        
            image_name = self.home_ui.mat_img_lbl_1.property("image")
            image_tag = self.image_tag_dict[image_name]
            return image_tag
        
        elif frame_id == 2:
            
            image_name = self.home_ui.mat_img_lbl_2.property("image")
            image_tag = self.image_tag_dict[image_name]
            return image_tag
        
        elif frame_id == 3:
            
            image_name = self.home_ui.mat_img_lbl_3.property("image")
            image_tag = self.image_tag_dict[image_name]
            return image_tag
        
        elif frame_id == 4:
            
            image_name = self.home_ui.mat_img_lbl_4.property("image")
            image_tag = self.image_tag_dict[image_name]
            return image_tag
        

