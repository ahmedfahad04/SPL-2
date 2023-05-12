import sys

from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

import ui_puzzle


class PuzzleGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.loadPicture()

    def initUI(self):
        self.puzzleMainWindow = ui_puzzle.Ui_puzzleMainWidget()
        self.puzzleMainWindow.setupUi(self)
        self.show()

        # Add event listeners for label clicks
        self.puzzleMainWindow.container_1.mousePressEvent = lambda event: self.labelClicked(event,
                                                                                            self.puzzleMainWindow.container_1)
        self.puzzleMainWindow.container_2.mousePressEvent = lambda event: self.labelClicked(event,
                                                                                            self.puzzleMainWindow.container_2)
        self.puzzleMainWindow.container_3.mousePressEvent = lambda event: self.labelClicked(event,
                                                                                            self.puzzleMainWindow.container_3)
        self.puzzleMainWindow.container_4.mousePressEvent = lambda event: self.labelClicked(event,
                                                                                            self.puzzleMainWindow.container_4)


    def loadPicture(self):
            # Load the image
            img = Image.open("cool_guy.png")

            # Get the dimensions of the image
            width, height = img.size

            # Calculate the dimensions of each quadrant
            quad_width = width // 2
            quad_height = height // 2

            # Divide the image into four quadrants
            quads = []
            for i in range(2):
                for j in range(2):
                    box = (i * quad_width, j * quad_height, (i + 1) * quad_width, (j + 1) * quad_height)
                    quads.append(img.crop(box))

            # quads[0] now contains the top-left quadrant of the image
            # quads[2] contains the top-right quadrant
            # quads[1] contains the bottom-left quadrant
            # quads[3] contains the bottom-right quadrant

            ### Redefined image pices to make Qpixmap
            pixMappedImages = []
            for quad in quads:
                pixMappedImages.append(quad.toqpixmap().scaled(self.puzzleMainWindow.container_1.width(), self.puzzleMainWindow.container_1.height(), aspectRatioMode=Qt.IgnoreAspectRatio))

            ### now fit the pictures to lables
            self.puzzleMainWindow.gridLayout.setSpacing(0)

            self.puzzleMainWindow.container_1.setPixmap(pixMappedImages[0])
            self.puzzleMainWindow.container_2.setPixmap(pixMappedImages[2])
            self.puzzleMainWindow.container_3.setPixmap(pixMappedImages[1])
            self.puzzleMainWindow.container_4.setPixmap(pixMappedImages[3])


    def labelClicked(self, event, label):
        # Check if the left mouse button was clicked
        if event.button() == Qt.LeftButton:
            # Get the source label and pixmap
            source_label = label
            source_pixmap = source_label.pixmap()

            # Set the source label's pixmap to None
            source_label.setPixmap(None)

            # Add event listeners for label releases
            self.puzzleMainWindow.container_1.mouseReleaseEvent = lambda event: self.labelReleased(event, self.puzzleMainWindow.container_1, source_label, source_pixmap)
            self.puzzleMainWindow.container_2.mouseReleaseEvent = lambda event: self.labelReleased(event, self.puzzleMainWindow.container_2, source_label, source_pixmap)
            self.puzzleMainWindow.container_3.mouseReleaseEvent = lambda event: self.labelReleased(event, self.puzzleMainWindow.container_3, source_label, source_pixmap)
            self.puzzleMainWindow.container_4.mouseReleaseEvent = lambda event: self.labelReleased(event, self.puzzleMainWindow.container_4, source_label, source_pixmap)

    def labelReleased(self, event, target_label, source_label, source_pixmap):
        # Check if the left mouse button was released
        if event.button() == Qt.LeftButton:
            # Get the target label and pixmap
            target_pixmap = target_label.pixmap()

            # Set the source label's pixmap to the target label's pixmap
            source_label.setPixmap(target_pixmap)

            # Set the target label's pixmap to the source pixmap
            target_label.setPixmap(source_pixmap)

            # Remove the event listeners for label releases
            self.puzzleMainWindow.container_1.mouseReleaseEvent = None
            self.puzzleMainWindow.container_2.mouseReleaseEvent = None
            self.puzzleMainWindow.container_3.mouseReleaseEvent = None
            self.puzzleMainWindow.container_4.mouseReleaseEvent = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PuzzleGame()
    sys.exit(app.exec_())
