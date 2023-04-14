from Frontend.src.Document_Formatter import *


class Task_Window(QWidget):  # Home extends QMainWindow

    def __init__(self, ui_object):
        super(QWidget, self).__init__()

        self.task_window = ui_object