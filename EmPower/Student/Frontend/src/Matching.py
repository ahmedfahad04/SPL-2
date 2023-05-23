import glob
import json
import os
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtMultimedia import QSound
from Backend.AudioPlayer import MusicPlayer
from Frontend.Student_UI import ui_home
from Frontend.src.Document_Formatter import *
from Frontend.src.Lesson import Lesson_Window
from Frontend.src.Puzzle import Puzzle_Window


class DraggableLabel(QLabel):

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

    def __init__(self, image_labels):
        super().__init__()

        self.images_labels = image_labels
        self.setAcceptDrops(True)  # Enable drop events

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasText():
            text = event.mimeData().text()
            self.setText(text)

            print("Dropped: ", text)
            print("ANS: ", self.images_labels)
            # ? Check if the dropped image is correct
            if self.images_labels == text:
                self.setStyleSheet("background-color: green")

            else:
                # ? If the dropped image is incorrect, play sound
                QSound.play("Frontend\Audio_Track\mistake_sound.wav")
                self.setStyleSheet("background-color: red")
                
                event.ignore()


class Matching_Window(QWidget):

    def __init__(self, home_ui):
        super().__init__()
        self.home_ui = home_ui
        self.folder_images = []
        self.image_tag_dict = {}
        self.image_tags = []

        # Other code...

    def load_matching_images(self):

        folder_pattern = "Resources/m_*"  # Pattern to match folders starting with "m_"

        # Get a list of matching folder paths
        matching_folder = glob.glob(folder_pattern)[0]
        folder_set_name = matching_folder.split("\\")[-1].split("_")[-1]
        print("SET: ", folder_set_name)
        folder_files = os.listdir(matching_folder)
        self.folder_images = [
            file for file in folder_files if file.endswith(".png")]

        # read image tags from json file
        with open(matching_folder + "/image_data.json", "r") as json_file:
            self.image_tag_dict = json.load(json_file)
            

            # ? update the keys of self.image_tag_dict to remove set6/ from the key
            self.image_tag_dict = {key: value.replace("{}/".format(folder_set_name), "") for key, value in self.image_tag_dict.items()}
            print("DICT: ", self.image_tag_dict)

            # include only those values that are images
            self.image_tag_dict = {
                key: value for key, value in self.image_tag_dict.items() if value in self.folder_images}

            # fill the image tags
            self.image_tags = list(self.image_tag_dict.keys())
            
        print("IMG: ", self.folder_images)
        print("LABEL: ", self.image_tags)

        # fill the image option labels with self.image_tags
        # self.home_ui.mat_txt_option_1.setText(self.image_tags[0])
        self.home_ui.mat_txt_option_2.setText(self.image_tags[1])
        self.home_ui.mat_txt_option_3.setText(self.image_tags[2])
        self.home_ui.mat_txt_option_4.setText(self.image_tags[3])
        
        
        
        
        

        ##################################

        # Create a QVBoxLayout to arrange the labels vertically
        layout_1 = QVBoxLayout()

        # Create draggable labels and add them to the layout
        draggable_label_1 = DraggableLabel(self.image_tags[0])
        draggable_label_1.setFont(QtGui.QFont("Arial", 10))
        draggable_label_1.setStyleSheet("border: none;")
        draggable_label_1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # add the label to the layout
        layout_1.addWidget(draggable_label_1)

        # Set the layout of the frame
        self.home_ui.mat_option_1_frame.setLayout(layout_1)

        ##################################
        
        
        
        
        
        
        
        

        ##################################

        # Create a QVBoxLayout to arrange the labels vertically
        compare_layout_1 = QVBoxLayout()

        # Create draggable labels and add them to the layout
        draggable_compare_label_1 = DroppableLabel(self.image_tags[0])
        draggable_compare_label_1.setFont(QtGui.QFont("Arial", 15))
        draggable_compare_label_1.setStyleSheet(
            "border: none; background-color: none;")
        draggable_compare_label_1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # add the label to the layout
        compare_layout_1.addWidget(draggable_compare_label_1)

        # Set the layout of the frame
        self.home_ui.mat_txt_lbl_1_frame.setLayout(compare_layout_1)

        ##################################
        
        
        
        
        
        
        
        
        

        # change the aspect ration so that it fit any kind of lable
        self.home_ui.mat_img_lbl_1.setScaledContents(True)
        self.home_ui.mat_img_lbl_2.setScaledContents(True)
        self.home_ui.mat_img_lbl_3.setScaledContents(True)
        self.home_ui.mat_img_lbl_4.setScaledContents(True)

        # fill the image labels with images
        self.home_ui.mat_img_lbl_1.setPixmap(
            QPixmap(matching_folder + "/" + self.folder_images[0]))
        self.home_ui.mat_img_lbl_2.setPixmap(
            QPixmap(matching_folder + "/" + self.folder_images[1]))
        self.home_ui.mat_img_lbl_3.setPixmap(
            QPixmap(matching_folder + "/" + self.folder_images[2]))
        self.home_ui.mat_img_lbl_4.setPixmap(
            QPixmap(matching_folder + "/" + self.folder_images[3]))
