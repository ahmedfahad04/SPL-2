import datetime
import glob
import json
import random
import time
import cv2
from PIL import Image, ImageDraw

from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import (pyqtSignal, QByteArray, QDataStream, QIODevice,
                          QMimeData, QPoint, QRect, QSize, Qt)
from PyQt5.QtGui import QDrag, QColor, QCursor, QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import (QFileDialog, QHBoxLayout,
                             QListView, QListWidget, QListWidgetItem, QMessageBox,
                             QWidget)
from Frontend.src.Document_Formatter import *

saveUIObject = None # Global variable to track success of the puzzle

class ImageManager:

    def __init__(self, image_path) -> None:

        pass
        # # Example usage
        self.input_image_path = image_path  # Replace with your image file path
        # self.brightness_factor = 0.5  # Adjust brightness factor between 0.0 (darker) and 2.0 (brighter)

    def adjust_brightness(self, image_path, brightness_factor):
        # Load the image
        image = cv2.imread(image_path)
        # Adjust the brightness
        adjusted_image = cv2.convertScaleAbs(image, alpha=brightness_factor)

        # Save the modified image
        # Modify the output filename as desired
        output_path = str(image_path.split('.')[0])+'_light.png'
        print(output_path)
        cv2.imwrite(output_path, adjusted_image)
        # cv2.imshow('NEW IMAGE', adjusted_image)

        print(f"Modified image saved as {output_path}")

    def draw_transparent_line(self, image_path):

        # Open the image
        image = Image.open(image_path).convert("RGBA")

        # Create a transparent image of the same size
        transparent_image = Image.new("RGBA", image.size, (0, 0, 0, 0))

        # Create a draw object
        draw = ImageDraw.Draw(transparent_image)

        # Calculate the coordinates of the middle point
        width, height = image.size
        middle_x = width // 2
        middle_y = height // 2

        # Define the line coordinates
        line_start = (middle_x, 0)
        line_end = (middle_x, height)
        line_width = 10

        # Draw the horizontal line
        draw.line([line_start, line_end], fill=(
            0, 0, 0, 128), width=line_width)

        # Draw the vertical line
        line_start = (0, middle_y)
        line_end = (width, middle_y)
        draw.line([line_start, line_end], fill=(
            0, 0, 0, 128), width=line_width)

        # Composite the transparent image with the original image
        result = Image.alpha_composite(image, transparent_image)

        # Save the result image
        result.save(str(self.input_image_path.split('.')[0])+'_light.png')

    def process_image(self):

        self.adjust_brightness(self.input_image_path, 0.2)
        self.draw_transparent_line(
            str(self.input_image_path.split('.')[0])+'_light.png')


class PuzzleWidget(QWidget):

    puzzleCompleted = pyqtSignal()

    def __init__(self, image_name=None, parent=None):
        super(PuzzleWidget, self).__init__(parent)

        self.piecePixmaps = []
        self.pieceRects = []
        self.pieceLocations = []
        self.alreadyPlacedLocation = []
        self.highlightedRect = QRect()
        self.inPlace = 0
        self.totalAttempts = 0
        self.correctAttempts = 0
        self.wrongAttempts = 0
        self.performance = {}

        try:
            self.image_name = image_name.split('.')[0]
        except:
            pass

        # # timers to track time elapsed
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.updateTime)
        # self.timeElapsed = 0
        # self.startTimer()
        self.start_time = time.time()
        self.end_time = 0

        self.setAcceptDrops(True)
        self.setMinimumSize(800, 800)
        self.setMaximumSize(800, 800)

    def clear(self):
        self.pieceLocations = []
        self.piecePixmaps = []
        self.pieceRects = []
        self.highlightedRect = QRect()
        self.inPlace = 0

        self.timeElapsed = 0
        self.update()

    def updateTime(self):
        self.timeElapsed += 1

    def startTimer(self):
        # Timer updates every second (1000 milliseconds)
        self.timer.start(1000)

    def stopTimer(self):
        self.timer.stop()

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('image/x-puzzle-piece'):
            event.accept()
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        updateRect = self.highlightedRect
        self.highlightedRect = QRect()
        self.update(updateRect)
        event.accept()

    def dragMoveEvent(self, event):
        updateRect = self.highlightedRect.united(
            self.targetSquare(event.pos()))

        if event.mimeData().hasFormat('image/x-puzzle-piece') and self.findPiece(self.targetSquare(event.pos())) == -1:
            self.highlightedRect = self.targetSquare(event.pos())
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            self.highlightedRect = QRect()
            event.ignore()

        # self.update(updateRect)  # update after each placement of pieces

    def dropEvent(self, event):

        if event.mimeData().hasFormat('image/x-puzzle-piece') and self.findPiece(self.targetSquare(event.pos())) == -1:
            self.totalAttempts += 1
            pieceData = event.mimeData().data('image/x-puzzle-piece')
            dataStream = QDataStream(pieceData, QIODevice.ReadOnly)
            square = self.targetSquare(event.pos())
            pixmap = QPixmap()
            location = QPoint()
            dataStream >> pixmap >> location
            
            print("LOCATION: ", location)
            print("SQUARE: ", square.x(), square.y())
            

            if location == QPoint(square.x() // 400, square.y() // 400) and location not in self.alreadyPlacedLocation:
                self.pieceLocations.append(location)
                self.piecePixmaps.append(pixmap)
                self.pieceRects.append(square)

                self.highlightedRect = QRect()
                self.update(square)

                event.setDropAction(Qt.MoveAction)
                event.accept()

                # track already placed location
                self.alreadyPlacedLocation.append(location)

                self.inPlace += 1

                # play music when a piece is placed successfully
                QSound.play(r'Frontend\Audio_Track\small_clap_sound.wav')

                # count attemtps
                self.correctAttempts += 1

                if self.inPlace == 4:
                    print('BINGO! You have completed the puzzle!')

                    # play music when puzzle is completed
                    QSound.play(r'Frontend\Audio_Track\clap_sound.wav')

                    # show total attempts
                    print("Total Attempts: ", self.totalAttempts)
                    print("Correct Attempts: ", self.correctAttempts)
                    print("Wrong Attempts: ", self.wrongAttempts)

                    # # stop timer
                    # self.stopTimer()
                    self.timeElapsed = time.time() - self.start_time
                    print("Time Elapsed: {} seconds".format(self.timeElapsed))
                    
                    # change to celebration page
                    Puzzle_Window().change_page()
                    
                    # Get a list of matching folder paths
                    folder_set_name = glob.glob("Resources/p_*")[0]
                    
                    # read the student detaisl json file to fetch the name and id
                    with open('.student_details.json') as json_file:
                        data = json.load(json_file)
                        student_name = data['name']
                        student_id = data['id']
                    
                    # write total moves, time and date into a json file
                    self.performance['std_name'] = student_name
                    self.performance['std_id'] = student_id
                    self.performance['set_name'] = folder_set_name
                    self.performance['correct_attempt'] = str(self.correctAttempts)
                    self.performance['wrong_attempt'] = str(self.wrongAttempts)
                    self.performance['total_attempt'] = str(self.totalAttempts)
                    self.performance['success_rate'] = str(round((self.correctAttempts/self.totalAttempts)*100, 2))
                    self.performance['time'] = round(self.timeElapsed, 2)
                    self.performance['date'] = datetime.datetime.now().strftime("%Y-%m-%d")
                    
                    with open('Performance' + "/puzzle_results.json", "w+") as json_file:
                        json.dump(self.performance, json_file)

            elif location in self.alreadyPlacedLocation:
                print("Already Placed Location: ", location)
                return

            else:

                # count attempts
                self.wrongAttempts += 1

                QSound.play(r'Frontend\Audio_Track\mistake_sound.wav')
                # show_warning_message("সতর্কতা!", "পাজল টি ভুল জায়গায় রাখা হয়েছে। সঠিক জায়গায় রাখুন।")
        else:
            self.highlightedRect = QRect()
            event.ignore()
    
    def findPiece(self, pieceRect):
        try:
            return self.pieceRects.index(pieceRect)
        except ValueError:
            return -1

    def mousePressEvent(self, event):
        square = self.targetSquare(event.pos())
        found = self.findPiece(square)

        if found == -1:
            return

        location = self.pieceLocations[found]
        pixmap = self.piecePixmaps[found]
        del self.pieceLocations[found]
        del self.piecePixmaps[found]
        del self.pieceRects[found]

        print("SX: ", square.x()//400, "SY: ", square.y()//400)
        if location == QPoint(square.x() // 200, square.y() // 200):
            print("Correct Location", location)
            self.inPlace -= 1

        self.update(square)

        itemData = QByteArray()
        dataStream = QDataStream(itemData, QIODevice.WriteOnly)

        dataStream << pixmap << location

        mimeData = QMimeData()
        mimeData.setData('image/x-puzzle-piece', itemData)

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(event.pos() - square.topLeft())
        drag.setPixmap(pixmap)

        if drag.exec_(Qt.MoveAction) != Qt.MoveAction:
            self.pieceLocations.insert(found, location)
            self.piecePixmaps.insert(found, pixmap)
            self.pieceRects.insert(found, square)
            self.update(self.targetSquare(event.pos()))

            if location == QPoint(square.x() // 200, square.y() // 200):
                self.inPlace += 1

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(), Qt.magenta)

        #! TODO: image should be light colored [DONE] and the the rect should not be resized.
        image = QPixmap(self.image_name+'_light.png')
        painter.drawPixmap(event.rect(), image)

        if self.highlightedRect.isValid():
            painter.setBrush(QColor("#ffcccc"))
            painter.setPen(Qt.NoPen)
            painter.drawRect(self.highlightedRect.adjusted(0, 0, -1, -1))

        for rect, pixmap in zip(self.pieceRects, self.piecePixmaps):
            painter.drawPixmap(rect, pixmap)

        painter.end()

    def targetSquare(self, position):
        return QRect(position.x() // (self.width() // 2) * (self.width() // 2),
                     position.y() // (self.height() // 2) * (self.height() // 2),
                     self.width() // 2, self.height() // 2)


class PiecesList(QListWidget):

    def __init__(self, parent=None):
        super(PiecesList, self).__init__(parent)

        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)

        self.setViewMode(QListView.ListMode)
        self.setMovement(QListView.Snap)

        # set the size of listview panel
        self.setFixedWidth(300)

        # set the position of listview to the left side
        self.move(0, 0)

        self.setIconSize(QSize(400, 400))
        self.setSpacing(3)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('image/x-puzzle-piece'):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):

        if event.mimeData().hasFormat('image/x-puzzle-piece'):
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasFormat('image/x-puzzle-piece'):
            pieceData = event.mimeData().data('image/x-puzzle-piece')
            dataStream = QDataStream(pieceData, QIODevice.ReadOnly)
            pixmap = QPixmap()
            location = QPoint()
            dataStream >> pixmap >> location

            self.addPiece(pixmap, location)

            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def addPiece(self, pixmap, location):
        pieceItem = QListWidgetItem(self)
        pieceItem.setIcon(QIcon(pixmap))
        pieceItem.setData(Qt.UserRole, pixmap)
        pieceItem.setData(Qt.UserRole+1, location)
        pieceItem.setFlags(Qt.ItemIsEnabled |
                           Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)

        print(pieceItem.data(Qt.UserRole+1).x(),
              pieceItem.data(Qt.UserRole+1).y())

    def startDrag(self, supportedActions):
        item = self.currentItem()

        if item is None:
            return

        itemData = QByteArray()
        dataStream = QDataStream(itemData, QIODevice.WriteOnly)
        pixmap = QPixmap(item.data(Qt.UserRole))
        location = item.data(Qt.UserRole+1)

        dataStream << pixmap << location

        mimeData = QMimeData()
        mimeData.setData('image/x-puzzle-piece', itemData)

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(QPoint(pixmap.width() // 2, pixmap.height() // 2))
        drag.setPixmap(pixmap)

        dragAction = drag.exec_(supportedActions)
        if dragAction == Qt.MoveAction:
            if self.currentItem() is not None:
                self.takeItem(self.row(item))
        elif dragAction == Qt.IgnoreAction:
            self.addItem(item)


class MainWindow:

    def __init__(self, image_name=None, frames=None, home_obj=None, parent=None):

        try:
            self.puzzleImage = QPixmap()
            self.image_name = image_name
            self.frames = frames
            self.home_object = home_obj
            self.piece_frame_layout = None
            self.widget_frame_layout = None

        except:
            pass

        self.setupWidgets()

        self.puzzleWidget = PuzzleWidget(self.image_name)

    def openImage(self, path=None):
        if not path:
            path, _ = QFileDialog.getOpenFileName(self, "Open Image", '',
                                                  "Image Files (*.png *.jpg *.bmp)")

        if path:
            newImage = QPixmap()
            if not newImage.load(path):
                QMessageBox.warning(self, "Open Image",
                                    "The image file could not be loaded.",
                                    QMessageBox.Cancel)
                return

            self.puzzleImage = newImage
            self.setupPuzzle()

    def setupPuzzle(self):
        
        size = min(self.puzzleImage.width(), self.puzzleImage.height())

        self.puzzleImage = self.puzzleImage.copy(self.puzzleImage.width(), self.puzzleImage.height(
        ), size, size).scaled(400, 400, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # self.puzzleImage = self.puzzleImage.copy(
        #     (self.puzzleImage.width() - size)//2, (self.puzzleImage.height() - size)//2, size, size).scaled(400, 400, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        print("SIZE: ", self.puzzleImage.width(), self.puzzleImage.height())

        self.piecesList.clear()

        # make pieces of puzzle
        for y in range(2):
            for x in range(2):
                pieceImage = self.puzzleImage.copy(x * (self.puzzleImage.width() // 2), y * (
                    self.puzzleImage.height() // 2), self.puzzleImage.width() // 2, self.puzzleImage.height() // 2)
                self.piecesList.addPiece(pieceImage, QPoint(x, y))

        random.seed(QCursor.pos().x() ^ QCursor.pos().y())

        for i in range(self.piecesList.count()):
            if random.random() < 0.5:
                item = self.piecesList.takeItem(i)
                self.piecesList.insertItem(0, item)

        self.puzzleWidget.clear()
        self.puzzleWidget.alreadyPlacedLocation = []

    def setupWidgets(self):

        piece_frame = self.frames[0]
        widget_frame = self.frames[1]

        self.piece_frame_layout = QHBoxLayout(piece_frame)
        self.widget_frame_layout = QHBoxLayout(widget_frame)

        self.piecesList = PiecesList()
        self.puzzleWidget = PuzzleWidget(self.image_name)

        self.piece_frame_layout.addWidget(self.piecesList)
        self.widget_frame_layout.addWidget(self.puzzleWidget)
       

class Puzzle_Window:

    def __init__(self, ui_object=None, puzzle_frames=None):

        global saveUIObject
        
        # if saveUIObject is null, then set it to the ui_object
        if saveUIObject == None:  
            saveUIObject = ui_object
                    
        self.evaluation_window = saveUIObject
        self.puzzle_frames = puzzle_frames
        self.change_new_window = None

        #! TODO: Change the image dynamically
        
        folder_pattern = "Resources/p_*/*.png"  # Pattern to match folders starting with "m_"
        self.puzzle_image = glob.glob(folder_pattern)[0]

    def launch_puzzle(self):


        img = ImageManager(self.puzzle_image)
        img.process_image()

        # Create the main window for the puzzle
        window = MainWindow(self.puzzle_image, self.puzzle_frames, self.evaluation_window)
        window.openImage(self.puzzle_image)
        return self.change_new_window
        
        
    def change_page(self):
        
        self.evaluation_window.stackedWidget.setCurrentWidget(self.evaluation_window.celebration_page)
        self.change_new_window = True