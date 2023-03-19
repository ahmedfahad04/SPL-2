import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
import time

class VideoPlayer(QDialog):
    def __init__(self):
        super(VideoPlayer, self).__init__()
        loadUi('player.ui', self)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.play_video)
        self.timer.start(1)

    def play_video(self):
        cap = cv2.VideoCapture('test.mp4')
        while True:
            ret, frame = cap.read()
            if ret:
                # Convert color space from BGR to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(image)
                self.video_label.setPixmap(pixmap)
                self.video_label.setScaledContents(True)
                QApplication.processEvents()
                time.sleep(0.03) # add a delay of 33 milliseconds (30fps)
            else:
                break     
        cap.release()
        
     # Override the closeEvent method to stop the QTimer when the window is closed
    def closeEvent(self, event):
        self.timer.stop()
        super(VideoPlayer, self).closeEvent(event)
        
    
app = QApplication([])
window = VideoPlayer()
window.show()
app.exec_()


