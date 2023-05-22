import sys

from PyQt5.QtGui import QPixmap, QImage, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl, QRect, QPoint, QFile


class Window(QWidget):

    def __init__(self, filename):
        super().__init__()

        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(350, 100, 800, 800)
        self.setWindowIcon(QIcon('player.png'))
        self.content_path = filename

        p = self.palette()
        p.setColor(QPalette.Window, Qt.white)
        self.setPalette(p)

        self.init_ui()

        self.show()

    def init_ui(self):

        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # create videowidget object
        self.videowidget = QVideoWidget()
        self.videowidget.setStyleSheet("border: 2px solid rgb(0, 43, 91)")

        # create open button
        openBtn = QPushButton('ফাইল ওপেন করুন')
        openBtn.clicked.connect(self.open_file)

        # create button for playing
        self.playBtn = QPushButton()
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        # create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        # create volume slider
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.sliderMoved.connect(self.set_volume)

        # create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # create volume label
        self.volume_lbl = QLabel("ভলিউম")
        self.volume_lbl.setStyleSheet("color: white")
        self.volume_lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.volume_lbl.setMinimumSize(350, 0)
        self.volume_lbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # create button for taking a snapshot
        snapshotBtn = QPushButton('Take Snapshot')
        snapshotBtn.clicked.connect(self.take_snapshot)

        # create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)

        # set widgets to the hbox layout
        hboxLayout.addWidget(self.slider)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(openBtn)
        hbox2.addWidget(self.playBtn)
        hbox2.addWidget(snapshotBtn)  # Add the snapshot button here
        hbox2.addWidget(self.volume_lbl)
        hbox2.addWidget(self.volume_slider)

        # create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addLayout(hbox2)
        vboxLayout.addWidget(self.label)

        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(self.videowidget)

        filename = self.content_path

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))

        # media player signals

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.volumeChanged.connect(self.volume_changed)
        self.mediaPlayer.setVolume(50)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

    def play_video(self):

        print('Playing...')

        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause)

            )

        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)

            )

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())

    def volume_changed(self, volume):
        self.volume_slider.setValue(volume)

    def set_volume(self, volume):
        self.mediaPlayer.setVolume(volume)

    def take_snapshot(self):
        # Get the video widget's position and size
        video_pos = self.videowidget.mapToGlobal(QPoint(0, 0))
        video_size = self.videowidget.size()

        # Calculate the coordinates and size for grabbing the video widget only
        grab_x = video_pos.x()
        grab_y = video_pos.y()
        grab_width = video_size.width()
        grab_height = video_size.height()

        # Grab the contents of the video widget
        pixmap = QApplication.primaryScreen().grabWindow(0, grab_x, grab_y, grab_width, grab_height)

        # Save the pixmap as an image file
        snapshot_path, _ = QFileDialog.getSaveFileName(self, "Save Snapshot", "", "PNG Image (*.png)")
        if snapshot_path:
            pixmap.save(snapshot_path, "PNG")
            QFile(snapshot_path).flush()
            print("screen shot saved successfully")


app = QApplication(sys.argv)
window = Window("sampleVideo.mp4")
sys.exit(app.exec_())