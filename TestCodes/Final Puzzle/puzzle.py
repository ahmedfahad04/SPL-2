

import random
import cv2
import sys
import os 


from PyQt5 import QtGui

from PyQt5.QtCore import (pyqtSignal, QByteArray, QDataStream, QIODevice,
                          QMimeData, QPoint, QRect, QSize, Qt)
from PyQt5.QtGui import QDrag, QColor, QCursor, QIcon, QPainter, QPixmap
from PyQt5.QtWidgets import (QApplication, QFileDialog, QFrame, QHBoxLayout,
                             QListView, QListWidget, QListWidgetItem, QMainWindow, QMessageBox,
                             QSizePolicy, QWidget)

class ImageManager:
    
    def __init__(self) -> None:
        
        pass 
        # # Example usage
        # self.input_image_path = 'example.jpg'  # Replace with your image file path
        # self.brightness_factor = 0.5  # Adjust brightness factor between 0.0 (darker) and 2.0 (brighter)
        

    def adjust_brightness(self, image_path, brightness_factor):
        # Load the image
        image = cv2.imread(image_path)

        # Adjust the brightness
        adjusted_image = cv2.convertScaleAbs(image, alpha=brightness_factor)

        # Save the modified image
        output_path = os.getcwd()+'\\'+str(image_path.split('.')[0])+'_light.jpg'  # Modify the output filename as desired
        print(output_path)
        cv2.imwrite(output_path, adjusted_image)
        # cv2.imshow('NEW IMAGE', adjusted_image)

        print(f"Modified image saved as {output_path}")


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
        self.image_name = image_name.split('.')[0]

        self.setAcceptDrops(True)
        self.setMinimumSize(700, 700)
        self.setMaximumSize(800, 800)

    def clear(self):
        self.pieceLocations = []
        self.piecePixmaps = []
        self.pieceRects = []
        self.highlightedRect = QRect()
        self.inPlace = 0
        self.update()

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
            pieceData = event.mimeData().data('image/x-puzzle-piece')
            dataStream = QDataStream(pieceData, QIODevice.ReadOnly)
           
            square = self.targetSquare(event.pos())
            print("SQUARE: ",square)
            
            pixmap = QPixmap()
            location = QPoint()
            dataStream >> pixmap >> location
            
            print("Location: ", location)
            print("X: ", square.x())
            print("Y: ", square.y())
            
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
                QMessageBox().information(self, "Correct Location",
                                        f"{self.inPlace} pieces are in the correct location.")

                if self.inPlace == 4:
                    print('BINGO! You have completed the puzzle!')
                    self.puzzleCompleted.emit()
                    return
                
            elif location in self.alreadyPlacedLocation:
                print("Already Placed Location: ", location)
                return
            
            else:
                # # Retrieve the pixmap from the original location
                original_location = QPoint(square.x() // 400, square.y() // 400)
                print("Original Location: ", original_location)
                print("ALL PIECE LOCATION: ", self.pieceLocations)
                # original_pixmap = self.piecePixmaps[self.pieceLocations.index(
                #     original_location)]

                # self.piecePixmaps.append(original_pixmap)
                # self.pieceLocations.append(original_location)
                # self.pieceRects.append(square)

                # self.highlightedRect = QRect()
                # self.update(square)

                # event.setDropAction(Qt.MoveAction)
                # event.accept()

                QMessageBox().warning(self, "Incorrect Location",
                                    "The piece is placed incorrectly.")
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
        image = QPixmap(self.image_name+'_light.jpg')
        painter.drawPixmap(event.rect(), image)

        if self.highlightedRect.isValid():
            painter.setBrush(QColor("#ffcccc"))
            painter.setPen(Qt.NoPen)
            painter.drawRect(self.highlightedRect.adjusted(0, 0, -1, -1))

        for rect, pixmap in zip(self.pieceRects, self.piecePixmaps):
            painter.drawPixmap(rect, pixmap)

        painter.end()

    def targetSquare(self, position):
        print("POS X: ", position.x())
        print("POS Y: ", position.y())
        print("WIDTH: ", self.width()//2)
        print("HEIGHT: ", self.height()//2)
        print("Target: ", position.x() // (self.width() // 2) * (self.width() // 2))
        print("Target: ", position.y() // (self.height() // 2) * (self.height() // 2))
        
        return QRect(position.x()-50 // (self.width() // 2) * (self.width() // 2),
                     position.y()-50 // (self.height() // 2) * (self.height() // 2),
                     self.width() // 2, self.height() // 2)


class PiecesList(QListWidget):

    def __init__(self, parent=None):
        super(PiecesList, self).__init__(parent)
        
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)

        self.setViewMode(QListView.ListMode)
        
        # set the size of listview panel
        self.setFixedWidth(400)
        
        # set the position of listview to the left side
        self.move(0, 0)
        
        self.setIconSize(QSize(400, 400))
        self.setSpacing(5)

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
        
        print(pieceItem.data(Qt.UserRole+1).x(), pieceItem.data(Qt.UserRole+1).y())

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
            
        
class MainWindow(QMainWindow):

    def __init__(self, image_name ,parent=None):
        super(MainWindow, self).__init__(parent)

        self.puzzleImage = QPixmap()
        self.image_name = image_name
        # current window size

        self.setupMenus()
        self.setupWidgets()

        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.setWindowTitle("Puzzle")

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

    def setCompleted(self):
        QMessageBox.information(self, "Puzzle Completed",
                                "Congratulations! You have completed the puzzle!\nClick OK "
                                "to start again.",
                                QMessageBox.Ok)

        self.setupPuzzle()

    def setupPuzzle(self):
        size = min(self.puzzleImage.width(), self.puzzleImage.height())

        self.puzzleImage = self.puzzleImage.copy(self.puzzleImage.width(), self.puzzleImage.height() , size, size).scaled(400, 400, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # self.puzzleImage = self.puzzleImage.copy(
        #     (self.puzzleImage.width() - size)//2, (self.puzzleImage.height() - size)//2, size, size).scaled(400, 400, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        
        print("SIZE: ", self.puzzleImage.width() , self.puzzleImage.height())
        
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

    def setupMenus(self):
        fileMenu = self.menuBar().addMenu("&File")

        openAction = fileMenu.addAction("&Open...")
        openAction.setShortcut("Ctrl+O")

        exitAction = fileMenu.addAction("&Exit")
        exitAction.setShortcut("Ctrl+Q")

        gameMenu = self.menuBar().addMenu("&Game")

        restartAction = gameMenu.addAction("&Restart")

        openAction.triggered.connect(self.openImage)
        exitAction.triggered.connect(QApplication.instance().quit)
        restartAction.triggered.connect(self.setupPuzzle)

    def setupWidgets(self):
        
        frame = QFrame()
        frameLayout = QHBoxLayout(frame)

        self.piecesList = PiecesList()
        self.puzzleWidget = PuzzleWidget(self.image_name)
        self.puzzleWidget.puzzleCompleted.connect(self.setCompleted, Qt.QueuedConnection)

        frameLayout.addWidget(self.piecesList)
        frameLayout.addWidget(self.puzzleWidget)
        self.setCentralWidget(frame)


if __name__ == '__main__':

    # image_manager =  ImageManager()
    # image_manager.adjust_brightness('fish1.png', 0.2)

    app = QApplication(sys.argv)
    window = MainWindow(r'Images\fish1.jpg')
    window.openImage(r'Images\fish1.jpg')
    window.show()
    sys.exit(app.exec_())
