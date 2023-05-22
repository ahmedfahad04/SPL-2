import json
import os
import cv2

# from Backend.Puzzle.puzzle import PuzzleWidget, PiecesList, MainWindow
from Frontend.src.Document_Formatter import *


class Evaluation_Window(QMainWindow):  # Home extends QMainWindow

    def __init__(self, ui_object):
        
        super(QMainWindow, self).__init__()
     
        self.evaluation_window = ui_object
        self.puzzle_image = r'E:\SPL2\SPL2 - GITHUB\EmPower\Student\Frontend\src\fish1.jpg'
        obj = cv2.imread(self.puzzle_image)

    def puzzle_window(self):
        
        pass 
        
        # puzzle frames 
        # puzzle_frames = [self.evaluation_window.puzzle_piece_frame, self.evaluation_window.puzzle_widget_frame]
        
        # # Create the main window for the puzzle
        # puzzle_window = MainWindow(self.puzzle_image, puzzle_frames)
        # puzzle_window.openImage('fish1.jpg')
        # puzzle_window.show()