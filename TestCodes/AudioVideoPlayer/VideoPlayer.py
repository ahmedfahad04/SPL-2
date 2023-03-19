import os
import sys

from PyQt5 import QtWidgets, QtMultimedia, uic, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle("Demo Media Player")
        self.ui = uic.loadUi(os.path.join(os.path.dirname(__file__), "form.ui"), self)
        self.player = QtMultimedia.QMediaPlayer(None, QtMultimedia.QMediaPlayer.VideoSurface)
        file = os.path.join(os.path.dirname(__file__), "AudioVideoPlayer\sampleVideo.mp4")
        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file)))
        self.player.setVideoOutput(self.ui.widget)
        self.player.play()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec())
