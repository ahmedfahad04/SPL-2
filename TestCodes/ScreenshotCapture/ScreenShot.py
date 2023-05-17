import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint

class ScreenshotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Screenshot Window")
        self.setGeometry(100, 100, 500, 500)

        self.screenshot_label = QLabel(self)
        self.screenshot_label.setGeometry(0, 0, 500, 500)

        self.start_pos = QPoint()
        self.end_pos = QPoint()
        self.is_drawing = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_pos = event.pos()
            self.is_drawing = True

    def mouseMoveEvent(self, event):
        if self.is_drawing:
            self.end_pos = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.is_drawing:
            self.end_pos = event.pos()
            self.is_drawing = False

            window = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId(),
                                                             self.start_pos.x(), self.start_pos.y(),
                                                             self.end_pos.x() - self.start_pos.x(),
                                                             self.end_pos.y() - self.start_pos.y())
            window.save("screenshot.png", "png")
            print("successfully taken screen shot")


    def paintEvent(self, event):
        if self.is_drawing:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawRect(self.start_pos.x(), self.start_pos.y(), self.end_pos.x() - self.start_pos.x(),
                             self.end_pos.y() - self.start_pos.y())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    screenshot_window = ScreenshotWindow()
    screenshot_window.show()

    sys.exit(app.exec_())
