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


class Matching_Window(QWidget):
    def __init__(self, home_ui):
        super().__init__()
        self.home_ui = home_ui
        self.folder_images = []
        self.image_tag_dict = {}
        self.image_tags = []

        # Enable dragging for labels
        lbl = DraggableLabel("BD")
        self.home_ui.mat_txt_option1 = lbl
        # self.home_ui.mat_txt_option_1.setText("কালো")
        # self.home_ui.mat_txt_option_2 = DragLabel(self.home_ui.mat_txt_option_2)
        # self.home_ui.mat_txt_option_3 = DragLabel(self.home_ui.mat_txt_option_3)
        # self.home_ui.mat_txt_option_4 = DragLabel(self.home_ui.mat_txt_option_4)

        # Other code...      
        
    
    def load_matching_images(self):

        folder_pattern = "Resources/m_*"  # Pattern to match folders starting with "m_"
        

        # Get a list of matching folder paths
        matching_folder = glob.glob(folder_pattern)[0]
        folder_files = os.listdir(matching_folder)
        self.folder_images = [
            file for file in folder_files if file.endswith(".png")]

        # read image tags from json file
        with open(matching_folder + "/image_data.json", "r") as json_file:
            self.image_tag_dict = json.load(json_file)

            # ? update the keys of self.image_tag_dict to remove set6/ from the key
            self.image_tag_dict = {key.replace(
                "set6/", ""): value for key, value in self.image_tag_dict.items()}

            # include only those values that are images
            self.image_tag_dict = {
                key: value for key, value in self.image_tag_dict.items() if key in self.folder_images}

            # fill the image tags
            self.image_tags = list(self.image_tag_dict.values())

        # fill the image option labels with self.image_tags
        self.home_ui.mat_txt_option_1.setText(self.image_tags[0])
        self.home_ui.mat_txt_option_2.setText(self.image_tags[1])
        self.home_ui.mat_txt_option_3.setText(self.image_tags[2])
        self.home_ui.mat_txt_option_4.setText(self.image_tags[3])

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

        print(self.folder_images)
