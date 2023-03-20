import os

from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QMainWindow


class Lesson_Window(QMainWindow):
    def __init__(self, ui_object):
        super(QMainWindow, self).__init__()

        # window
        self.lesson_window = ui_object

        # load lesson
        self.load_lesson()

    def load_lesson(self):
        folder_path = "Resources/নাম_শিখন(Noun)_পাঠ_1"
        image_file_path = os.path.join(folder_path, "image.jpeg")
        image = QImage(image_file_path)

