from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStyle 
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl


class Window(QWidget):
    
    def __init__(self, filename):
        super().__init__()

        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(350, 100, 600, 300)
        self.setWindowIcon(QIcon('player.png'))
        self.content_path = filename
        self.mediaPlayer = None 

        self.init_ui()
        self.show()


    def init_ui(self):

        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # create videowidget object
        videowidget = QVideoWidget()
        videowidget.setStyleSheet("border: 2px solid rgb(0, 43, 91)")
        
        # create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)

        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(videowidget)

        filename = self.content_path

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            
        self.play_video()


    def play_video(self):
        print('Playing...')
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()


# app = QApplication(sys.argv)
# window = Window('Backend\media.mp4')
# sys.exit(app.exec_())
