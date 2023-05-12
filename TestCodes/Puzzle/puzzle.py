import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QDrag
from PyQt5.QtCore import Qt, QMimeData


class PuzzleGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Puzzle Game")
        self.setGeometry(100, 100, 500, 500)

        # Load the image
        self.image = QPixmap("cool_guy.png")

        # Divide the image into four pieces
        width = self.image.width() // 2
        height = self.image.height() // 2
        self.image_pieces = [
            self.image.copy(0, 0, width, height),
            self.image.copy(width, 0, width, height),
            self.image.copy(0, height, width, height),
            self.image.copy(width, height, width, height)
        ]

        # Create the labels for the image and the image pieces
        self.image_label = QLabel(self)
        self.image_label.setPixmap(self.image)
        self.image_label.setGeometry(50, 50, 250, 250)

        self.piece_labels = []
        for i in range(4):
            piece_label = QLabel(self)
            piece_label.setPixmap(self.image_pieces[i])
            piece_label.setGeometry(350 + 75 * (i % 2), 50 + 125 * (i // 2), 125, 125)
            piece_label.setAcceptDrops(True)
            piece_label.piece_index = i
            piece_label.mousePressEvent = lambda event, label=piece_label: self.mousePressEvent(event, label)
            self.piece_labels.append(piece_label)

        # Create the check button
        self.check_button = QPushButton("Check", self)
        self.check_button.setGeometry(200, 400, 100, 50)
        self.check_button.clicked.connect(self.check_puzzle)

        # Initialize the puzzle state
        self.puzzle_state = [None, None, None, None]

    def mousePressEvent(self, event, label):
        if event.button() == Qt.LeftButton:
            pixmap = label.pixmap()
            mime_data = QMimeData()
            mime_data.setImageData(pixmap.toImage())

            drag = QDrag(self)
            drag.setMimeData(mime_data)
            drag.setPixmap(pixmap)
            drag.exec_()

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        piece_index = event.source().piece_index
        event.source().setPixmap(QPixmap())
        self.puzzle_state[piece_index] = event.mimeData().imageData()
        self.check_puzzle()

    def check_puzzle(self):
        if None not in self.puzzle_state:
            if self.puzzle_state == self.image_pieces:
                self.image_label.setPixmap(self.image)
                self.check_button.setEnabled(False)
                for piece_label in self.piece_labels:
                    piece_label.setAcceptDrops(False)
                    piece_label.setPixmap(QPixmap())
                    piece_label.setCursor(Qt.ArrowCursor)
                    piece_label.mousePressEvent = None
                print("Congratulations! You completed the puzzle!")
            else:
                self.puzzle_state = [None, None, None, None]
                for piece_label in self.piece_labels:
                    piece_label.setPixmap(self.image_pieces[piece_label.piece_index])
                print("Incorrect! Please try again.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = PuzzleGame()
    game.show()
    sys.exit(app.exec_())
