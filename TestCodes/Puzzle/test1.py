import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap, QResizeEvent

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
        self.image = QPixmap('flag.png')

        # Divide the image into 4 pieces
        self.pieces = []
        for i in range(2):
            for j in range(2):
                piece = self.image.copy(j * self.image.width()//2, i * self.image.height()//2, self.image.width()//2, self.image.height()//2)
                self.pieces.append(piece)

        # Add the pieces to the grid
        for i in range(2):
            for j in range(2):
                label = QLabel()
                label.setPixmap(self.pieces[i * 2 + j])
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

        for i in range(2):
            for j in range(2):
                label = self.grid.itemAtPosition(i, j).widget()
                label.setPixmap(self.pieces[i * 2 + j])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PuzzleGame()
    sys.exit(app.exec_())
