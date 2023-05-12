import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QMessageBox
from PyQt5.QtGui import QPixmap, QResizeEvent, QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent, QDropEvent
from PyQt5.QtCore import Qt, QMimeData

class PuzzleGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Puzzle Game')
        self.setMinimumSize(400, 400)

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        # Load the image
        self.image = QPixmap('cool_guy.png')

        # Divide the image into 4 pieces
        self.pieces = []
        for i in range(2):
            for j in range(2):
                piece = self.image.copy(j * self.image.width()//2, i * self.image.height()//2, self.image.width()//2, self.image.height()//2)
                self.pieces.append(piece)

        # Shuffle the pieces
        from random import shuffle
        shuffle(self.pieces)

        # Add the shuffled pieces to the grid
        for i in range(2):
            for j in range(2):
                label = QLabel()
                label.setPixmap(self.pieces[i * 2 + j])
                label.setAcceptDrops(True)
                label.setAlignment(Qt.AlignCenter)
                self.grid.addWidget(label, i, j)

        self.show()

    def resizeEvent(self, event: QResizeEvent) -> None:
        # When the widget is resized, resize the image to fit the new size and update the pieces
        self.image = self.image.scaled(self.size(), aspectRatioMode=1)
        self.pieces = []
        for i in range(2):
            for j in range(2):
                piece = self.image.copy(j * self.image.width()//2, i * self.image.height()//2, self.image.width()//2, self.image.height()//2)
                self.pieces.append(piece)

        # Shuffle the pieces
        from random import shuffle
        shuffle(self.pieces)

        for i in range(2):
            for j in range(2):
                label = self.grid.itemAtPosition(i, j).widget()
                label.setPixmap(self.pieces[i * 2 + j])

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        # Accept the drag event if it contains a pixmap
        if event.mimeData().hasImage():
            event.acceptProposedAction()

    def dragMoveEvent(self, event: QDragMoveEvent) -> None:
        # Move the label to the position of the drag event
        label = self.childAt(event.pos())
        if label and label.acceptDrops():
            event.acceptProposedAction()
            label.move(event.pos() - label.rect().center())

    def dragLeaveEvent(self, event: QDragLeaveEvent) -> None:
        # Reset the position of the label when the drag event leaves the widget
        label = self.sender()
        if label and label.acceptDrops():
            label.move(label.pos() - label.rect().center())

    def dropEvent(self, event: QDropEvent) -> None:
        # Swap the pixmaps of the two labels
        label = self.childAt(event.pos())
        if label and label.acceptDrops():
            source = event.source()
            pixmap1 = label.pixmap()
            pixmap2 = source.pixmap()
            label.setPixmap(pixmap2)
            source.setPixmap(pixmap1)

            # Check if the puzzle is solved
            solved = True
            for i in range(2):
                for j in range(2):
                    if self.grid.itemAtPosition(i, j).widget().pixmap() != self.pieces[i * 2 + j]:
                        solved = False
                        break
                if not solved:
                    break

            if solved:
                # If the puzzle is solved, show a success message
                QMessageBox.information(self, 'Congratulations', 'You solved the puzzle!')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PuzzleGame()
    sys.exit(app.exec_())