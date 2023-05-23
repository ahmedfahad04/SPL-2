from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag


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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a draggable label
        self.draggable_label = DraggableLabel("Drag me")
        self.setCentralWidget(self.draggable_label)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
