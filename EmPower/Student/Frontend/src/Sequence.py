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

    def __init__(self, image):
        super().__init__()
        
        self.image_name = image.split("/")[-1] 
        image = QtGui.QPixmap(image)
        self.setPixmap(image.scaled(self.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return

        drag = QDrag(self)
        mime_data = QMimeData()

        pixmap = self.pixmap()
        mime_data.setImageData(pixmap)

        drag.setMimeData(mime_data)
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())

        drag.exec_(QtCore.Qt.MoveAction)
        
    def get_image_name(self):
        return self.image_name


class DroppableLabel(QLabel):
    
    matchSuccessful = pyqtSignal(str)

    def __init__(self, image_frame, image_labels):
        super().__init__(image_labels)
        self.images_labels = image_labels
        self.image_frame = image_frame
        self.already_matched = False
        self.setAcceptDrops(True)
        self.pixmap = None  # Initialize the pixmap as None

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasImage():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasImage():
            event.acceptProposedAction()

    def dropEvent(self, event: QtGui.QDropEvent):
        if event.mimeData().hasImage() and self.pixmap is None:  # Check if pixmap is None
            image_data = event.mimeData().imageData()
            dragged_image_name = event.source().get_image_name()
            dragged_image_id = dragged_image_name.split("_")[0]

            if self.images_labels == dragged_image_id and image_data is not None:
                QSound.play("Frontend/Audio_Track/small_clap_sound.wav")
                self.setStyleSheet("background-color: green; border: 5px solid green;")
                self.pixmap = image_data.scaled(self.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)  # Set the pixmap
                self.setPixmap(self.pixmap)
                self.matchSuccessful.emit(dragged_image_name)
                global moves
                moves += 1
                print("Moves: ", moves)
            else:
                QSound.play("Frontend/Audio_Track/mistake_sound.wav")
                self.setStyleSheet("background-color: red; border: none;")
                moves += 1
                print("Moves: ", moves)
                event.ignore()
        else:
            event.ignore()
         
    
class Sequence_Window(QWidget):

    def __init__(self, home_ui):
        super().__init__()
        
        self.home_ui = home_ui
        self.images = []
        self.image_tag_dict = {}
        self.image_tags = []
        self.matching_folder = ""
        self.correct_matches = 0
        self.start_time = time.time()
        self.end_time = None
        self.folder_set_name = None
        self.performance = {}
               
    def load_sequence_file(self):
        
        folder_pattern = "Resources/s_*"  # Pattern to match folders starting with "m_"

        # Get a list of matching folder paths
        self.matching_folder = glob.glob(folder_pattern)[0]
        self.folder_set_name = self.matching_folder.split("\\")[-1].split("_")[-1]
        folder_files = os.listdir(self.matching_folder)
        
        # read images from folder and remove the initial two words (eg. 1_, 2_) from the file name
        self.actual_image_path = [file for file in folder_files if file.endswith(".png")]
        self.images = [file[2:] for file in folder_files if file.endswith(".png")]
        
        # read image tags from json file
        with open(self.matching_folder + "/image_data.json", "r") as json_file:
            self.image_seq_dict = json.load(json_file)
            
            # ? update the keys of self.image_seq_dict to remove set6/ from the value
            self.image_seq_dict = {key: value.replace("{}/".format(self.folder_set_name), "") for key, value in self.image_seq_dict.items()}
            print("DICT: ", self.image_seq_dict)

            #! include only those values that are images
            self.image_seq_dict = {key: value for key, value in self.image_seq_dict.items() if value in self.images}

            # fill the image tags
            self.image_tags = list(self.image_seq_dict.values()) 
            
        print("SEQ: ", self.image_seq_dict)
        all_option_frames = [
            self.home_ui.seq_img_frame_lbl_1,
            self.home_ui.seq_img_frame_lbl_2,
            self.home_ui.seq_img_frame_lbl_3,
            self.home_ui.seq_img_frame_lbl_4
        ]

        # set the labels for the images
        self.set_drop_label(all_option_frames, self.home_ui.seq_lbl_frame_1, '1')
        self.set_drop_label(all_option_frames, self.home_ui.seq_lbl_frame_2, '2')
        self.set_drop_label(all_option_frames, self.home_ui.seq_lbl_frame_3, '3')
        self.set_drop_label(all_option_frames, self.home_ui.seq_lbl_frame_4, '4')
        
        # Shuffle the images and tags
        random.shuffle(self.images)
        random.shuffle(self.actual_image_path)
        updated_path = [file[2:] for file in self.actual_image_path]
        print("PATH: ", self.actual_image_path)
        print("UPATH", updated_path)
        print("IMG: ", self.images)

        # Set picture to option labels with shuffled images
        self.set_option_label(self.actual_image_path[0], self.home_ui.seq_img_frame_lbl_1, updated_path[0])
        self.set_option_label(self.actual_image_path[1], self.home_ui.seq_img_frame_lbl_2, updated_path[1])
        self.set_option_label(self.actual_image_path[2], self.home_ui.seq_img_frame_lbl_3, updated_path[2])
        self.set_option_label(self.actual_image_path[3], self.home_ui.seq_img_frame_lbl_4, updated_path[3])
        
    def set_option_label(self, image_path, label_frame, image_tag):
        
        # Create a QVBoxLayout to arrange the labels vertically
        layout_1 = QVBoxLayout()

        # Create draggable labels and add them to the layout
        draggable_label_1 = DraggableLabel(self.matching_folder + "/" + image_path)
        draggable_label_1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        draggable_label_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        draggable_label_1.setScaledContents(True)
        draggable_label_1.setProperty("image", image_tag)
        draggable_label_1.setPixmap(
            QPixmap(self.matching_folder + "/" + image_path).scaled(
                label_frame.size(), 
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )
        
        # add the label to the layout
        layout_1.addWidget(draggable_label_1)
        layout_1.setContentsMargins(0, 0, 0, 0)
        
        # # Connect the matchSuccessful signal from the draggable label to a slot
        draggable_label_1.matchSuccessful.connect(lambda: self.handle_match_successful(label_frame))

        # Set the layout of the frame
        label_frame.setLayout(layout_1)
        
    def set_drop_label(self, drop_label_frame, label_frame, label_text):
        
        compare_layout_1 = QVBoxLayout()
        cnt = 0

        # Create draggable labels and add them to the layout
        draggable_compare_label_1 = DroppableLabel(label_frame, label_text)
        draggable_compare_label_1.setFont(QtGui.QFont("Arial", 25))
        draggable_compare_label_1.setStyleSheet("border: none; background-color: none; color: gray;")
        draggable_compare_label_1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        draggable_compare_label_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        # add the label to the layout
        compare_layout_1.addWidget(draggable_compare_label_1)
        
        # # # Connect the matchSuccessful signal from the droppable label to a slot
        draggable_compare_label_1.matchSuccessful.connect(lambda: self.handle_match_successful(drop_label_frame, label_text))

        # Set the layout of the frame
        label_frame.setLayout(compare_layout_1)
        
    def handle_match_successful(self, option_label_frames, matched_image_id):
        
        # count correct matches
        self.correct_matches += 1
        
        # get image name
        print("SEQ: ", self.image_seq_dict)
        matched_image_name = self.image_seq_dict[matched_image_id]
        print("Matched image name: ", matched_image_name)
        print("ID: ", matched_image_id)
        
        # loop through all frames where the image is matched
        for option_frame in option_label_frames:
            
            # get the image tag
            image_tag = option_frame.layout().itemAt(0).widget().property("image")
            
            # if the image tag matches the matched image tag
            if image_tag == matched_image_name:
                
                # remove the label text from the frame
                option_frame.layout().itemAt(0).widget().setPixmap(QPixmap())
                break
            
        if self.correct_matches == 4:
            print("All matches successful")
            QSound.play(r'Frontend\Audio_Track\clap_sound.wav')
            
            # All boxes are filled
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
            self.performance['attempts'] = moves
            self.performance['time'] = round(time_taken,2)
            self.performance['success_rate'] = round((4/moves)*100,2)
            self.performance['date'] = datetime.datetime.now().strftime("%Y-%m-%d")
            
            with open('Performance' + "/sequencing_results.json", "w+") as json_file:
                json.dump(self.performance, json_file)
                
            self.home_ui.stackedWidget.setCurrentWidget(self.home_ui.celebration_page)
       
    def img_drag_value(self, image_names):
        
        for key, value in self.image_seq_dict.items():
            
            if value == image_names:
                return key
        